import time

from gmail.gmail_loader import load_jobs_from_gmail
from gmail.gmail_labels import apply_label, archive_message
from services.writer import save_jobs
from services.summary import print_summary
from services.html_report import generate_html_report
from services.banner import (
    print_banner,
    print_step,
    print_success,
    print_divider
)
from scoring.llm_scorer import score_job_llm
from workflow.decision_engine import decide
from workflow.label_filter import already_processed
from workflow.duplicate_filter import deduplicate_jobs
from utils.logger import setup_logger
from services.job_page_fetcher import fetch_job_page
from services.job_page_parser import parse_job_description
from services.job_page_parser import (
    parse_job_description,
    parse_salary_from_description,
    parse_compensation_from_description
)

logger = setup_logger()

start = time.perf_counter()

logger.info("AI Job Intelligence workflow started")

print_banner()

print_step("Connecting to Gmail...")
logger.info("Connecting to Gmail")

print_success("Connected to Gmail")
logger.info("Connected to Gmail")
print()

print_step("Reading job alerts...")
logger.info("Reading job alerts")

jobs = load_jobs_from_gmail(
    query="label:Jobs",
    max_results=1
)

print_success(f"Loaded {len(jobs)} jobs")
logger.info("Loaded %s jobs", len(jobs))
print()

print_step("Enriching job descriptions...")
logger.info("Starting job enrichment")

for job in jobs:
    try:
        html = fetch_job_page(job.url)

        job.description = parse_job_description(
            html
        )
           
        description_salary = parse_salary_from_description(
            job.description
        )

        if description_salary > job.salary:
            job.salary = description_salary

        logger.info(
            "JOB ENRICHED | title=%s | company=%s | description_length=%s",
            job.title,
            job.company,
            len(job.description)
        )

    except Exception:
        logger.exception(
            "JOB ENRICHMENT FAILED | title=%s | company=%s",
            job.title,
            job.company
        )

        job.description = ""

print_success("Job enrichment complete")
logger.info("Job enrichment complete")
print()

print_step("Removing duplicates...")
logger.info("Removing duplicate jobs")

jobs = deduplicate_jobs(jobs)

print_success(f"{len(jobs)} unique jobs remain")
logger.info(
    "%s unique jobs remain after deduplication",
    len(jobs)
)
print()

processed_jobs = []

print_step("Scoring jobs with OpenAI...")
logger.info("Starting OpenAI job scoring")

total = len(jobs)

for job in jobs:

    if already_processed(job):
        print(f"Skipping already processed job: {job}")
        print("-" * 40)

        logger.info(
            "SKIPPED JOB | title=%s | company=%s | reason=already_processed",
            job.title,
            job.company
        )

        continue

    logger.info(
        "SCORING JOB | title=%s | company=%s | url=%s",
        job.title,
        job.company,
        job.url
    )

    try:
        job.score, job.summary, job.reasons = score_job_llm(job)
        job.decision = decide(job.score)

        logger.info(
            "SCORED JOB | title=%s | company=%s | score=%s | decision=%s",
            job.title,
            job.company,
            job.score,
            job.decision
        )

    except Exception:
        logger.exception(
            "SCORING FAILED | title=%s | company=%s",
            job.title,
            job.company
        )

        raise

    try:
        apply_label(
            job.message_id,
            job.decision
        )

        logger.info(
            "GMAIL LABEL | company=%s | label=%s",
            job.company,
            job.decision
        )

    except Exception:
        logger.exception(
            "GMAIL LABEL FAILED | company=%s | label=%s",
            job.company,
            job.decision
        )


    print(
        f"[✓] {len(processed_jobs) + 1}/{total} "
        f"{job.company}"
    )

    print(f"    → {job.decision}")

    if job.decision == "Jobs Reject":
        archive_message(job.message_id)
        print("    → Archived")

        logger.info(
            "ARCHIVED JOB | title=%s | company=%s",
            job.title,
            job.company
        )

    job.labels.append(job.decision)
    processed_jobs.append(job)

    print()
    print(job)
    print(f"Score: {job.score}")
    print(f"Decision: {job.decision}")
    print(
        f"Reasons: {', '.join(job.reasons)}"
    )
    print("-" * 40)

print_success("Scoring complete")
logger.info("OpenAI job scoring complete")
print()

print_divider()
print("SUMMARY")
print_divider()

print_summary(processed_jobs)

print_step("Saving reports...")
logger.info("Saving reports")

save_jobs(
    processed_jobs,
    "output/scored_jobs.json"
)

generate_html_report(
    processed_jobs,
    "output/job_report.html"
)

print_success("Reports written")

logger.info(
    "Reports written | json=output/scored_jobs.json | "
    "html=output/job_report.html"
)

print()

elapsed = time.perf_counter() - start

logger.info(
    "WORKFLOW COMPLETE | jobs_processed=%s | elapsed_seconds=%.2f",
    len(processed_jobs),
    elapsed
)

print("=" * 50)
print("Workflow Complete")
print("=" * 50)
print(
    f"Jobs processed : {len(processed_jobs)}"
)
print(
    f"Elapsed time   : {elapsed:.2f} seconds"
)
print(
    "JSON report    : output/scored_jobs.json"
)
print(
    "HTML report    : output/job_report.html"
)
print("=" * 50)
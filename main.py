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


start = time.perf_counter()

print_banner()

print_step("Connecting to Gmail...")
print_success("Connected to Gmail")
print()

print_step("Reading job alerts...")
jobs = load_jobs_from_gmail(
    query="label:Jobs",
    max_results=1
)
print_success(f"Loaded {len(jobs)} jobs")
print()

print_step("Removing duplicates...")
jobs = deduplicate_jobs(jobs)
print_success(f"{len(jobs)} unique jobs remain")
print()

processed_jobs = []

print_step("Scoring jobs with OpenAI...")
total = len(jobs)

for job in jobs:

    if already_processed(job):
        print(f"Skipping already processed job: {job}")
        print("-" * 40)
        continue

    job.score, job.summary, job.reasons = score_job_llm(job)
    job.decision = decide(job.score)

    apply_label(job.message_id, job.decision)
    print(f"[✓] {len(processed_jobs) + 1}/{total} {job.company}")
    print(f"    → {job.decision}")

    if job.decision == "Jobs Reject":
        archive_message(job.message_id)
        print("    → Archived")

    job.labels.append(job.decision)
    processed_jobs.append(job)

    print()
    print(job)
    print(f"Score: {job.score}")
    print(f"Decision: {job.decision}")
    print(f"Reasons: {', '.join(job.reasons)}")
    print("-" * 40)

print_success("Scoring complete")
print()

print_divider()
print("SUMMARY")
print_divider()
print_summary(processed_jobs)

print_step("Saving reports...")
save_jobs(processed_jobs, "output/scored_jobs.json")
generate_html_report(processed_jobs, "output/job_report.html")
print_success("Reports written")
print()

elapsed = time.perf_counter() - start

print("=" * 50)
print("Workflow Complete")
print("=" * 50)
print(f"Jobs processed : {len(processed_jobs)}")
print(f"Elapsed time   : {elapsed:.2f} seconds")
print("JSON report    : output/scored_jobs.json")
print("HTML report    : output/job_report.html")
print("=" * 50)
import json
import os

from dotenv import load_dotenv
from openai import OpenAI

from services.prompt_loader import load_prompt


load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def clean_json_response(content):
    """
    Removes Markdown code fences from an LLM response
    before JSON parsing.
    """

    content = content.strip()

    if content.startswith("```json"):
        content = content[7:]

    elif content.startswith("```"):
        content = content[3:]

    if content.endswith("```"):
        content = content[:-3]

    return content.strip()


def normalize_compensation_type(compensation_type):
    """
    Normalizes compensation types returned by the LLM.
    """

    value = str(
        compensation_type or ""
    ).strip().lower()

    compensation_types = {
        "base": "Base Salary",
        "base salary": "Base Salary",
        "base pay": "Base Salary",
        "ote": "OTE",
        "on-target earnings": "OTE",
        "on target earnings": "OTE",
        "salary": "Salary",
        "hourly": "Hourly",
        "unknown": "Unknown",
        "": "Unknown"
    }

    return compensation_types.get(
        value,
        "Unknown"
    )


def score_job_llm(job):
    """
    Scores and enriches a Job object using OpenAI.

    Returns:
        tuple: score, summary, reasons
    """

    base_prompt = load_prompt(
        "prompts/job_scoring.txt"
    )

    job_context = f"""
=========================================================
JOB DATA
=========================================================

Title: {job.title}
Company: {job.company}
Location: {job.location}
Source: {job.source}
URL: {job.url}

=========================================================
JOB DESCRIPTION
=========================================================

{job.description}
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": (
                    base_prompt
                    + "\n\n"
                    + job_context
                )
            }
        ],
        temperature=0
    )

    content = (
        response
        .choices[0]
        .message
        .content
    )

    clean_content = clean_json_response(
        content
    )

    result = json.loads(
        clean_content
    )

    score = int(
        result["score"]
    )

    summary = str(
        result["summary"]
    ).strip()

    reasons = result["reasons"]

    job.compensation_min = int(
        result.get(
            "compensation_min",
            0
        )
        or 0
    )

    job.compensation_max = int(
        result.get(
            "compensation_max",
            0
        )
        or 0
    )

    job.compensation_type = (
        normalize_compensation_type(
            result.get(
                "compensation_type",
                "Unknown"
            )
        )
    )

    job.salary = job.compensation_max

    return score, summary, reasons
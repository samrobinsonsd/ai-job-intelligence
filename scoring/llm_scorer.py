import json
import os

from dotenv import load_dotenv
from openai import OpenAI

from services.prompt_loader import load_prompt

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def clean_json_response(content):
    """
    Removes Markdown code fences from an LLM response so json.loads()
    can parse the raw JSON.
    """

    content = content.strip()

    if content.startswith("```json"):
        content = content.replace("```json", "", 1)

    if content.startswith("```"):
        content = content.replace("```", "", 1)

    if content.endswith("```"):
        content = content[:-3]

    return content.strip()


def score_job_llm(job):
    """
    Scores a Job object using OpenAI.

    Returns:
        tuple: score, reasons
    """

    base_prompt = load_prompt("prompts/job_scoring.txt")

    job_context = f"""
    Job:
    Title: {job.title}
    Company: {job.company}
    Location: {job.location}
    Salary: {job.salary}
    Source: {job.source}
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": base_prompt + "\n\n" + job_context
            }
        ],
        temperature=0
    )

    content = response.choices[0].message.content
    
    clean_content = clean_json_response(content)
    
    result = json.loads(clean_content)
    
    score = result["score"]
    summary = result["summary"]
    reasons = result["reasons"]

    return score, summary, reasons
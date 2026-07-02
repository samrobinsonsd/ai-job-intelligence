from gmail.html_parser import parse_linkedin_jobs_from_html

with open("sample_email.html", "r", encoding="utf-8") as file:
    html = file.read()

jobs = parse_linkedin_jobs_from_html(html)

print(f"Found {len(jobs)} jobs\n")

for job in jobs:
    print(job)
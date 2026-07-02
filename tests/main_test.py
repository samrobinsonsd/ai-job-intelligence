from gmail.gmail_loader import load_jobs_from_gmail

jobs = load_jobs_from_gmail(max_results=2)

print(f"\nLoaded {len(jobs)} jobs\n")

for job in jobs:
    print(job)
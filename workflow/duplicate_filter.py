def job_key(job):
    """
    Creates a normalized key for duplicate detection.
    """

    return (
        job.title.lower().strip(),
        job.company.lower().strip(),
        job.location.lower().strip()
    )


def deduplicate_jobs(jobs):
    """
    Removes duplicate jobs from a list of Job objects.
    """

    seen = set()
    unique_jobs = []

    for job in jobs:
        key = job_key(job)

        if key in seen:
            continue

        seen.add(key)
        unique_jobs.append(job)

    return unique_jobs
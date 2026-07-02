PROCESSED_LABELS = [
    "Jobs High-Value",
    "Jobs Review",
    "Jobs Reject"
]


def already_processed(job):
    """
    Checks whether a job has already been processed.

    If the job already has one of the final decision labels,
    we should skip it so the pipeline is idempotent.
    """

    for label in job.labels:
        if label in PROCESSED_LABELS:
            return True

    return False
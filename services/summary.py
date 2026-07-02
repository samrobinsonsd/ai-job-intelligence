def print_summary(jobs):
    """
    Prints a summary of processed job results.

    Parameters:
        jobs (list[Job]): List of processed Job objects.
    """

    # Count total jobs processed.
    total = len(jobs)
        
    # Count jobs by decision label.
    high_value = 0
    review = 0
    reject = 0

    # Add all scores so we can calculate the average later.
    total_score = 0

    for job in jobs:
        total_score += job.score

        if job.decision == "Jobs High-Value":
            high_value += 1
        elif job.decision == "Jobs Review":
            review += 1
        elif job.decision == "Jobs Reject":
            reject += 1

    # Avoid division by zero if the list is empty.
    if total > 0:
        average_score = total_score / total
    else:
        average_score = 0

    print("")
    print("=" * 40)
    print("JOB FILTER SUMMARY")
    print("=" * 40)
    print(f"Processed:      {total}")
    print(f"High Value:     {high_value}")
    print(f"Review:         {review}")
    print(f"Reject:         {reject}")
    print(f"Average Score:  {average_score:.1f}")
    print("=" * 40)
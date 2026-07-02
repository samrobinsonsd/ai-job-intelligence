import json


def save_jobs(jobs, path):
    """
    Saves a list of Job objects to a JSON file.

    Parameters:
        jobs (list[Job]): List of processed Job objects.
        path (str): Output file path.
    """

    # Convert every Job object into a dictionary.
    #
    # JSON cannot directly save custom Python objects,
    # so each Job must be converted using job.to_dict().
    job_data = []

    for job in jobs:
        job_data.append(job.to_dict())

    # Open the output file in write mode.
    with open(path, "w") as file:

        # Save the list of dictionaries as formatted JSON.
        json.dump(job_data, file, indent=4)
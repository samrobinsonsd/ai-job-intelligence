import json

# Import our custom Job class.
# We'll convert raw JSON data into Job objects.
from jobs.job import Job


def load_jobs(path):
    """
    Loads a JSON file containing job listings and converts each
    dictionary into a Job object.
    
    """

    # Open the JSON file in read mode.
    with open(path, "r") as file:

        # Parse the JSON into Python objects.
        jobs_data = json.load(file)

    # Create an empty list that will hold our Job objects.
    jobs = []

    # Loop through every dictionary in the JSON file.
    for item in jobs_data:

        # Create a new Job object using values from the dictionary.
        #
        # item["title"] gets the value associated with the "title" key.
        jobs.append(Job.from_dict(item))
        
    # Return the completed list of Job objects to whoever called this function.
    return jobs
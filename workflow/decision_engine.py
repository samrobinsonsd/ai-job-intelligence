def decide(score):
    """
    Converts a numeric score into a Gmail label.
    """

    if score >= 80:
        return "Jobs High-Value"
    elif score >= 60:
        return "Jobs Review"
    else:
        return "Jobs Reject"
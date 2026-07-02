def score_job(job):
    score = 0
    reasons = []

    title = job.title.lower()
    location = job.location.lower()

    if "solutions engineer" in title or "solution engineer" in title:
        score += 35
        reasons.append("Strong title match")

    if "senior" in title:
        score += 10
        reasons.append("Seniority match")

    if location == "remote":
        score += 20
        reasons.append("Remote role")
    elif location == "unknown":
        reasons.append("Location unknown")

    if job.salary >= 140000:
        score += 30
        reasons.append("Strong salary match")
    elif job.salary == 0:
        reasons.append("Salary unknown")
    elif job.salary < 90000:
        score -= 20
        reasons.append("Salary below target")

    return score, reasons
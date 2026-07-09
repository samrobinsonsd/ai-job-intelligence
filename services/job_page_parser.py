from bs4 import BeautifulSoup


def parse_job_description(html):
    soup = BeautifulSoup(
        html,
        "lxml"
    )

    description = soup.select_one(
        "section.description"
    )

    if description is None:
        return ""

    return description.get_text(
        "\n",
        strip=True
    )


import re


def parse_salary_from_description(description):
    matches = re.findall(
        r"\$([0-9]{2,3}(?:,[0-9]{3})?|[0-9]{2,3})\s*[Kk]?",
        description
    )

    salaries = []

    for match in matches:
        value = int(match.replace(",", ""))

        if value < 1000:
            value *= 1000

        if value >= 50000:
            salaries.append(value)

    if not salaries:
        return 0

    return max(salaries)

import re


def parse_compensation_from_description(description):
    """
    Extracts compensation range and type from a job description.

    Returns:
        dict with min, max, type
    """

    text = description.lower()

    comp_type = ""

    if "ote" in text or "on-target earnings" in text:
        comp_type = "OTE"
    elif "base salary" in text:
        comp_type = "Base Salary"
    elif "salary" in text:
        comp_type = "Salary"
    elif "compensation" in text:
        comp_type = "Compensation"

    money_matches = re.findall(
        r"\$([0-9]{2,3}(?:,[0-9]{3})?|[0-9]{2,3})(?:\s*[kK])?",
        description
    )

    values = []

    for match in money_matches:
        value = int(match.replace(",", ""))

        if value < 1000:
            value *= 1000

        if value >= 50000:
            values.append(value)

    if not values:
        return {
            "min": 0,
            "max": 0,
            "type": comp_type
        }

    return {
        "min": min(values),
        "max": max(values),
        "type": comp_type
    }
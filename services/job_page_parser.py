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
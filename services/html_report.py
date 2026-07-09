from html import escape


def format_compensation(job):
    """
    Formats compensation information for display.
    """

    compensation_min = job.compensation_min
    compensation_max = job.compensation_max
    compensation_type = job.compensation_type

    if (
        not compensation_min
        and not compensation_max
    ):
        return "Unknown"

    if (
        compensation_min
        and compensation_max
        and compensation_min != compensation_max
    ):
        compensation = (
            f"${compensation_min:,.0f} - "
            f"${compensation_max:,.0f}"
        )

    elif compensation_max:
        compensation = (
            f"${compensation_max:,.0f}"
        )

    else:
        compensation = (
            f"${compensation_min:,.0f}"
        )

    if (
        compensation_type
        and compensation_type != "Unknown"
    ):
        return (
            f"{escape(compensation_type)} "
            f"{compensation}"
        )

    return compensation


def generate_html_report(
    jobs,
    path="output/job_report.html"
):
    """
    Creates an HTML report for scored jobs.
    """

    rows = ""

    for job in sorted(
        jobs,
        key=lambda j: j.score,
        reverse=True
    ):
        if job.decision == "Jobs High-Value":
            row_class = "high"

        elif job.decision == "Jobs Review":
            row_class = "review"

        else:
            row_class = "reject"

        reasons = "<br>".join(
            escape(reason)
            for reason in job.reasons
        )

        compensation = format_compensation(
            job
        )

        title = escape(job.title)
        company = escape(job.company)
        location = escape(job.location)
        decision = escape(
            job.decision or ""
        )

        if job.url:
            job_title = (
                f'<a href="{escape(job.url)}" '
                f'target="_blank" '
                f'rel="noopener noreferrer">'
                f'{title}</a>'
            )

        else:
            job_title = title

        rows += f"""
        <tr class="{row_class}">
            <td class="score">{job.score}</td>
            <td>{decision}</td>
            <td>{job_title}</td>
            <td>{company}</td>
            <td>{location}</td>
            <td class="compensation">{compensation}</td>
            <td>{reasons}</td>
        </tr>
        """

    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta
            name="viewport"
            content="width=device-width, initial-scale=1.0"
        >

        <title>AI Job Intelligence Report</title>

        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 30px;
                background: #f6f6f6;
                color: #222;
            }}

            h1 {{
                margin-bottom: 5px;
            }}

            .summary {{
                margin-bottom: 20px;
                color: #555;
            }}

            table {{
                width: 100%;
                border-collapse: collapse;
                background: white;
            }}

            th,
            td {{
                border: 1px solid #ddd;
                padding: 10px;
                vertical-align: top;
                text-align: left;
            }}

            th {{
                background: #222;
                color: white;
            }}

            a {{
                color: #0066cc;
                font-weight: 600;
                text-decoration: none;
            }}

            a:hover {{
                text-decoration: underline;
            }}

            .score {{
                font-weight: bold;
                text-align: center;
            }}

            .compensation {{
                white-space: nowrap;
            }}

            .high {{
                background: #e6f4ea;
            }}

            .review {{
                background: #fff8e1;
            }}

            .reject {{
                background: #fdecea;
            }}
        </style>
    </head>

    <body>
        <h1>AI Job Intelligence Report</h1>

        <p class="summary">
            Processed {len(jobs)} jobs.
        </p>

        <table>
            <thead>
                <tr>
                    <th>Score</th>
                    <th>Decision</th>
                    <th>Title</th>
                    <th>Company</th>
                    <th>Location</th>
                    <th>Compensation</th>
                    <th>Reasons</th>
                </tr>
            </thead>

            <tbody>
                {rows}
            </tbody>
        </table>
    </body>
    </html>
    """

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:
        file.write(html)
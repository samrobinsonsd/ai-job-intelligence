def generate_html_report(jobs, path="output/job_report.html"):
    """
    Creates a simple HTML report for scored jobs.
    """

    rows = ""

    for job in sorted(jobs, key=lambda j: j.score, reverse=True):
        if job.decision == "Jobs High-Value":
            row_class = "high"
        elif job.decision == "Jobs Review":
            row_class = "review"
        else:
            row_class = "reject"

        reasons = "<br>".join(job.reasons)

        rows += f"""
        <tr class="{row_class}">
            <td>{job.score}</td>
            <td>{job.decision}</td>
            <td>{job.title}</td>
            <td>{job.company}</td>
            <td>{job.location}</td>
            <td>${job.salary}</td>
            <td>{reasons}</td>
        </tr>
        """

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>AI Job Filter Report</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 30px;
                background: #f6f6f6;
            }}
            h1 {{
                margin-bottom: 5px;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                background: white;
            }}
            th, td {{
                border: 1px solid #ddd;
                padding: 10px;
                vertical-align: top;
            }}
            th {{
                background: #222;
                color: white;
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
        <h1>AI Job Filter Report</h1>
        <p>Processed {len(jobs)} jobs.</p>

        <table>
            <tr>
                <th>Score</th>
                <th>Decision</th>
                <th>Title</th>
                <th>Company</th>
                <th>Location</th>
                <th>Salary</th>
                <th>Reasons</th>
            </tr>
            {rows}
        </table>
    </body>
    </html>
    """

    with open(path, "w", encoding="utf-8") as file:
        file.write(html)
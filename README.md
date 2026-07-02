# AI Job Intelligence

An AI-powered job intelligence pipeline that automatically reads LinkedIn Job Alerts from Gmail, extracts job information from HTML emails, evaluates opportunities using OpenAI, and generates professional reports.

Instead of manually reviewing dozens of job alerts every day, the system automatically scores each opportunity based on technical alignment, seniority, company fit, remote preference, compensation (when available), and overall relevance.

---

## Features

- Gmail API integration
- OAuth2 authentication
- HTML email extraction
- BeautifulSoup HTML parsing
- LinkedIn Job Alert parsing
- Duplicate detection
- AI-powered job evaluation using OpenAI
- Structured JSON output
- Interactive HTML dashboard
- Modular Python architecture

---

# Example Workflow

```
                Gmail API
                    │
                    ▼
        LinkedIn Job Alert Emails
                    │
                    ▼
         Extract HTML Email Body
                    │
                    ▼
           BeautifulSoup Parser
                    │
                    ▼
              Build Job Objects
                    │
                    ▼
           Remove Duplicate Jobs
                    │
                    ▼
           OpenAI Job Evaluation
                    │
                    ▼
            Decision Engine
                    │
        ┌───────────┴───────────┐
        ▼                       ▼
   JSON Report            HTML Dashboard
```

---

# AI Evaluation

Each job is evaluated using an LLM against a candidate profile including:

- Senior Solutions Engineering
- Presales
- Customer Discovery
- Solution Architecture
- Technical Workshops
- APIs
- AI
- Cloud
- UCaaS
- CCaaS
- Microsoft Teams Voice

The model returns:

- Match Score (0-100)
- Executive Summary
- Decision
- Supporting Reasons

Example:

```json
{
    "score": 85,
    "summary": "Excellent senior remote Solutions Engineering opportunity with competitive compensation.",
    "reasons": [
        "Strong senior technical alignment.",
        "Remote role matches preferred work style.",
        "Competitive compensation.",
        "Likely customer-facing technical role.",
        "Industry alignment appears strong."
    ]
}
```

---

# Decision Categories

| Score | Decision |
|-------:|----------|
| 80-100 | Jobs High-Value |
| 60-79 | Jobs Review |
| 0-59 | Jobs Reject |

---

# Technologies Used

- Python 3.14
- OpenAI API
- Gmail API
- BeautifulSoup4
- OAuth2
- HTML
- JSON
- CSS

---

# Project Structure

```
AI-Job-Filter/

├── gmail/
│   ├── gmail_client.py
│   ├── gmail_loader.py
│   ├── body_extractor.py
│   ├── html_parser.py
│   └── parser.py
│
├── jobs/
│   └── job.py
│
├── prompts/
│   └── job_scoring.txt
│
├── scoring/
│   ├── llm_scorer.py
│   └── rule_scorer.py
│
├── services/
│   ├── loader.py
│   ├── writer.py
│   ├── summary.py
│   ├── prompt_loader.py
│   └── html_report.py
│
├── workflow/
│   ├── decision_engine.py
│   ├── duplicate_filter.py
│   └── label_filter.py
│
├── output/
│   ├── scored_jobs.json
│   └── job_report.html
│
├── main.py
├── requirements.txt
└── README.md
```

---

# Example Console Output

```
==================================================
         AI JOB INTELLIGENCE
 Gmail + OpenAI + BeautifulSoup
==================================================

[✓] Connected to Gmail

[✓] Loaded 48 jobs

[✓] Removed duplicates

[✓] AI evaluation complete

========================================
JOB FILTER SUMMARY
========================================

Processed:      39
High Value:      4
Review:          3
Reject:         32

Average Score:  71.4

========================================

Reports generated successfully.
```

---

# HTML Dashboard

The application generates a color-coded HTML report containing:

- AI Score
- Decision
- Job Title
- Company
- Location
- Salary
- Executive Summary
- AI Reasoning

This makes it easy to quickly identify the most promising opportunities without opening every job posting.

---

# Future Improvements

- Gmail label automation
- Automatic email archiving
- Resume matching
- Cover letter generation
- Multi-job board support
- Company enrichment
- LinkedIn API integration
- Scheduler for unattended execution

---

# Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-job-intelligence.git

cd ai-job-intelligence
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env`

```text
OPENAI_API_KEY=your_openai_api_key
```

Add your Gmail OAuth credentials

```
credentials.json
```

Run

```bash
python main.py
```

---

# Screenshots

## HTML Dashboard

*(Add screenshot here)*

## Console Output

*(Add screenshot here)*

---

# Why I Built This

I built this project to automate one of the most repetitive parts of a job search.

Instead of manually reviewing every LinkedIn Job Alert, the pipeline automatically extracts job data, evaluates opportunities using an LLM, and produces structured reports that prioritize the most relevant positions.
The project combines API integrations, prompt engineering, HTML parsing, structured data processing, and workflow automation into a practical end-to-end AI application.

---

# License

MIT License

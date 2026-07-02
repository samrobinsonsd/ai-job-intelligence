# AI Job Intelligence

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4.1-412991?logo=openai)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)

An AI-powered job intelligence pipeline that automatically reads
LinkedIn Job Alerts from Gmail, extracts structured job information from
HTML emails, evaluates opportunities using OpenAI, and generates
professional reports.

Instead of manually reviewing dozens of job alerts every day, AI Job
Intelligence prioritizes opportunities based on your own experience,
technical background, and career goals.

The scoring logic is prompt-driven, making it easy to adapt the
application for nearly any technical profession without modifying the
Python code.

## Features

-   Gmail API integration
-   OAuth2 authentication
-   HTML email extraction
-   BeautifulSoup HTML parsing
-   LinkedIn Job Alert parsing
-   Duplicate detection
-   Prompt-driven OpenAI evaluation
-   Structured JSON responses
-   Executive summaries
-   Color-coded HTML dashboard
-   Modular Python architecture
-   Easily customized for different careers

## Demo

1.  Authenticate with Gmail
2.  Read LinkedIn Job Alerts
3.  Parse HTML into job objects
4.  Remove duplicates
5.  Score each opportunity with OpenAI
6.  Categorize as High Value, Review, or Reject
7.  Generate HTML and JSON reports

## Customize for Your Career

Edit:

``` text
prompts/job_scoring.txt
```

Update: - Background - Preferred industries - Roles to avoid - Decision
thresholds

No Python changes are required. Changing the prompt changes the
behavior.

## Technologies

-   Python
-   OpenAI API
-   Gmail API
-   BeautifulSoup4
-   OAuth2
-   HTML/CSS
-   JSON

## Installation

``` bash
git clone https://github.com/samrobinsonsd/ai-job-intelligence.git
cd ai-job-intelligence
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

Create a `.env`:

``` text
OPENAI_API_KEY=your_openai_api_key
```

Place your Gmail OAuth `credentials.json` in the project root.

## Why I Built This

I built this project to automate one of the most repetitive parts of a
job search. It combines API integration, HTML parsing, prompt
engineering, structured data processing, and workflow automation into a
practical end-to-end AI application.

## Roadmap

-   Resume embeddings
-   Semantic job matching
-   RAG-powered company research
-   Company enrichment
-   Docker deployment
-   Multi-job board support
-   Historical analytics

## License

MIT License

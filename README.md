# Securacy-Project

A Python-based service that converts structured security threat data into Jira issues using the Jira Cloud REST API.  
Each threat in the input JSON is transformed into a separate Jira ticket with correct priority, description, and metadata so that engineering or product teams can remediate the issue efficiently.

---

## 📌 Problem Statement

Security assessments often produce structured threat data (threats, severity, CVSS ratings, mitigations).  
Manually converting these into Jira tickets is error-prone and time-consuming.

This project automates the process by:
- Accepting threat data in JSON format
- Creating one Jira issue per threat
- Applying severity-based prioritization
- Using secure authentication
- Returning a clear per-threat result

---
## Features

- One Jira issue created per threat
- Severity-based priority mapping
- CVSS rating and mitigations included in issue description
- Secure authentication using Jira API tokens
- Per-threat error handling
- Compatible with Jira Cloud REST API v3
-
---
## Project Setup

### Installation 
```json
git clone <repo-url>
cd threat-to-jira
python -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows
pip install -r requirements.txt
```

### How to get Environment Variables
Create a `.env` file in the project root:
```env
JIRA_BASE_URL: Your Jira Cloud URL
JIRA_EMAIL: Email linked to Jira account
JIRA_API_TOKEN: Generate from https://id.atlassian.com/manage-profile/security/api-tokens
JIRA_PROJECT_KEY: Found in Jira project settings or URL
```

### Running the Application
```json
python app.py
```
##### Sever at - http://127.0.0.1:5000
---
## API Usage
##### Sever at -  
```json
POST /convert
```
- Use the Threats JSON for the Sample Input
- Use Postman or thunderclient to send a post request to the server
---
## Assumptions
- Jira Cloud REST API v3 is used
- Jira project key is valid and accessible
- Issue type Bug exists in the project
- CVSS rating is included as descriptive text
- Duplicate detection is omitted due to Jira Cloud API restrictions
---
## Project Structure
Securacy-project/
├── app.py
├── jira_client.py
├── threat_processor.py
├── requirements.txt
├── sample_input.json
├── .env.example
└── README.md
---
## Requirements
- Python 3.9+
- Flask
- requests
- Jira Cloud REST API v3
- python-dotenv
---
## Example Threats.json
```json
{
  "threats": [
    {
      "id": "T-001",
      "title": "SQL Injection in login form",
      "category": "Injection",
      "description": "User input is not properly sanitized in the login form, allowing attackers to inject malicious SQL queries that could compromise the database.",
      "mitigations": [
        "Use parameterized queries to stop SQL injection",
        "Input validation of inputs",
        "Implement prepared statements",
        "Use ORM frameworks with built-in protection"
      ],
      "cvss_rating": 8.9,
      "severity": "High"
    },
    {
      "id": "T-002",
      "title": "Weak password policy",
      "category": "Authentication",
      "description": "Current password policy allows weak passwords that can be easily brute-forced or guessed by attackers.",
      "mitigations": [
        "Enforce minimum password length of 12 characters",
        "Require password complexity (uppercase, lowercase, numbers, symbols)",
        "Implement password strength meter",
        "Block common passwords using a blacklist"
      ],
      "cvss_rating": 6.5,
      "severity": "Medium"
    },
    {
      "id": "T-003",
      "title": "Missing rate limiting on API endpoints",
      "category": "Security Misconfiguration",
      "description": "API endpoints lack rate limiting, making them vulnerable to denial-of-service attacks and brute-force attempts.",
      "mitigations": [
        "Implement rate limiting per IP address",
        "Add request throttling for authenticated users",
        "Use API gateway with built-in rate limiting",
        "Monitor and alert on unusual traffic patterns"
      ],
      "cvss_rating": 7.2,
      "severity": "High"
    },
    {
      "id": "T-004",
      "title": "Unencrypted sensitive data in logs",
      "category": "Sensitive Data Exposure",
      "description": "Application logs contain sensitive information such as passwords, API keys, and personal data in plaintext.",
      "mitigations": [
        "Implement log sanitization to remove sensitive data",
        "Use structured logging with field-level filtering",
        "Encrypt log files at rest",
        "Implement log retention policies"
      ],
      "cvss_rating": 5.3,
      "severity": "Medium"
    },
    {
      "id": "T-005",
      "title": "Outdated third-party dependencies",
      "category": "Vulnerable Components",
      "description": "Multiple third-party libraries and dependencies have known security vulnerabilities that could be exploited.",
      "mitigations": [
        "Update all dependencies to latest secure versions",
        "Implement automated dependency scanning",
        "Set up vulnerability alerts and monitoring",
        "Establish regular dependency update schedule"
      ],
      "cvss_rating": 4.1,
      "severity": "Low"
    },
    {
      "id": "T-006",
      "title": "Cross-Site Scripting (XSS) vulnerability",
      "category": "Injection",
      "description": "User-generated content is not properly escaped, allowing attackers to inject malicious JavaScript that executes in other users' browsers.",
      "mitigations": [
        "Implement context-aware output encoding",
        "Use Content Security Policy (CSP) headers",
        "Sanitize HTML input using trusted libraries",
        "Enable XSS protection headers"
      ],
      "cvss_rating": 9.2,
      "severity": "Critical"
    }
  ]
}
```

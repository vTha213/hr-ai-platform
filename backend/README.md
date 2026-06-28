# 🤖 HR AI Automation Platform

> AI-powered Recruitment Platform built with **FastAPI**, **PostgreSQL**, **Groq LLM**, and **SQLAlchemy Async**.

This project automates the recruitment lifecycle from job creation to candidate screening using Artificial Intelligence.

The platform enables recruiters to create jobs, generate AI-assisted job descriptions, collect candidate applications, automatically screen resumes, analyze GitHub profiles, detect AI-generated resumes, manually review LinkedIn profiles, calculate weighted candidate scores, and generate social media hiring posts.

---

# 📖 Project Overview

Hiring the right candidate is a time-consuming process.

Recruiters usually need to:

- Create Job Description
- Publish Jobs
- Receive Applications
- Read hundreds of resumes
- Compare Resume with JD
- Check GitHub
- Check LinkedIn
- Rank Candidates
- Share Hiring Posts

This platform automates almost the entire workflow using AI while still allowing Human Approval wherever required.

---

# 🎯 Assignment Objective

The objective of this assignment is to build an AI-powered HR Recruitment Platform that demonstrates:

- Backend API Development
- Authentication
- AI Integration
- Resume Parsing
- Candidate Screening
- GitHub Analysis
- Dashboard Development
- Background Processing
- Secure File Upload
- Human-in-the-loop Decision Making

---

# ✅ Assignment Coverage

| Requirement | Status |
|------------|--------|
| JWT Authentication | ✅ |
| User Registration | ✅ |
| User Login | ✅ |
| Protected APIs | ✅ |
| Job CRUD | ✅ |
| AI Job Description Generator | ✅ |
| Human Approval Flow | ✅ |
| Public Candidate Application | ✅ |
| Resume Upload | ✅ |
| PDF Validation | ✅ |
| DOCX Validation | ✅ |
| Magic Byte Validation | ✅ |
| Resume Parser | ✅ |
| Background Screening | ✅ |
| Resume vs JD Matching | ✅ |
| GitHub REST API Integration | ✅ |
| AI GitHub Analysis | ✅ |
| AI Resume Detection | ✅ |
| LinkedIn Manual Review | ✅ |
| Weighted Candidate Ranking | ✅ |
| Dashboard | ✅ |
| Social Media Generator | ✅ |
| Retry Logic | ✅ |
| Timeout Handling | ✅ |
| Logging | ✅ |
| PostgreSQL | ✅ |
| Async SQLAlchemy | ✅ |
| Swagger Documentation | ✅ |

---

# 🚀 Key Features

## 🔐 Authentication

- JWT Authentication
- OAuth2 Password Flow
- Password Hashing using bcrypt
- Protected Endpoints
- Current User Endpoint

---

## 💼 Job Management

Recruiters can:

- Create Jobs
- Update Jobs
- Delete Jobs
- View Jobs
- Generate AI Job Descriptions
- Approve Job Description before publishing

---

## 👨‍💼 Candidate Portal

Candidates can:

- Apply for Jobs
- Upload Resume
- Submit GitHub Profile
- Submit LinkedIn Profile
- Give Processing Consent

---

## 📄 Resume Processing

Platform automatically:

- Stores Resume
- Validates File Type
- Validates File Size
- Validates Magic Bytes
- Extracts Resume Text
- Saves Parsed Resume

---

## 🤖 AI Resume Screening

Groq LLM compares:

Resume

↓

Job Description

Outputs:

- Skills Score
- Experience Score
- Education Score
- Overall Score
- Recommendation
- Strengths
- Weaknesses

---

## 💻 GitHub Analysis

System fetches candidate GitHub profile using GitHub REST API.

AI evaluates:

- Repository Quality
- Project Consistency
- Recent Activity
- Resume Consistency

Returns:

- GitHub Score
- GitHub Summary

---

## 🧠 AI Resume Detection

Platform estimates probability that a resume was AI generated.

Output:

- AI Generated Probability (%)

---

## 🔗 LinkedIn Review

Recruiters manually assign LinkedIn Score.

Reason:

LinkedIn API restrictions prevent public profile scraping.

Manual review ensures compliance with platform policies.

---

## 📊 Candidate Dashboard

Dashboard displays:

- Candidate Information
- Resume Score
- GitHub Score
- LinkedIn Score
- Final Weighted Score
- Recommendation
- Screening Status

---

## 📢 Social Media Assistant

Automatically generates:

- LinkedIn Hiring Post
- Twitter/X Post
- Facebook Post
- Instagram Caption
- Hiring Poster Prompt
- Suggested Hiring Groups

---

## ⚡ Background Processing

Resume screening runs asynchronously.

Workflow:

Application Submitted

↓

Response Returned Immediately

↓

Background Screening Starts

↓

Dashboard Updated Automatically

This ensures a fast user experience while AI processing continues in the background.

---

# 🛠 Technology Stack

## Backend

- Python 3.10
- FastAPI
- SQLAlchemy Async
- PostgreSQL
- Alembic
- Uvicorn

---

## Artificial Intelligence

- Groq API
- Llama 3.3 70B
- Prompt Engineering

---

## Authentication

- JWT
- OAuth2
- bcrypt

---

## Database

- PostgreSQL
- AsyncPG

---

## File Processing

- PDF
- DOCX
- Resume Parser

---

## Version Control

- Git
- GitHub

---

# 🏗 High Level Architecture

```text
                    +-----------------------+
                    |      Recruiter        |
                    +-----------+-----------+
                                |
                                |
                          FastAPI Backend
                                |
      -------------------------------------------------------
      |             |             |            |             |
 Authentication    Jobs      Candidates   Dashboard   Social Media
      |             |             |            |             |
      -------------------------------------------------------
                                |
                         Background Tasks
                                |
      -------------------------------------------------------
      |                    |                    |
 Resume Parser       Groq AI Screening     GitHub REST API
      |                    |                    |
      -------------------------------------------------------
                                |
                          PostgreSQL Database
```

---

# 📂 Project Structure

```text
backend/
│
├── app/
│   ├── api/
│   ├── core/
│   ├── db/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   ├── uploads/
│   └── main.py
│
├── migrations/
│
├── requirements.txt
├── README.md
├── .env
└── alembic.ini
```

---
# ⚙️ Installation Guide

## Prerequisites

Before running the project, make sure the following software is installed:

* Python 3.10+
* PostgreSQL 14+
* Git
* pip
* Virtual Environment

---

# Clone Repository

```bash
git clone https://github.com/your-username/hr-ai-platform.git
```

```bash
cd hr-ai-platform/backend
```

---

# Create Virtual Environment

### Windows

```bash
python -m venv .venv
```

Activate:

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Database Setup

Create PostgreSQL database.

Example:

```sql
CREATE DATABASE hr_ai;
```

Run database migrations (if using Alembic):

```bash
alembic upgrade head
```

---

# Start Server

```bash
uvicorn app.main:app --reload
```

Server:

```
http://127.0.0.1:8000
```

Swagger:

```
http://127.0.0.1:8000/docs
```

OpenAPI JSON:

```
http://127.0.0.1:8000/openapi.json
```

---

# 🔑 Environment Variables

Create a `.env` file inside the backend folder.

| Variable                    | Description                  |
| --------------------------- | ---------------------------- |
| DATABASE_URL                | PostgreSQL Async Connection  |
| SECRET_KEY                  | JWT Secret Key               |
| ALGORITHM                   | JWT Algorithm                |
| ACCESS_TOKEN_EXPIRE_MINUTES | JWT Expiry                   |
| GROQ_API_KEY                | Groq API Key                 |
| GROQ_MODEL                  | Llama Model Name             |
| GITHUB_TOKEN                | GitHub Personal Access Token |

Example:

```env
DATABASE_URL=postgresql+asyncpg://postgres:password@localhost/hr_ai

SECRET_KEY=change_this_secret_key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=60

GROQ_API_KEY=your_groq_api_key

GROQ_MODEL=llama-3.3-70b-versatile

GITHUB_TOKEN=your_github_token
```

---

# 📚 API Documentation

Swagger UI

```
http://127.0.0.1:8000/docs
```

Interactive API documentation is automatically generated using FastAPI.

---

# API Endpoints

## Authentication

| Method | Endpoint       | Description   |
| ------ | -------------- | ------------- |
| POST   | /auth/register | Register User |
| POST   | /auth/login    | Login         |
| GET    | /auth/me       | Current User  |

---

## Jobs

| Method | Endpoint   | Description  |
| ------ | ---------- | ------------ |
| POST   | /jobs      | Create Job   |
| GET    | /jobs      | Get All Jobs |
| GET    | /jobs/{id} | Get Job      |
| PUT    | /jobs/{id} | Update Job   |
| DELETE | /jobs/{id} | Delete Job   |

---

## AI Job Description

| Method | Endpoint            |
| ------ | ------------------- |
| POST   | /ai/job-description |

---

## Candidate

| Method | Endpoint        |
| ------ | --------------- |
| POST   | /apply/{job_id} |

---

## AI Screening

| Method | Endpoint                  |
| ------ | ------------------------- |
| POST   | /screening/{candidate_id} |

---

## Dashboard

| Method | Endpoint                            |
| ------ | ----------------------------------- |
| GET    | /dashboard/candidates               |
| GET    | /dashboard/candidate/{candidate_id} |
| PUT    | /dashboard/linkedin/{candidate_id}  |

---

## Social Media Assistant

| Method | Endpoint               |
| ------ | ---------------------- |
| POST   | /social-media/{job_id} |

---

# 🗄 Database Schema

The project uses PostgreSQL with SQLAlchemy Async ORM.

Main Tables:

```
Users
│
├── Jobs
│
├── Candidates
│
├── Resumes
│
└── Screenings
```

Entity Relationship:

```
User
 │
 └──────< Job

Job
 │
 └──────< Candidate

Candidate
 │
 ├────── Resume

Candidate
 │
 └────── Screening
```

---

# Database Tables

## users

Stores recruiter login information.

Fields:

* id
* email
* password
* role
* full_name

---

## jobs

Stores job information.

Fields:

* id
* title
* department
* location
* skills
* description
* approved

---

## resumes

Stores uploaded resume metadata.

Fields:

* id
* filename
* filepath
* resume_text
* created_at

---

## candidates

Stores candidate profile.

Fields:

* id
* job_id
* resume_id
* name
* email
* phone
* linkedin_url
* github_url
* consent_given

---

## screenings

Stores AI screening results.

Fields:

* overall_score
* skills_score
* experience_score
* education_score
* github_score
* linkedin_score
* final_score
* recommendation
* strengths
* weaknesses
* ai_generated_probability
* screening_status

---
# 🧠 AI Screening Workflow

The platform automates candidate evaluation using a multi-stage AI pipeline while keeping humans in control of the final hiring decision.

## Workflow

```text
Candidate Applies
        │
        ▼
Resume Upload
        │
        ▼
Resume Validation
        │
        ▼
Resume Parsing
        │
        ▼
Background Screening Starts
        │
        ├──────────────┐
        │              │
        ▼              ▼
Resume vs JD      GitHub Analysis
 Screening             │
        │              │
        └──────┬───────┘
               ▼
     AI Resume Detection
               │
               ▼
      Weighted Score Calculation
               │
               ▼
      HR Dashboard Updated
               │
               ▼
 Recruiter Reviews Candidate
```

---

# 📊 Candidate Scoring Strategy

The final candidate score is calculated using a weighted scoring approach.

| Component        | Weight |
| ---------------- | -----: |
| Resume Screening |    70% |
| GitHub Analysis  |    15% |
| LinkedIn Review  |    15% |

Formula:

```text
Final Score

=

(Resume Score × 0.70)

+

(GitHub Score × 0.15)

+

(LinkedIn Score × 0.15)
```

This approach prevents a single source from dominating the hiring decision and provides a balanced evaluation.

---

# 🤖 Resume AI Screening

The Resume Screening Service compares the uploaded resume against the selected Job Description.

Evaluation Criteria:

* Skills Match
* Experience Match
* Education Match

Generated Output:

* Skills Score
* Experience Score
* Education Score
* Overall Score
* Strengths
* Weaknesses
* Hiring Recommendation

Possible Recommendations:

* Highly Recommended
* Recommended
* Consider
* Not Recommended

---

# 💻 GitHub AI Analysis

The GitHub Analysis Service verifies whether the candidate's GitHub profile supports the skills claimed in the resume.

The service evaluates:

* Public repositories
* Programming languages
* Repository activity
* Recent commits
* Repository consistency
* Resume consistency

Generated Output:

* GitHub Score
* GitHub Summary

If no GitHub profile is provided or the profile is unavailable, the GitHub score is set to 0 and the system continues processing.

---

# 📝 AI Resume Detection

The platform estimates the probability that a resume was generated primarily by AI.

This feature does **not** reject candidates.

Instead, it provides recruiters with an additional signal during manual review.

Output:

* AI Generated Probability (%)

Example:

```text
67%
```

---

# 🔗 LinkedIn Review

Due to LinkedIn API restrictions, recruiter feedback is collected manually.

Recruiters assign a LinkedIn Score after reviewing:

* Professional experience
* Career progression
* Skills
* Recommendations
* Profile quality

This score contributes 15% of the final candidate score.

---

# ⚙️ Background Processing

AI screening is executed using FastAPI Background Tasks.

## Why Background Tasks?

Large Language Model inference can take several seconds.

Instead of making the candidate wait, the platform immediately returns:

```json
{
    "message":"Application Submitted",
    "screening_status":"Processing"
}
```

The AI screening continues asynchronously.

Once completed, the dashboard automatically reflects the updated screening results.

Benefits:

* Better User Experience
* Faster API Response
* Non-blocking Processing
* Improved Scalability

---

# 🔐 Authentication Flow

The application uses JWT Authentication.

Workflow:

```text
User Login
     │
     ▼
JWT Token Generated
     │
     ▼
Client Stores Token
     │
     ▼
Authorization Header

Bearer <token>

     │
     ▼
Protected API
     │
     ▼
Current User Validation
```

Protected APIs include:

* Jobs
* Dashboard
* AI Screening
* Social Media Generation

---

# 🛡 Security Features

The platform implements multiple security measures.

## Authentication

* JWT Authentication
* OAuth2 Password Flow
* Password Hashing (bcrypt)

---

## File Upload Security

Resume uploads are validated using:

* MIME Type Validation
* File Size Validation
* Magic Byte Validation
* Extension Validation

This prevents malicious or renamed files from being uploaded.

---

## Candidate Consent

Candidate consent is mandatory before processing resumes.

If consent is not provided, the application is rejected.

---

## Duplicate Candidate Handling

Duplicate candidates are detected using email.

Instead of creating duplicate records:

* Resume is replaced
* Candidate profile is updated
* AI screening is restarted

---

## Prompt Injection Protection

The application minimizes prompt injection risk by:

* Structured prompts
* Fixed prompt templates
* JSON-only output instructions
* Controlled input formatting

This improves response consistency and reduces unexpected model outputs.

---

# 🔄 Retry Logic

External AI APIs may temporarily fail.

To improve reliability, the platform implements:

* Automatic Retry
* Timeout Handling
* JSON Validation
* Graceful Fallback Responses
* Structured Logging

If the AI service fails repeatedly, the screening process returns safe default values instead of crashing.

---

# 🏛 Architecture Decisions

## Why FastAPI?

* High Performance
* Async Support
* Automatic Swagger Documentation
* Easy Dependency Injection

---

## Why PostgreSQL?

* ACID Compliance
* Strong Relational Support
* Excellent SQL Performance
* Production Ready

---

## Why SQLAlchemy Async?

* Non-blocking Database Operations
* Better Scalability
* Modern Async Architecture

---

## Why Groq?

Groq provides:

* Very Low Latency
* High Throughput
* Large Language Models
* Simple Python SDK

This makes it suitable for AI-powered recruitment workflows.

---

## Why Background Tasks Instead of Waiting?

Recruiters should not wait several seconds for AI processing.

Background execution provides:

* Immediate API Response
* Better User Experience
* Faster Candidate Submission

---

## Human-in-the-Loop Design

Artificial Intelligence assists recruiters but never makes the final hiring decision.

Human approval is required for:

* Job Description Approval
* LinkedIn Review
* Final Hiring Decision

This design ensures fairness, transparency, and recruiter control.

---
# 🚀 Deployment Guide

This project can be deployed on multiple cloud platforms.

## Backend Deployment Options

* Render
* Railway
* AWS EC2
* Azure App Service
* Google Cloud Run

---

## Database

Recommended Production Database:

* PostgreSQL

Recommended Providers:

* Railway PostgreSQL
* Render PostgreSQL
* Supabase PostgreSQL
* AWS RDS PostgreSQL

---

## Environment Variables

Configure the following variables before deployment.

```env
DATABASE_URL=

SECRET_KEY=

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=60

GROQ_API_KEY=

GROQ_MODEL=llama-3.3-70b-versatile

GITHUB_TOKEN=
```

---

## Production Startup Command

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

---

# 🧪 Testing

The application was tested using FastAPI Swagger UI.

## Tested Modules

### Authentication

* Register User
* Login
* JWT Authentication
* Protected Routes

Result:

✅ Passed

---

### Job Management

* Create Job
* Update Job
* Delete Job
* Get Job
* Get Jobs

Result:

✅ Passed

---

### Resume Upload

Test Cases

✔ Valid PDF

✔ Valid DOCX

✔ Invalid File Extension

✔ Invalid Magic Bytes

✔ File Size Validation

Result:

✅ Passed

---

### Candidate Application

Test Cases

✔ New Candidate

✔ Duplicate Candidate

✔ Resume Replacement

✔ Consent Validation

✔ Background Screening

Result:

✅ Passed

---

### AI Resume Screening

Test Cases

✔ Resume vs Job Description

✔ Recommendation

✔ Skills Score

✔ Experience Score

✔ Education Score

Result:

✅ Passed

---

### GitHub Analysis

Test Cases

✔ Public Repository Analysis

✔ Repository Consistency

✔ GitHub Score

✔ GitHub Summary

Result:

✅ Passed

---

### Dashboard

Test Cases

✔ Candidate List

✔ Candidate Details

✔ Final Score

✔ LinkedIn Review

Result:

✅ Passed

---

### Social Media Generator

Test Cases

✔ LinkedIn Post

✔ Twitter/X Post

✔ Facebook Post

✔ Instagram Caption

✔ Hiring Poster Prompt

Result:

✅ Passed

---

# 📷 Screenshots

The following screenshots can be added after deployment.

* Login Page
* Swagger Documentation
* Job Creation
* Candidate Application
* AI Screening Result
* Dashboard
* Social Media Generator

Example:

```text
docs/

├── login.png

├── swagger.png

├── dashboard.png

├── screening.png

├── social-media.png
```

---

# 📌 Assumptions

The following assumptions were made during implementation.

* Recruiters are authenticated users.
* Candidates apply through a public application endpoint.
* GitHub profile is optional.
* LinkedIn scoring is performed manually.
* AI recommendations assist recruiters but never replace human decisions.
* Only PDF and DOCX resumes are accepted.
* PostgreSQL is used as the primary database.

---

# ⚠ Known Limitations

Current limitations of the platform include:

* LinkedIn public profiles cannot be analyzed automatically due to platform restrictions.
* Social media posts are generated but not published automatically.
* Email notifications are not implemented.
* Interview scheduling is not implemented.
* Multi-language resume parsing is not supported.

---

# 🔮 Future Improvements

The following enhancements are planned for future versions.

## Infrastructure

* Docker
* Docker Compose
* Kubernetes
* CI/CD Pipeline

---

## AI Features

* Multi-language Resume Parsing
* Resume Keyword Highlighting
* Interview Question Generator
* Candidate Skill Gap Analysis
* AI Interview Assistant

---

## HR Features

* Email Notifications
* Interview Scheduling
* Calendar Integration
* Offer Letter Generator
* Employee Onboarding Workflow

---

## Analytics

* Recruitment Analytics Dashboard
* Hiring Trend Analysis
* Candidate Funnel Reports
* Recruiter Performance Dashboard

---

## Cloud

* AWS S3 Resume Storage
* AWS ECS Deployment
* Redis Queue
* Celery Workers

---

# 📖 API Documentation

Interactive API Documentation

```text
http://127.0.0.1:8000/docs
```

OpenAPI

```text
http://127.0.0.1:8000/openapi.json
```

---

# 🤝 Contributing

Contributions are welcome.

Steps:

1. Fork the repository

2. Create a new feature branch

3. Commit changes

4. Push to your branch

5. Open a Pull Request

---

# 📄 License

This project is intended for educational purposes and technical assessment.

---

# 👨‍💻 Author

**Vishwanath Thakur**

AI Engineer | Python Developer

### Skills

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy
* Generative AI
* LangChain
* LangGraph
* CrewAI
* Machine Learning
* Power BI

GitHub

```text
https://github.com/vTha213
```

LinkedIn

```text
https://www.linkedin.com/in/vishwanath-thakur
```

Email

```text
thakurvishwanath565@gmail.com
```

---

# ⭐ Project Summary

The HR AI Automation Platform demonstrates how Artificial Intelligence can streamline modern recruitment while preserving human oversight.

Key capabilities include:

* Secure Authentication
* AI-powered Resume Screening
* GitHub Analysis
* AI Resume Detection
* LinkedIn Manual Review
* Weighted Candidate Ranking
* Social Media Content Generation
* Background Processing
* PostgreSQL Integration
* FastAPI Async Architecture
* Production-ready Error Handling
* Retry Logic
* Logging
* Human-in-the-loop Decision Making

This project was designed as a production-inspired recruitment platform that emphasizes scalability, security, maintainability, and responsible AI usage.

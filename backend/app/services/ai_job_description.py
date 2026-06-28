from groq import Groq

from app.core.config import settings

client = Groq(
    api_key=settings.GROQ_API_KEY
)


def generate_job_description(
    title: str,
    experience: str,
    skills: str
):

    prompt = f"""
You are an HR Recruitment Expert.

Generate a professional Job Description.

Job Title:
{title}

Experience:
{experience}

Required Skills:
{skills}

Generate:

1. Job Summary

2. Responsibilities

3. Required Skills

4. Preferred Qualifications

5. Benefits

Professional HR format only.
"""

    response = client.chat.completions.create(
        model=settings.GROQ_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=1200
    )

    return response.choices[0].message.content


def screen_resume(
    resume_text: str,
    job_description: str
):

    prompt = f"""
You are an expert HR recruiter.

Compare the following Resume with the Job Description.

Resume:

{resume_text}

Job Description:

{job_description}

Provide:

1. Match Percentage

2. Strengths

3. Missing Skills

4. Weaknesses

5. Final Recommendation

Keep the response professional.
"""

    response = client.chat.completions.create(
        model=settings.GROQ_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
        max_tokens=1500
    )

    return response.choices[0].message.content
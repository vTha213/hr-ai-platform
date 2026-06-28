import json
import re

from groq import Groq

from app.core.config import settings

client = Groq(
    api_key=settings.GROQ_API_KEY
)


def generate_social_media_posts(
    job_title: str,
    job_description: str
):

    prompt = f"""
You are an HR Recruitment Marketing Expert.

Create social media content for the following job.

Job Title:
{job_title}

Job Description:
{job_description}

Return ONLY valid JSON.

{{
    "linkedin_post":"",
    "twitter_post":"",
    "facebook_post":"",
    "instagram_post":"",
    "suggested_groups":[
        "",
        "",
        ""
    ],
    "image_prompt":""
}}

Rules:

LinkedIn:
Professional tone.

Twitter:
Maximum 280 characters.

Facebook:
Friendly tone.

Instagram:
Include suitable hashtags.

Suggested Groups:
Return 3-5 relevant professional communities.

Image Prompt:
Generate one hiring poster prompt for an AI image generator.

Return ONLY JSON.
"""

    response = client.chat.completions.create(
        model=settings.GROQ_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.4,
        max_tokens=1200
    )

    content = response.choices[0].message.content.strip()

    content = re.sub(r"^```json", "", content)
    content = re.sub(r"```$", "", content)
    content = content.strip()

    return json.loads(content)
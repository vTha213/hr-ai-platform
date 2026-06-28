import json
import logging
import re
import time

from groq import (
    Groq,
    APIError,
    APITimeoutError,
    RateLimitError
)

from app.core.config import settings

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

client = Groq(
    api_key=settings.GROQ_API_KEY
)

MAX_RETRIES = 3
RETRY_DELAY = 2


def screen_candidate(
    resume_text: str,
    job_description: str
):

    prompt = f"""
You are a Senior HR Recruitment Specialist.

Compare the Resume with the Job Description.

Return scores between 0 and 100.

Scoring Criteria:

1. Skills Match
2. Experience Match
3. Education Match

Recommendation:

- Highly Recommended
- Recommended
- Consider
- Not Recommended

Return ONLY valid JSON.

Resume:

{resume_text}

Job Description:

{job_description}

Return exactly:

{{
    "skills_score":0,
    "experience_score":0,
    "education_score":0,
    "strengths":"",
    "weaknesses":"",
    "recommendation":""
}}
"""

    for attempt in range(1, MAX_RETRIES + 1):

        try:

            response = client.chat.completions.create(

                model=settings.GROQ_MODEL,

                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],

                temperature=0,

                max_tokens=700,

                timeout=30

            )

            content = response.choices[0].message.content.strip()

            content = re.sub(r"^```json", "", content)
            content = re.sub(r"```$", "", content)

            content = content.strip()

            logger.info(content)

            result = json.loads(content)

            result["skills_score"] = max(
                0,
                min(
                    100,
                    int(result["skills_score"])
                )
            )

            result["experience_score"] = max(
                0,
                min(
                    100,
                    int(result["experience_score"])
                )
            )

            result["education_score"] = max(
                0,
                min(
                    100,
                    int(result["education_score"])
                )
            )

            result["overall_score"] = int(

                (
                    result["skills_score"]
                    + result["experience_score"]
                    + result["education_score"]
                ) / 3

            )

            return result

        except (
            APITimeoutError,
            APIError,
            RateLimitError,
            json.JSONDecodeError
        ) as e:

            logger.warning(

                f"Groq Retry {attempt}/{MAX_RETRIES}: {e}"

            )

            if attempt == MAX_RETRIES:

                logger.error(

                    "Groq AI Screening Failed"

                )

                return {

                    "overall_score": 0,

                    "skills_score": 0,

                    "experience_score": 0,

                    "education_score": 0,

                    "strengths": "AI Screening Failed",

                    "weaknesses": str(e),

                    "recommendation": "Consider"

                }

            time.sleep(RETRY_DELAY)
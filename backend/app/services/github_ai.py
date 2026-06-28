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


def analyze_github(
    github_data: dict,
    resume_text: str
):

    if not github_data.get("applicable"):

        return {
            "github_score": 0,
            "github_summary": github_data.get(
                "message",
                "GitHub profile unavailable."
            )
        }

    prompt = f"""
You are an AI Technical Recruiter.

Compare the candidate's resume with the GitHub profile.

Resume:

{resume_text}

GitHub Data:

{json.dumps(github_data, indent=2)}

Evaluate:

1. Does the GitHub profile support the claimed skills?

2. Is the repository activity consistent?

3. Score GitHub consistency between 0 and 100.

Return ONLY valid JSON.

{{
    "github_score":0,
    "github_summary":""
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

                max_tokens=400,

                timeout=30

            )

            content = response.choices[0].message.content.strip()

            content = re.sub(r"^```json", "", content)
            content = re.sub(r"```$", "", content)
            content = content.strip()

            logger.info(content)

            result = json.loads(content)

            result["github_score"] = max(
                0,
                min(
                    100,
                    int(result["github_score"])
                )
            )

            return result

        except (
            APITimeoutError,
            APIError,
            RateLimitError,
            json.JSONDecodeError
        ) as e:

            logger.warning(

                f"GitHub AI Retry {attempt}/{MAX_RETRIES}: {e}"

            )

            if attempt == MAX_RETRIES:

                logger.error(
                    "GitHub AI Analysis Failed"
                )

                return {

                    "github_score": 0,

                    "github_summary":

                    "GitHub analysis failed after multiple retries."

                }

            time.sleep(RETRY_DELAY)
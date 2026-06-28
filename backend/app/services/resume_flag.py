import json
import re

from groq import Groq

from app.core.config import settings

client = Groq(
    api_key=settings.GROQ_API_KEY
)


def detect_ai_resume(
    resume_text: str
):

    prompt = f"""
You are an experienced HR Resume Reviewer.

Estimate the probability that this resume was AI-assisted.

IMPORTANT:

- Return a number between 0 and 100.
- This is ONLY a soft heuristic.
- Never use this score to reject a candidate.
- Do not always return 0.
- Use the resume writing style, repetition, wording and formatting to estimate the probability.

Return ONLY valid JSON.

Example:

{{
    "ai_generated_probability": 35
}}

Resume:

{resume_text}
"""

    response = client.chat.completions.create(
        model=settings.GROQ_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2,
        max_tokens=150
    )

    content = response.choices[0].message.content.strip()

    content = re.sub(r"^```json", "", content)
    content = re.sub(r"```$", "", content)
    content = content.strip()

    print(content)

    result = json.loads(content)

    probability = int(result.get("ai_generated_probability", 0))

    probability = max(
        0,
        min(
            100,
            probability
        )
    )

    return {
        "ai_generated_probability": probability
    }
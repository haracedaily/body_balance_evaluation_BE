import json

from openai import OpenAI

from app.core.config import settings
from app.ai.prompt_builder import build_prompt
from app.schemas.analysis import RoutineResponse

client = OpenAI(api_key=settings.OPENAI_API_KEY)


FALLBACK_RESPONSE = {
    "summary": "기본 자세 교정 루틴입니다.",
    "exercises": [
        {
            "name": "Chin Tuck",
            "sets": "3",
            "reps": "15"
        }
    ],
    "cautions": [
        "통증 발생 시 중단하세요"
    ]
}



def generate_routine(posture_result: dict):
    prompt = build_prompt(posture_result)

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3,
        )

        content = response.choices[0].message.content

        parsed = json.loads(content)

        validated = RoutineResponse(**parsed)

        return validated.model_dump()

    except Exception:
        return FALLBACK_RESPONSE
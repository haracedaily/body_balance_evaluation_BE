
def build_prompt(posture_result: dict):
    return f"""
You are a posture assistant.

Generate ONLY valid JSON.

Input:
{posture_result}

JSON format:
{{
  "summary": "",
  "exercises": [
    {{
      "name": "",
      "sets": "",
      "reps": ""
    }}
  ],
  "cautions": []
}}
"""
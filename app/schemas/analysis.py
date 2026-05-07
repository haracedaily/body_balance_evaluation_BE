from pydantic import BaseModel
from typing import List

class Exercise(BaseModel):
    name: str
    sets: str
    reps: str

class RoutineResponse(BaseModel):
    summary: str
    exercises: List[Exercise]
    cautions: List[str]

class AnalysisResponse(BaseModel):
    status: str
    posture_analysis: dict | None = None
    routine: RoutineResponse | None = None
    error_code: str | None = None
    message: str | None = None
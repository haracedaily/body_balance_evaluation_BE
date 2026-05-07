import os
import uuid

from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

from app.cv.pose_detector import detect_pose
from app.logic.validator import validate_landmarks
from app.logic.posture_analyzer import analyze_posture
from app.ai.llm_service import generate_routine

router = APIRouter(prefix="/analysis")

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/start")
async def start_analysis(
    front_image: UploadFile = File(...)
):
    task_id = str(uuid.uuid4())

    image_path = f"{UPLOAD_DIR}/{task_id}.jpg"

    with open(image_path, "wb") as f:
        f.write(await front_image.read())

    landmarks = detect_pose(image_path)

    if not validate_landmarks(landmarks):
        return {
            "status": "failed",
            "error_code": "INVALID_POSE",
            "message": "전신 사진을 업로드해주세요"
        }

    posture_result = analyze_posture(landmarks)

    routine = generate_routine(posture_result)

    return {
        "status": "completed",
        "posture_analysis": posture_result,
        "routine": routine
    }
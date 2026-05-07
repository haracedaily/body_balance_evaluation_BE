import cv2
import mediapipe as mp

mp_pose = mp.solutions.pose

pose = mp_pose.Pose(
    static_image_mode=True,
    min_detection_confidence=0.5,
)


def detect_pose(image_path: str):
    image = cv2.imread(image_path)

    if image is None:
        return None

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    results = pose.process(image_rgb)

    if not results.pose_landmarks:
        return None

    return results.pose_landmarks.landmark
import math


def calculate_angle(a, b):
    dx = a.x - b.x
    dy = a.y - b.y

    angle = math.degrees(math.atan2(dy, dx))

    return abs(angle)



def analyze_posture(landmarks):
    left_shoulder = landmarks[11]
    right_shoulder = landmarks[12]
    nose = landmarks[0]

    shoulder_diff = abs(left_shoulder.y - right_shoulder.y)

    neck_angle = calculate_angle(nose, left_shoulder)

    result = {}

    if neck_angle > 15:
        result["forward_head"] = {
            "severity": "moderate",
            "confidence": 0.82
        }

    if shoulder_diff > 0.03:
        result["shoulder_imbalance"] = {
            "severity": "mild",
            "confidence": 0.75
        }

    return result
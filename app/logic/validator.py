REQUIRED_INDEXES = [0, 11, 12, 23, 24]


def validate_landmarks(landmarks):
    if landmarks is None:
        return False

    for idx in REQUIRED_INDEXES:
        landmark = landmarks[idx]

        if landmark.visibility < 0.5:
            return False

    return True
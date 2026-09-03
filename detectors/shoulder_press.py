from core.base_exercise import BaseExercise

class ShoulderPressDetector(BaseExercise):
    UP_THRESHOLD = 50
    DOWN_THRESHOLD = 160
    MIN_VISIBILITY = 0.7
    ELBOW_DRIFT_TOLERANCE = 0.06
    SWING_THRESHOLD = 15

    LEFT_SHOULDER = 11
    LEFT_ELBOW = 13
    LEFT_WRIST = 15
    RIGHT_SHOULDER = 12
    RIGHT_ELBOW = 14
    RIGHT_WRIST = 16
    LEFT_HIP = 23
    RIGHT_HIP = 24

import os
import cv2
import threading
from streamlit_webrtc import VideoProcessorBase
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from detectors.squat import SquatDetector
from detectors.pushup import PushUpDetector
from detectors.biceps_curl import BicepsCurlDetector
from detectors.shoulder_press import ShoulderPressDetector
from detectors.lunges import LungesDetector
from services.config.workout_config import POSE_CONNECTIONS

class VideoProcessorClass(VideoProcessorBase):
  def __init__(self):
      self._lock = threading.Lock()
      self._latest_matrics = None
      self.exercise_type = "Squats"

      model_path = os.path.join(os.getcwd(), "ml_models", "pose_landmark_full_task")
      base_option = python.BaseOptions(model_path=model_path)

      options = vision.PoseLandmarkerOptions(
         base_option = base_option,
         running_mode = vision.RunningMode.VIDEO,
         min_pose_detection_confidence = 0.7,
         min_pose_prsence_confidence = 0.7,
         min_tracking_confidence = 0.7,
         output_segmentation_masks= False
      )

      self._landmarker = vision.PoseLandmarker.create_from_options(options)

      self._detectors = {
         "Squats": SquatDetector(),
         "Push-ups": PushUpDetector(),
         "Bicep Curls (Dumbbell)": BicepsCurlDetector(),
         "Shoulder Press": ShoulderPressDetector(),
         "Lunges": LungesDetector(),
      }

      self._frame_timestamps_ms = 0

  def set_latest_metrics(self, metrics):
     with self._lock:
        self._latest_matrics = metrics.copy()


  def get_latest_metrics(self):
     with self._lock:
        return None if self._latest_matrics is None else self._latest_matrics.copy()


  def set_exercise(self, exercise_type):
     with self._lock:
        self._exercise_type = exercise_type


  def get_exercise(self):
     with self._lock:
        return self._exercise_type
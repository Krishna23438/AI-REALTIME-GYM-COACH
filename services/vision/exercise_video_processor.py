import os
import threading
from streamlit_webrtc import VideoProcessorBase
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

class VideoProcessorClass(VideoProcessorBase):
  def __init__(self):
      self._lock = threading.Lock()
      self._latest_matrics = None
      self.exercise_type = "Squats"

      model_path = os.path.join(os.getcwd(), "ml_models", "pose_landmark_full_task")
      base_option = python.BaseOptions(model_path=model_path)
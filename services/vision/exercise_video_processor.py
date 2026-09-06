import threading
from streamlit_webrtc import VideoProcessorBase

class VideoProcessorClass(VideoProcessorBase):
  def __init__(self):
      self._lock = threading.Lock()
      self._latest_matrics = None
      self.exercise_type = "Squats"

      
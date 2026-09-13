import time 
import streamlit as st

class VoicePipeline:
  def __init__(self, llm, tts):
    self.llm = llm
    self.tts = tts
    self.last_spoken_at = 0

  def _find_form_issue(self, exercise, metrics):
    if "issue" in metrics:
      return metrics["issue"]

    

  def process_event(self, event, exercise, metrics):
    issue = self._find_form_issue(exercise, metrics)

    now = time.time()

    is_major_issue = event in ["workout_started", "set_completed", "workout_complete"]

    if not is_major_issue:
      if not issue:
        return None

      if now - self.last_spoken_at < 5:
        return None

    text = self.llm.give_feedback(event, issue)
    voice = self.tts.speak(text)

    self.last_spoken_at = now

    return voice, text
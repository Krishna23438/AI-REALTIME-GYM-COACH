import time 
import streamlit as st

class VoicePipeline:
  def __init__(self, llm, tts):
    self.llm = llm
    self.tts = tts
    self.last_spoken_at = 0

  def _find_form_issue(self, exercise, metrics):
    pass

  def process_event(self, event, exercise, metrics):
    issue = self._find_form_issue(exercise, metrics)

    now = time.time()
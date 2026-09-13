

class VoicePipeline:
  def __init__(self, llm, tts):
    self.llm = llm
    self.tts = tts
    self.last_spoken_at = 0

  
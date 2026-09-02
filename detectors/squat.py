from core.base_exercise import BaseExercise

class SquatDetector(BaseExercise):
   DOWN_THRESHOLD = 100   
   UP_THRESHOLD = 160     
   MIN_VISIBILITY = 0.7

   LEFT_HIP = 23
   LEFT_KNEE = 25
   LEFT_ANKLE = 27
   RIGHT_HIP = 24
   RIGHT_KNEE = 26
   RIGHT_ANKLE = 28
   LEFT_SHOULDER = 11
   RIGHT_SHOULDER = 12
   
   def __init__(self):
    super().__init__()

   def reset(self):
    self.reps = 0 
    self.stage = None

   def process(self, landmarks):
    left_knee_angle = self.calculate_angle(
      self.get_point(landmarks, self.LEFT_HIP),
      self.get_point(landmarks, self.LEFT_KNEE),
      self.get_point(landmarks, self.LEFT_ANKLE)
    )

    right_knee_angle = self.calculate_angle(
      
    )
from core.base_exercise import BaseExercise

class LungesDetector(BaseExercise):
      UP_THRESHOLD = 160
      DOWN_THRESHOLD = 100
      MIN_VISIBILITY = 0.7
      BALANCE_TOLERANCE = 0.10
  
      LEFT_SHOULDER = 11
      LEFT_ELBOW = 13
      LEFT_WRIST = 15
      RIGHT_SHOULDER = 12
      RIGHT_ELBOW = 14
      RIGHT_WRIST = 16
      LEFT_HIP = 23
      RIGHT_HIP = 24
      LEFT_ANKLE = 27
      RIGHT_ANKLE = 28
      LEFT_KNEE = 25
      RIGHT_KNEE = 26

      def __int__(self):
            super().__init__()

      def reset(self) -> None:
           self.reps = 0
           self.stage = None

      def process(self, landmarks) -> dict:
          left_knee_angle = self.calculate_angle(
               self.get_point(landmarks, self.LEFT_HIP),
               self.get_point(landmarks, self.LEFT_KNEE),
               self.get_point(landmarks, self.LEFT_ANKLE),
          )

          right_knee_angle = self.calculate_angle(
               self.get_point(landmarks, self.RIGHT_HIP),
               self.get_point(landmarks, self.RIGHT_KNEE),
               self.get_point(landmarks,self.RIGHT_ANKLE)
          )

          if left_knee_angle <= right_knee_angle:
               front_knee_angle = left_knee_angle
               front_hip_idx = self.LEFT_HIP
               front_knee_idx = self.LEFT_KNEE
               front_ankle_idx = self.LEFT_ANKLE
               shoulder_idx_for_torso = self.LEFT_SHOULDER
          else:
               front_knee_angle = right_knee_angle
               front_hip_idx = self.RIGHT_HIP
               front_knee_idx = self.RIGHT_KNEE
               shoulder_idx_for_torso = self.LEFT_SHOULDER
               front_ankle_idx = self.RIGHT_ANKLE

          key_landmarks_visible = landmarks[front_hip_idx].visibility
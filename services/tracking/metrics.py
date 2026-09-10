import streamlit as st

def sync_metrics_update(context):
  if not context or not hasattr(context, "state") or not context.state.playing:
     return

  processor = getattr(context, "video_processor", None)

  if not processor:
     return

  exercise = st.session_state.get("exercise_type")

  if not exercise:
     return

  

  

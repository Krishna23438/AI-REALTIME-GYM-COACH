import streamlit as st
from services.auth.login import render_login_wall
from services.state.session_default import initial_session_defaults
from services.config.workout_config import EXERCISE_OPTIONS

def main():
  st.set_page_config(
    page_icon="🏋️",
    page_title="AI Real-time GYM Coach",
    initial_sidebar_state="expanded",
    layout="centered",
  )

  if not render_login_wall():
    return

  initial_session_defaults()

  workout_started = st.session_state.get("workout_started",False)

  with st.sidebar:
    st.title("🏋️ Apna AI Coach")

    if st.session_state.username:
      st.caption(f"👤 Login as {st.session_state.username}")

    st.divider()

    st.subheader("Workout Plan")

    if not workout_started:
      st.selectbox("Exercise",options=EXERCISE_OPTIONS,key="plan_exercise")

      st.number_input("Sets",min_value=0, max_value=50,key="plan_sets",step=1)

      st.number_input("Reps per Set",min_value=0, max_value=50,key="plan_reps",step=1)

      st.markdown("")

      start_session_button = st.button("Start Session", width="stretch",key="start_session_button")

      if start_session_button:
        st.session_state["workout_started"] = True
        st.rerun()

    else:
      exercise = st.session_state.get("plan_exercise")
      sets = st.session_state.get("plan_sets")
      reps = st.session_state.get("plan_reps")

      st.info(f"**{exercise}** -- {sets} Sets / {reps} Reps")

      end_session_button = st.button("End Session", key="end_session_button",width="stretch")

      if end_session_button:
        st.session_state["workout_started"] = False
        st.rerun()

    if workout_started:
      st.divider()

      exercise = st.session_state.get("plan_exercise")
      total_reps = st.session_state.get("reps")
      current_set_reps = st.session_state.get("current_set_reps")
      reps_per_sec = st.session_state.get("reps_per_sec")
      sets_completed = st.session_state.get("sets_completed")
      target_sets = st.session_state.get("target_sets")
      
      st.subheader("Progress")

      st.metric("Total Reps",f"{total_reps}")
      st.metric("Current Set Reps",f"{current_set_reps} / {reps_per_sec}")
      st.metric("Sets completed",f"{sets_completed} / {target_sets}")




if __name__ == "__main__":
  main()
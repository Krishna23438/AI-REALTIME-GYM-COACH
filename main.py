import streamlit as st
from services.auth.login import render_login_wall
from services.state.session_default import initial_session_defaults

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

  with st.sidebar:
    st.title("🏋️ Apna AI Coach")

    if st.session_state.username:
      st.caption(f"👤 Login as {st.session_state.username}")

if __name__ == "__main__":
  main()
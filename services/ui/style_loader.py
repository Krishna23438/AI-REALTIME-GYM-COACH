import os
import streamlit as st
import base64

def load_css(file_path):
  if os.path.exists(file_path):
    with open(file_path) as f:
      st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def inject_local_font(font_path,  font_name):
  if not os.path.exists(font_path):
    return

  with open(font_path, "rb") as f:
    encoded = base64.b64decode(f.read()).decode()

  ext = os.path.splitext(font_path)[1].strip(".")
  fmt = {"otf": "opentype"}.get(ext, ext)
  
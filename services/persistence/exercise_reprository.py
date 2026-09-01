import sqlite3
import streamlit as st
import pathlib as Path

_DB_PATH = str(Path(__file__).parent.parent.parent / "data.db")

@st.cache_resource
def _get_connection():
  conn = sqlite3.connect(_DB_PATH,check_same_thread=False)
  conn.row_factory = sqlite3.Row
  return conn

def init_db():
  conn = _get_connection()


  with conn:
    conn.execute("""
  
    """)
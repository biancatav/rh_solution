
import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="RH Solution", layout="wide")
st.title("RH Solution — App Online")

BASE = Path(__file__).parent
CSV  = BASE / "artifacts" / "processed" / "artifact_test.csv"

st.write("Lendo arquivo:", str(CSV))

if not CSV.exists():
    st.error("Arquivo não encontrado!")
    st.stop()

df = pd.read_csv(CSV)
st.dataframe(df, use_container_width=True)

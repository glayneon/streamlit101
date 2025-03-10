import streamlit as st

if "slider" not in st.session_state:
    st.session_state["slider"] = 5

st.slider("Select a Number", 0, 10, key="slider")

st.write(st.session_state["slider"])

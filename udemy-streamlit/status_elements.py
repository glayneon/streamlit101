import streamlit as st
import time

# progress bar
st.header('st.progress')
st.caption('Display a progress bar')

def progress_bar():
    my_bar = st.progress(0)
    for pct_complete in range(0, 101, 10):
        time.sleep(0.2)
        pct_complete = min(pct_complete, 100)
        my_bar.progress(pct_complete)

# spinner
st.header('st.spinner', divider=True)
with st.spinner("Something is processing..."):
    progress_bar()

st.success('Done!')

st.subheader('st.info')
st.info('This is information message')

st.subheader('st.success')
st.success('This is success message')

st.subheader('st.warning')
st.warning('This is warning message')

st.subheader('This is error message')
st.error('This is error message', icon=':material/thumb_up:')

time.sleep(2)
st.balloons()
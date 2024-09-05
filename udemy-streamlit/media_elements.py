import streamlit as st

st.header('Display image using st.image')

st.image(
    './media/image.jpg', 
    caption='This is a sample image for city',
    width=800,
    )

# video
st.header('Display videos')

with open(
    './media/waterfalls.mp4',
    'rb'
    ) as video_file:
    video_bytes = video_file.read()
    st.video(video_bytes)

# let's play audio
st.header('Display audio')
with open(
    './media/audio.mp3', 'rb') as audio_file:
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/ogg')
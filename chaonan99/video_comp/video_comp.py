import streamlit as st
import streamlit.components.v1 as components

def video_component():
    return components.html(
        open("index.html").read(),
        width=320,
        height=240,
    )

st.title('Video Player with Timestamp')
timestamp = video_component()
if timestamp:
    st.write(f'Current Timestamp: {timestamp}')
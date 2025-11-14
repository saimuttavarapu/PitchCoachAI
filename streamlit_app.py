import streamlit as st
import requests
import os

st.set_page_config(page_title="Pitch Coach AI", layout="wide")
st.title("🎤 Pitch Coach AI")

# Backend URL from Render environment variable
backend_url = os.getenv("BACKEND_URL")

# File upload
video = st.file_uploader("Upload your pitch video", type=["mp4", "mov"])
slides = st.file_uploader("Upload your pitch deck (PDF)", type=["pdf"])

if st.button("Analyze") and video and slides:
    files = {
        "pitch_video": (video.name, video, video.type),
        "pitch_deck": (slides.name, slides, slides.type),
    }

    with st.spinner("Analyzing pitch..."):
        res = requests.post(f"{backend_url}/analyze", files=files)
        if res.status_code == 200:
            st.subheader("AI Analysis:")
            st.write(res.json()["analysis"])
        else:
            st.error("Failed to analyze pitch. Check backend.")

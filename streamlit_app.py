import streamlit as st
import requests

st.title("🎤 Pitch Coach AI")

video = st.file_uploader("Upload your pitch video", type=["mp4", "mov"])
slides = st.file_uploader("Upload your pitch deck (PDF)", type=["pdf"])

if st.button("Analyze") and video and slides:
    files = {
        "pitch_video": (video.name, video, video.type),
        "pitch_deck": (slides.name, slides, slides.type),
    }

    res = requests.post("http://localhost:8000/analyze", files=files)
    if res.status_code == 200:
        st.subheader("AI Analysis:")
        st.write(res.json()["analysis"])
    else:
        st.error("Failed to analyze pitch.")

import streamlit as st
import whisper
import tempfile

st.title("🎥 AttentionX - Content Repurposing Engine")

video_file = st.file_uploader("Upload a video", type=["mp4"])

if video_file is not None:
    st.video(video_file)

    # -------- SAVE VIDEO --------
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_video:
        temp_video.write(video_file.read())
        video_path = temp_video.name

    st.write("Transcribing...")

    # -------- TRANSCRIPTION --------
    model = whisper.load_model("base")
    result = model.transcribe(video_path)

    transcript = result["text"]

    st.subheader("📄 Transcript")
    st.write(transcript)

    # -------- HIGHLIGHT DETECTION --------
    st.subheader("✨ Highlights")

    sentences = transcript.split(".")

    keywords = ["important", "success", "mistake", "secret", "key", "improve", "critical"]

    scored_sentences = []

    for sentence in sentences:
        score = 0
        for word in keywords:
            if word in sentence.lower():
                score += 1

        score += len(sentence.split()) * 0.01
        scored_sentences.append((sentence.strip(), score))

    scored_sentences = sorted(scored_sentences, key=lambda x: x[1], reverse=True)

    top_highlights = scored_sentences[:3]

    for idx, (sentence, score) in enumerate(top_highlights, 1):
        if sentence:
            st.write(f"👉 Highlight {idx}: {sentence}")

    # -------- CLIP PLACEHOLDER --------
    st.subheader("🎬 Generated Clip")
    st.write("🚧 Clip generation feature coming soon... (can be implemented using MoviePy)")
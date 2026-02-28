import streamlit as st
import whisper
from fpdf import FPDF

st.title("🎓 Lecture Voice-to-Notes Generator")

audio_file = st.file_uploader("Upload Lecture Audio", type=["mp3", "wav"])

if audio_file is not None:

    with open("temp_audio.wav", "wb") as f:
        f.write(audio_file.read())

    st.info("Transcribing audio...")

    model = whisper.load_model("base")
    result = model.transcribe("temp_audio.wav")
    lecture_text = result["text"]

    st.subheader("📄 Transcription")
    st.write(lecture_text)

    # SIMPLE SUMMARY LOGIC (no transformers)
    st.info("Generating Summary...")

    sentences = lecture_text.split(".")
    summary_text = ". ".join(sentences[:3])  # take first 3 sentences

    st.subheader("📝 Summary")
    st.write(summary_text)

    # SIMPLE QUIZ GENERATOR
    st.info("Generating Quiz...")

    quiz_text = f"""
1. What is the main topic discussed in the lecture?
2. Explain one important concept mentioned.
3. Why is this topic important?
"""

    st.subheader("❓ Quiz Questions")
    st.write(quiz_text)

    if st.button("Download Summary as PDF"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, summary_text)
        pdf.output("Lecture_Notes.pdf")

        with open("Lecture_Notes.pdf", "rb") as file:
            st.download_button("Download PDF", file, file_name="Lecture_Notes.pdf")
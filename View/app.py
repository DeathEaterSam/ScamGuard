import sys
import os
import streamlit as st

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Controller.Controller import process_audio_file
from Controller.Controller import process_text_file




st.title('Scam Detection System')

# Prompt the user to select an input method
input_method = st.radio("Choose input method:", ("Audio File", "Text"))

if input_method == "Audio File":
    audio_file = st.file_uploader("Upload your audio file", type=['wav', 'mp3'])

    if audio_file is not None:
        with st.spinner('Processing...'):
            text, results = process_audio_file(audio_file)
            st.write("Transcribed Text:", text)
            st.write("Result:", results)

elif input_method == "Text":
    text_prompt = st.text_area("Enter your text prompt:")

    if st.button("Analyze Text"):
        with st.spinner('Processing...'):
            results = process_text_file(text_prompt)
            st.write("Result:", results)

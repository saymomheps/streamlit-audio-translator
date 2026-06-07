import streamlit as st
import os
import google.generativeai as genai
from gtts import gTTS

st.set_page_config(page_title="Audio Translator & TTS", layout="wide")

st.title("Audio Translator + Text-to-Speech")
st.markdown("Completely FREE using Google Gemini API and Google TTS")

with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("Gemini API Key", type="password", value="AQ.Ab8RN6LEa3T8tqMfzY9b9qTOBZT49hIlfJ6utmpnbfZqaRAPjQ")
    language = st.selectbox("Target Language", ["English", "Spanish", "French", "German", "Hindi", "Bengali", "Arabic", "Chinese", "Japanese"])
    tts_lang = st.selectbox("TTS Language", {"Bengali": "bn", "English": "en", "Hindi": "hi", "Spanish": "es", "French": "fr", "German": "de", "Arabic": "ar", "Chinese": "zh", "Japanese": "ja"})
    st.info("Completely FREE - No payment needed!")

if not api_key:
    st.warning("Please enter Gemini API Key")
else:
    try:
        genai.configure(api_key=api_key)
        tab1, tab2 = st.tabs(["Audio to Text", "Text to Audio"])
        
        with tab1:
            st.header("Audio Transcription and Translation")
            uploaded_file = st.file_uploader("Upload Audio", type=["mp3", "wav", "ogg", "m4a"])
            
            if uploaded_file:
                st.audio(uploaded_file)
                if st.button("Transcribe"):
                    with st.spinner("Processing..."):
                        try:
                            with open("temp.wav", "wb") as f:
                                f.write(uploaded_file.read())
                            audio_file = genai.upload_file("temp.wav")
                            model = genai.GenerativeModel("gemini-1.5-flash")
                            response = model.generate_content(["Transcribe this audio in English:", audio_file])
                            st.session_state.text = response.text
                            st.success("Done!")
                            os.remove("temp.wav")
                        except Exception as e:
                            st.error(str(e))
                
                if "text" in st.session_state:
                    st.text_area("Transcription", st.session_state.text, disabled=True)
                    if st.button("Translate"):
                        try:
                            model = genai.GenerativeModel("gemini-1.5-flash")
                            response = model.generate_content(f"Translate to {language}: {st.session_state.text}")
                            st.session_state.translation = response.text
                        except Exception as e:
                            st.error(str(e))
                    if "translation" in st.session_state:
                        st.text_area(f"Translation ({language})", st.session_state.translation, disabled=True)
        
        with tab2:
            st.header("Text to Speech")
            text = st.text_area("Enter text:", height=150)
            if text and st.button("Generate Audio"):
                with st.spinner("Generating..."):
                    try:
                        tts = gTTS(text=text, lang=tts_lang)
                        tts.save("audio.mp3")
                        with open("audio.mp3", "rb") as f:
                            st.audio(f.read(), format="audio/mp3")
                    except Exception as e:
                        st.error(str(e))
    except Exception as e:
        st.error(f"API Error: {str(e)}")

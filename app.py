import streamlit as st
import librosa
import soundfile as sf
import numpy as np
from openai import OpenAI
import io
import os
from pathlib import Path

st.set_page_config(page_title="Audio Translator & TTS", layout="wide")

st.title("🎵 অডিও ট্রান্সলেটর + টেক্স টু স্পিচ")
st.markdown("অডিও ফাইল আপলোড করুন এবং ট্রান্সলেট করুন, তারপর হাই কোয়ালিটি অডিও তৈরি করুন")

# সাইডবার কনফিগারেশন
with st.sidebar:
    st.header("⚙️ সেটিংস")
    api_key = st.text_input("OpenAI API Key", type="password")
    language = st.selectbox(
        "টার্গেট ভাষা",
        ["English", "Spanish", "French", "German", "Hindi", "Bengali"]
    )
    
    # TTS সেটিংস
    st.subheader("🎙️ অডিও জেনারেশন")
    voice_choice = st.selectbox(
        "ভয়েস সিলেক্ট করুন",
        ["alloy", "echo", "fable", "onyx", "nova", "shimmer"]
    )
    speed = st.slider("স্পিড", 0.25, 4.0, 1.0, 0.25)

# মেইন অ্যাপ্লিকেশন
if not api_key:
    st.warning("⚠️ OpenAI API Key দিন সাইডবারে")
    st.info("""
    ### 🔑 OpenAI API Key কোথায় পাবেন?
    
    1. **https://platform.openai.com/api-keys** এ যান
    2. OpenAI অ্যাকাউন্ট দিয়ে লগইন করুন (নেই থাকলে সাইন আপ করুন)
    3. **"Create new secret key"** বাটন ক্লিক করুন
    4. কী কপি করুন এবং এখানে পেস্ট করুন
    
    ⚠️ **গুরুত্বপূর্ণ:** এই কী কখনো কাউকে শেয়ার করবেন না!
    """)
else:
    client = OpenAI(api_key=api_key)
    
    tab1, tab2 = st.tabs(["📤 অডিও থেকে টেক্স", "✍️ টেক্স থেকে অডিও"])
    
    # Tab 1: Transcription & Translation
    with tab1:
        st.header("অডিও আপলোড এবং ট্রান্সলেট করুন")
        
        uploaded_file = st.file_uploader(
            "অডিও ফাইল আপলোড করুন",
            type=["mp3", "wav", "ogg", "m4a"],
            key="audio_uploader"
        )
        
        if uploaded_file is not None:
            st.audio(uploaded_file)
            
            col1, col2 = st.columns(2)
            
            with col1:
                if st.button("🔄 ট্রান্সক্রাইব করুন", key="transcribe_btn"):
                    with st.spinner("প্রসেস হচ্ছে..."):
                        try:
                            # অডিও ফাইল সংরক্ষণ
                            audio_bytes = uploaded_file.read()
                            temp_file = "temp_audio.wav"
                            with open(temp_file, "wb") as f:
                                f.write(audio_bytes)
                            
                            # Whisper API দিয়ে ট্রান্সক্রাইব করুন
                            with open(temp_file, "rb") as f:
                                transcript = client.audio.transcriptions.create(
                                    model="whisper-1",
                                    file=f,
                                    language="en"
                                )
                            
                            st.success("✅ ট্রান্সক্রিপশন সফল!")
                            st.session_state.original_text = transcript.text
                            
                            # টেম্পোরারি ফাইল ডিলিট করুন
                            if os.path.exists(temp_file):
                                os.remove(temp_file)
                        
                        except Exception as e:
                            st.error(f"❌ ত্রুটি: {str(e)}")
            
            # Display transcription
            if "original_text" in st.session_state:
                st.subheader("📝 অরিজিনাল টেক্স্ট")
                st.text_area("", value=st.session_state.original_text, height=100, disabled=True)
                
                if st.button("🌐 অনুবাদ করুন"):
                    with st.spinner("অনুবাদ প্রক্রিয়া চলছে..."):
                        try:
                            translation_prompt = f"Translate the following text to {language}:\n\n{st.session_state.original_text}"
                            
                            response = client.chat.completions.create(
                                model="gpt-3.5-turbo",
                                messages=[
                                    {"role": "system", "content": "You are a professional translator."},
                                    {"role": "user", "content": translation_prompt}
                                ]
                            )
                            
                            st.session_state.translated_text = response.choices[0].message.content
                            st.success("✅ অনুবাদ সফল!")
                        
                        except Exception as e:
                            st.error(f"❌ ত্রুটি: {str(e)}")
                
                # Display translation
                if "translated_text" in st.session_state:
                    st.subheader(f"🌐 অনুবাদ ({language})")
                    st.text_area("", value=st.session_state.translated_text, height=100, disabled=True, key="translated_display")
                    
                    st.download_button(
                        label="📥 টেক্স্ট ফাইল ডাউনলোড করুন",
                        data=f"Original:\n{st.session_state.original_text}\n\nTranslated:\n{st.session_state.translated_text}",
                        file_name="translation.txt",
                        mime="text/plain"
                    )
    
    # Tab 2: Text to Speech
    with tab2:
        st.header("টেক্স থেকে হাই কোয়ালিটি অডিও তৈরি করুন")
        
        text_input = st.text_area(
            "টেক্স এন্টার করুন:",
            height=150,
            placeholder="এখানে আপনার টেক্স লিখুন..."
        )
        
        if text_input:
            col1, col2 = st.columns(2)
            
            with col1:
                if st.button("🎙️ অডিও জেনারেট করুন (OpenAI TTS)", key="generate_tts"):
                    with st.spinner("অডিও জেনারেট হচ্ছে..."):
                        try:
                            # OpenAI TTS API ব্যবহার করুন
                            response = client.audio.speech.create(
                                model="tts-1-hd",  # High quality model
                                voice=voice_choice,
                                input=text_input,
                                speed=speed
                            )
                            
                            # অডিও সংরক্ষণ
                            audio_file = "generated_audio.mp3"
                            response.stream_to_file(audio_file)
                            
                            st.session_state.generated_audio = audio_file
                            st.success("✅ অডিও জেনারেশন সফল!")
                        
                        except Exception as e:
                            st.error(f"❌ ত্রুটি: {str(e)}")
            
            # Display generated audio
            if "generated_audio" in st.session_state and os.path.exists(st.session_state.generated_audio):
                st.subheader("🎵 জেনারেটেড অডিও")
                
                with open(st.session_state.generated_audio, "rb") as audio_file:
                    audio_bytes = audio_file.read()
                
                st.audio(audio_bytes, format="audio/mp3")
                
                st.download_button(
                    label="📥 অডিও ফাইল ডাউনলোড করুন",
                    data=audio_bytes,
                    file_name="generated_audio.mp3",
                    mime="audio/mp3"
                )

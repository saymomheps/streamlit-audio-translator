import streamlit as st
import librosa
import soundfile as sf
import numpy as np
from openai import OpenAI
import io
import os

st.set_page_config(page_title="Audio Translator", layout="wide")

st.title("🎵 অডিও ট্রান্সলেটর")
st.markdown("অডিও ফাইল আপলোড করুন এবং তা ট্রান্সলেট করুন")

# সাইডবার কনফিগারেশন
with st.sidebar:
    st.header("⚙️ সেটিংস")
    api_key = st.text_input("OpenAI API Key", type="password")
    language = st.selectbox(
        "টার্গেট ভাষা",
        ["English", "Spanish", "French", "German", "Hindi", "Bengali"]
    )

# মেইন অ্যাপ্লিকেশন
if not api_key:
    st.warning("⚠️ OpenAI API Key দিন সাইডবারে")
else:
    client = OpenAI(api_key=api_key)
    
    uploaded_file = st.file_uploader(
        "অডিও ফাইল আপলোড করুন",
        type=["mp3", "wav", "ogg", "m4a"]
    )
    
    if uploaded_file is not None:
        st.audio(uploaded_file)
        
        if st.button("🔄 ট্রান্সলেট করুন"):
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
                            file=f
                        )
                    
                    st.subheader("📝 ট্রান্সক্রিপ্ট")
                    st.write(transcript.text)
                    
                    # অনুবাদ করুন
                    translation_prompt = f"Translate the following text to {language}:\n\n{transcript.text}"
                    
                    response = client.chat.completions.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "system", "content": "You are a professional translator."},
                            {"role": "user", "content": translation_prompt}
                        ]
                    )
                    
                    translated_text = response.choices[0].message.content
                    
                    st.subheader(f"🌐 অনুবাদ ({language})")
                    st.write(translated_text)
                    
                    # ডাউনলোড বাটন
                    st.download_button(
                        label="📥 টেক্সট ডাউনলোড করুন",
                        data=f"Original:\n{transcript.text}\n\nTranslated:\n{translated_text}",
                        file_name="translation.txt",
                        mime="text/plain"
                    )
                    
                    # টেম্পোরারি ফাইল ডিলিট করুন
                    os.remove(temp_file)
                    
                except Exception as e:
                    st.error(f"❌ ত্রুটি: {str(e)}")

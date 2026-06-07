# 🎵 অডিও ট্রান্সলেটর

এটি একটি Streamlit অ্যাপ্লিকেশন যা অডিও ফাইলকে ট্রান্সক্রাইব এবং অনুবাদ করে।

## বৈশিষ্ট্য

✨ **মূল ফিচার:**
- অডিও ফাইল আপলোড করুন (MP3, WAV, OGG, M4A)
- OpenAI Whisper API দিয়ে ট্রান্সক্রিপশন
- GPT-3.5-turbo দিয়ে একাধিক ভাষায় অনুবাদ
- অনুবাদিত টেক্সট ডাউনলোড করুন

## ইনস্টলেশন

### প্রয়োজনীয় জিনিস
- Python 3.8+
- OpenAI API Key

### স্টেপ ১: রিপোজিটরি ক্লোন করুন

```bash
git clone https://github.com/saymomheps/streamlit-audio-translator.git
cd streamlit-audio-translator
```

### স্টেপ ২: Virtual Environment তৈরি করুন

```bash
python -m venv venv

# Windows এ:
venv\Scripts\activate

# macOS/Linux এ:
source venv/bin/activate
```

### স্টেপ ३: প্যাকেজ ইনস্টল করুন

```bash
pip install -r requirements.txt
```

### স্টেপ ४: অ্যাপ চালান

```bash
streamlit run app.py
```

ব্রাউজার স্বয়ংক্রিয়ভাবে খুলবে `http://localhost:8501`

## ব্যবহার করার নির্দেশনা

1. **API Key যোগ করুন:**
   - সাইডবারে আপনার OpenAI API Key পেস্ট করুন
   - [এখানে API Key পান](https://platform.openai.com/api-keys)

2. **অডিও ফাইল আপলোড করুন:**
   - MP3, WAV, OGG বা M4A ফাইল আপলোড করুন

3. **ট্রান্সলেট করুন:**
   - "ট্রান্সলেট করুন" বাটনে ক্লিক করুন
   - টার্গেট ভাষা নির্বাচন করুন

4. **ফলাফল দেখুন:**
   - অরিজিনাল ট্রান্সক্রিপ্ট দেখুন
   - অনুবাদিত টেক্সট দেখুন
   - প্রয়োজনে ডাউনলোড করুন

## সমর্থিত ভাষা

- English
- Spanish
- French
- German
- Hindi
- Bengali

## খরচ

- Whisper API: প্রতি মিনিট অডিও $0.006
- GPT-3.5-turbo: প্রতি 1K টোকেনে $0.0005

## লাইসেন্স

MIT License

## যোগাযোগ

প্রশ্ন বা সমস্যার জন্য Issue তৈরি করুন।

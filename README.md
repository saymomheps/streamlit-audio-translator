# 🎵 অডিও ট্রান্সলেটর + টেক্স টু স্পিচ (Gemini API সংস্করণ)

এটি একটি Streamlit অ্যাপ্লিকেশন যা **সম্পূর্ণ বিনামূল্যে** অডিও ফাইলকে টেক্সে রূপান্তরিত করে, অনুবাদ করে এবং টেক্সকে অডিওতে রূপান্তরিত করে।

## ✨ বৈশিষ্ট্য

⭐ **অডিও থেকে টেক্স:**
- Google Gemini API দিয়ে টেক্সে রূপান্তর
- একাধিক ভাষা সমর্থন

🌐 **অনুবাদ:**
- Google Gemini API দিয়ে একাধিক ভাষায় অনুবাদ
- উচ্চ মানের অনুবাদ

🎙️ **টেক্স থেকে অডিও:**
- Google Text-to-Speech - বিনামূল্যে
- ৯+ ভাষা সমর্থন
- উচ্চ মানের অডিও

## 🆓 সম্পূর্ণ বিনামূল্যে!

✅ Gemini API - বিনামূল্যে  
✅ Google TTS - বিনামূল্যে  
✅ কোনো পেমেন্ট কার্ড লাগবে না  

## প্রয়োজনীয় জিনিস

- Python 3.8+
- Google Gemini API Key (বিনামূল্যে)

## ইনস্টলেশন

### স্টেপ ১: রিপোজিটরি ক্লোন করুন

```bash
git clone https://github.com/saymomheps/streamlit-audio-translator.git
cd streamlit-audio-translator
```

### স্টেপ २: Virtual Environment তৈরি করুন

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

ব্রাউজারে খুলবে: `http://localhost:8501`

## 🔑 Google Gemini API Key পাওয়ার উপায়

### ১. Google AI Studio এ যান
- ব্রাউজারে যান: **https://aistudio.google.com/app/apikey**

### २. Google অ্যাকাউন্ট দিয়ে লগইন করুন
- কোনো Google অ্যাকাউন্ট থাকলে লগইন করুন
- নেই থাকলে ফ্রি অ্যাকাউন্ট তৈরি করুন

### ३. "Create API Key" ক্লিক করুন
- **"Create API Key in new project"** বা **"Create API Key"** সিলেক্ট করুন

### ४. কী কপি করুন
- নীল বোতাম "Copy" ক্লিক করুন
- কী আপনার ক্লিপবোর্ডে সংরক্ষিত হবে

### ५. অ্যাপে ব্যবহার করুন
- অ্যাপের সাইডবারে API Key পেস্ট করুন

⚠️ **গুরুত্বপূর্ণ সুরক্ষা টিপস:**
- এই কী কখনো গিটহাব বা অন্য জায়গায় শেয়ার করবেন না
- পরিবেশ ভেরিয়েবলে সংরক্ষণ করুন (.env ফাইলে)

## ব্যবহারের নির্দেশনা

### অডিও থেকে টেক্স এবং অনুবাদ:

1. **"📤 অডিও থেকে টেক্স" ট্যাবে যান**
2. **অডিও ফাইল আপলোড করুন** (MP3, WAV, OGG বা M4A)
3. **"🔄 ট্রান্সক্রাইব এবং অনুবাদ করুন" ক্লিক করুন**
4. **টার্গেট ভাষা নির্বাচন করুন**
5. **"🌐 অনুবাদ করুন" ক্লিক করুন**
6. **ফলাফল দেখুন এবং ডাউনলোড করুন**

### টেক্স থেকে অডিও:

1. **"✍️ টেক্স থেকে অডিও" ট্যাবে যান**
2. **টেক্স এন্টার করুন**
3. **সাইডবারে ভাষা নির্বাচন করুন**
4. **"🎙️ অডিও জেনারেট করুন" ক্লিক করুন**
5. **অডিও শুনুন এবং ডাউনলোড করুন**

## সমর্থিত ভাষা

অনুবাদের জন্য:
- English
- Spanish
- French
- German
- Hindi
- Bengali
- Arabic
- Chinese
- Japanese

Google TTS সব প্রধান ভাষায় সমর্থিত।

## ভাষা কোড (TTS এর জন্য)

- Bengali: `bn`
- English: `en`
- Hindi: `hi`
- Spanish: `es`
- French: `fr`
- German: `de`
- Arabic: `ar`
- Chinese: `zh`
- Japanese: `ja`

## লাইসেন্স

MIT License

## সাহায্য এবং সমর্থন

সমস্যা হলে:
1. API Key সঠিক কিনা চেক করুন
2. ইন্টারনেট সংযোগ চেক করুন
3. নতুন API Key তৈরি করুন: https://aistudio.google.com/app/apikey
4. Issue তৈরি করুন: https://github.com/saymomheps/streamlit-audio-translator/issues

## অবদান

Pull Request স্বাগত জানাই! 🎉

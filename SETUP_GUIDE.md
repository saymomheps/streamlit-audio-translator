# 🚀 Complete Setup Guide

## বাংলায় নির্দেশনা (Bengali Instructions)

এই গাইডটি আপনাকে স্টেপ বাই স্টেপ অ্যাপ্লিকেশন সেটআপ করতে সাহায্য করবে।

---

## Step 1: FFmpeg ইনস্টল করুন

### Windows

#### Option A: Chocolatey ব্যবহার করে (সহজ)
```bash
# প্রথমে Chocolatey ইনস্টল করুন (Admin Command Prompt এ)
@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "[System.Net.ServicePointManager]::SecurityProtocol = 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))" && set "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"

# তারপর FFmpeg ইনস্টল করুন
choco install ffmpeg
```

#### Option B: সরাসরি ডাউনলোড
1. https://ffmpeg.org/download.html এ যান
2. Windows build ডাউনলোড করুন
3. Extract করুন `C:\ffmpeg` এ
4. System PATH এ যোগ করুন

### macOS
```bash
# Homebrew ব্যবহার করে
brew install ffmpeg
```

### Linux (Ubuntu/Debian)
```bash
sudo apt-get update
sudo apt-get install ffmpeg
```

### Verify FFmpeg Installation
```bash
ffmpeg -version
```

---

## Step 2: Python Setup

### Python ইনস্টল করুন
1. https://www.python.org/downloads/ থেকে Python 3.8+ ডাউনলোড করুন
2. Install করার সময় **"Add Python to PATH"** চেক করুন
3. Verify করুন:
```bash
python --version
```

---

## Step 3: Repository Clone করুন

### Git ব্যবহার করে
```bash
git clone https://github.com/saymomheps/streamlit-audio-translator.git
cd streamlit-audio-translator
```

### অথবা ZIP ডাউনলোড করুন
1. GitHub এ যান
2. "Code" → "Download ZIP" ক্লিক করুন
3. Extract করুন এবং ফোল্ডারে প্রবেश করুন

---

## Step 4: Virtual Environment তৈরি করুন

### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

### macOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

**Verify:** Terminal এ `(venv)` দেখা যাওয়া উচিত

---

## Step 5: Dependencies ইনস্টল করুন

```bash
pip install -r requirements.txt
```

**Verify:**
```bash
pip list
```

সব প্যাকেজ দেখা যাওয়া উচিত:
- SpeechRecognition 3.16.1
- pydub 0.25.1
- gtts 2.5.4
- deep-translator 1.11.4
- streamlit 1.40.0

---

## Step 6: অ্যাপ চালান

```bash
streamlit run app.py
```

অটোমেটিক্যালি ব্রাউজার খুলবে: `http://localhost:8501`

---

## 🎯 Quick Start Command (সব একসাথে)

### Windows
```bash
python -m venv venv && venv\Scripts\activate && pip install -r requirements.txt && streamlit run app.py
```

### macOS/Linux
```bash
python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt && streamlit run app.py
```

---

## ✅ Troubleshooting

### Problem: "python command not found"
**Solution:** 
- Python সঠিকভাবে ইনস্টল করেছেন কি?
- System PATH এ Python যোগ আছে কি?
- Terminal restart করুন

### Problem: "FFmpeg not found"
**Solution:**
```bash
ffmpeg -version
```
যদি কাজ না করে:
- FFmpeg সঠিকভাবে ইনস্টল করুন
- System restart করুন
- PATH environment variable চেক করুন

### Problem: "Module not found"
**Solution:**
```bash
# Virtual environment activate করেছেন কি?
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

# আবার install করুন
pip install -r requirements.txt --force-reinstall
```

### Problem: "Port 8501 already in use"
**Solution:**
```bash
streamlit run app.py --server.port 8502
```

### Problem: "Could not understand audio"
**Solution:**
- স্পষ্ট অডিও ব্যবহার করুন
- কম শব্দ হওয়া উচিত
- স্পষ্টভাবে কথা বলুন

### Problem: "Network Error"
**Solution:**
- ইন্টারনেট কানেকশন চেক করুন
- Google APIs অ্যাক্সেসযোগ্য কি?
- কয়েক সেকেন্ড পর আবার চেষ্টা করুন

---

## 🔍 Advanced Configuration

### কাস্টম Port ব্যবহার করুন
```bash
streamlit run app.py --server.port 9000
```

### Remote Server এ চালান
```bash
streamlit run app.py --server.address 0.0.0.0
```

### Headless Mode (কোনো ব্রাউজার ছাড়া)
```bash
streamlit run app.py --logger.level=error --client.showErrorDetails=false
```

---

## 📊 Performance Optimization

### Large Audio Files এর জন্য
```python
# app.py এ modify করুন
recognizer.energy_threshold = 4000  # Default: 300
```

### Network Slow থাকলে
```python
# Timeout বাড়ান
recognizer.listen(source, timeout=10)
```

---

## 🌐 Deployment (Optional)

### Streamlit Cloud এ Deploy করুন
1. GitHub এ push করুন
2. https://share.streamlit.io এ যান
3. Repository connect করুন
4. app.py ফাইল নির্বাচন করুন

### Heroku এ Deploy করুন
1. Procfile তৈরি করুন:
```
web: streamlit run --server.port $PORT --server.address 0.0.0.0 app.py
```

2. Deploy করুন:
```bash
heroku create
git push heroku main
```

---

## 📚 Next Steps

1. অ্যাপ খুলুন: `http://localhost:8501`
2. একটি ইংরেজি অডিও ফাইল আপলোড করুন
3. "Start Translation" ক্লিক করুন
4. বাংলা অডিও ডাউনলোড করুন

---

## 🆘 সাহায্যের জন্য

- 📖 README.md পড়ুন
- 🔗 GitHub Issues চেক করুন
- 💬 Q&A ফোরাম ব্যবহার করুন

---

**Happy Translating! 🎉**

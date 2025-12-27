# 🎙️ Chatterbox TTS - Streamlit UI

A beautiful, user-friendly web interface for [Chatterbox TTS](https://github.com/resemble-ai/chatterbox) by Resemble AI - State-of-the-Art, open-source text-to-speech models.

## ✨ Features

- **Three Model Options**:
  - **Chatterbox-Turbo**: Fastest model with paralinguistic tags support ([laugh], [chuckle], [cough])
  - **Chatterbox-Multilingual**: Supports 23 languages
  - **Chatterbox**: English-only standard model

- **Long Text Support**: Process text of any length
- **Voice Cloning**: Upload a reference audio to clone any voice
- **Paralinguistic Tags**: Add natural emotions with tags (Turbo model)
- **23 Language Support**: Full multilingual capabilities
- **Audio Playback & Download**: Listen and download generated speech
- **Modern UI**: Clean, intuitive interface built with Streamlit

## 📋 Requirements

- Python 3.11 (recommended)
- CUDA-capable GPU (recommended for faster generation)
- Sufficient VRAM:
  - Turbo: ~2GB VRAM (most efficient)
  - Multilingual/Standard: ~4GB+ VRAM

## 🚀 Installation

1. **Clone or navigate to this directory**:
```bash
cd "c:/Users/ahmed/OneDrive - ashghal.gov.qa/CODING/Chatterbox TTS"
```

2. **Create a virtual environment** (recommended):
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# source venv/bin/activate  # On Linux/Mac
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

## 🎯 Usage

1. **Start the Streamlit app**:
```bash
streamlit run app.py
```

2. **Open your browser** to the URL shown (usually `http://localhost:8501`)

3. **Use the interface**:
   - Select your preferred model from the sidebar
   - Choose a language (if using Multilingual model)
   - Enter or paste your text
   - Optionally upload a reference audio for voice cloning
   - Click "Generate Speech"
   - Listen and download your generated audio!

## 🌍 Supported Languages

Arabic (ar) • Danish (da) • German (de) • Greek (el) • English (en) • Spanish (es) • Finnish (fi) • French (fr) • Hebrew (he) • Hindi (hi) • Italian (it) • Japanese (ja) • Korean (ko) • Malay (ms) • Dutch (nl) • Norwegian (no) • Polish (pl) • Portuguese (pt) • Russian (ru) • Swedish (sv) • Swahili (sw) • Turkish (tr) • Chinese (zh)

## 🎭 Paralinguistic Tags (Turbo Model)

Add natural emotion and realism to your speech:
- `[laugh]` - Natural laughter
- `[chuckle]` - Light chuckle
- `[cough]` - Cough sound

**Example**:
```
Hi there, Sarah here [chuckle], thanks for calling back!
```

## 🎤 Voice Cloning

1. Prepare a 10-second audio clip of the target voice
2. Upload it in the sidebar under "Voice Cloning"
3. Generate speech - the model will clone the voice!

**Supported formats**: WAV, MP3, FLAC

## 💡 Tips for Best Results

1. **Use Turbo model** for fastest generation and natural-sounding speech with emotions
2. **Provide clear reference audio** (10 seconds, minimal background noise) for best voice cloning
3. **Break very long text** into paragraphs for better control
4. **Use appropriate language** selection for multilingual model
5. **GPU recommended** for real-time generation

## 🔧 Troubleshooting

**Model downloads slow?**
- Models download automatically on first use (~350MB - 1GB each)
- Subsequent runs will be much faster

**Out of memory errors?**
- Try using Turbo model (most efficient)
- Close other GPU-intensive applications
- Use CPU mode (slower but works without GPU)

**Audio quality issues?**
- Use high-quality reference audio for voice cloning
- Ensure reference audio is clear with minimal background noise

## 📚 Resources

- [Chatterbox GitHub](https://github.com/resemble-ai/chatterbox)
- [Resemble AI](https://resemble.ai)
- [Streamlit Documentation](https://docs.streamlit.io)

## 📄 License

This UI wrapper is provided as-is. Chatterbox TTS follows its own license from Resemble AI.

---

Made with ❤️ using Streamlit and Chatterbox TTS

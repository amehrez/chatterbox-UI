# Alternative Streamlit setup instructions

## Quick Start (Without chatterbox-tts package)

If you encounter build issues, you can create a simplified demo app. Here are the steps:

### 1. Install basic requirements
```bash
pip install streamlit==1.28.0
conda install -y pytorch torchaudio -c pytorch
```

### 2. For chatterbox-tts installation issues

The package requires Microsoft Visual C++ 14.0 or greater on Windows.

**Option A: Install Build Tools**
Download and install from: https://visualstudio.microsoft.com/visual-cpp-build-tools/

**Option B: Try simplified install**
```bash
# Install dependencies one by one
pip install diffusers==0.29.0
pip install transformers==4.44.0
pip install soundfile librosa
pip install accelerate
pip install einops
pip install huggingface-hub
```

Then clone and try again:
```bash
cd "c:/Users/ahmed/OneDrive - ashghal.gov.qa/CODING/Chatterbox TTS/chatterbox"
pip install -e . --no-build-isolation
```

### 3. Run the app
```bash
streamlit run app.py
```

## Notes
- The app will download models on first use (~500MB - 1GB per model)
- GPU is highly recommended for good performance
- On CPU, generation will be much slower but still functional

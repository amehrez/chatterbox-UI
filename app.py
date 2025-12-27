import streamlit as st
import torch
import torchaudio as ta
import tempfile
import os
import gc
import numpy as np
from scipy.io import wavfile
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="Chatterbox TTS",
    page_icon="🎙️",
    layout="wide"
)

# Title and description
st.title("🎙️ Chatterbox TTS")
st.markdown("**State-of-the-Art Text-to-Speech by Resemble AI**")

# Sidebar configuration
st.sidebar.header("⚙️ Configuration")

# Model selection
model_type = st.sidebar.selectbox(
    "Select Model",
    ["Chatterbox-Turbo", "Chatterbox-Multilingual", "Chatterbox"],
    help="Turbo: Fastest, supports paralinguistic tags | Multilingual: 23 languages | Chatterbox: English only"
)

# Supported languages for multilingual model
SUPPORTED_LANGUAGES = {
    "Arabic": "ar",
    "Danish": "da",
    "German": "de",
    "Greek": "el",
    "English": "en",
    "Spanish": "es",
    "Finnish": "fi",
    "French": "fr",
    "Hebrew": "he",
    "Hindi": "hi",
    "Italian": "it",
    "Japanese": "ja",
    "Korean": "ko",
    "Malay": "ms",
    "Dutch": "nl",
    "Norwegian": "no",
    "Polish": "pl",
    "Portuguese": "pt",
    "Russian": "ru",
    "Swedish": "sv",
    "Swahili": "sw",
    "Turkish": "tr",
    "Chinese": "zh"
}

# Language selector (always visible, used when Multilingual model is selected)
st.sidebar.markdown("### 🌍 Language Settings")
language_name = st.sidebar.selectbox(
    "Select Language",
    list(SUPPORTED_LANGUAGES.keys()),
    index=4,  # Default to English
    help="Choose language for Multilingual model, or English for other models"
)
language = SUPPORTED_LANGUAGES[language_name]

if model_type == "Chatterbox-Multilingual":
    st.sidebar.success(f"Using: **{language_name}** ({language})")
else:
    st.sidebar.info(f"Language selection available with Multilingual model")

# Paralinguistic tags helper for Turbo model
if model_type == "Chatterbox-Turbo":
    st.sidebar.markdown("### 💬 Paralinguistic Tags")
    st.sidebar.markdown("""
    Available tags for Turbo model:
    - `[laugh]` - Laughter
    - `[chuckle]` - Light chuckle
    - `[cough]` - Coughing sound
    
    Insert these tags in your text to add natural emotion and realism.
    """)

# Device selection and memory info
device = "cuda" if torch.cuda.is_available() else "cpu"
st.sidebar.markdown("### 💻 System Info")
st.sidebar.info(f"🖥️ Device: **{device.upper()}**")

if device == "cuda":
    try:
        gpu_mem = torch.cuda.get_device_properties(0).total_memory / 1024**3
        st.sidebar.info(f"📊 GPU Memory: {gpu_mem:.1f} GB")
    except:
        pass
else:
    st.sidebar.warning("⚠️ Using CPU mode (slower)")

# Memory warning
st.sidebar.markdown("### ⚠️ Memory Tips")
st.sidebar.markdown("""
**If you get memory errors**:
1. **Use Turbo model** (most efficient)
2. **Increase Windows paging file**:
   - Settings → System → About
   → Advanced system settings
   → Performance Settings
   → Advanced → Virtual memory
   → Change → Set to 16GB+
3. **Close other applications**
4. **Restart Streamlit** after changes
""")

# Audio prompt options
st.sidebar.markdown("### 🎤 Voice Settings")
voice_option = st.sidebar.radio(
    "Voice Source",
    ["Included Speakers", "Upload Custom"],
    index=0,
    help="Select a saved speaker or upload a new file"
)

audio_prompt_path = None

if voice_option == "Included Speakers":
    # Ensure speakers directory exists
    speakers_dir = Path("speakers")
    speakers_dir.mkdir(exist_ok=True)
    
    # List files
    speaker_files = list(speakers_dir.glob("*.wav")) + list(speakers_dir.glob("*.mp3")) + list(speakers_dir.glob("*.flac"))
    
    if not speaker_files:
        st.sidebar.warning("No speakers found in 'speakers' folder.")
        st.sidebar.info("💡 Tip: Add .wav files to the 'speakers' folder to build your library!")
    else:
        selected_speaker = st.sidebar.selectbox(
            "Select Speaker",
            [f.name for f in speaker_files],
            format_func=lambda x: Path(x).stem
        )
        if selected_speaker:
            audio_prompt_path = str(speakers_dir / selected_speaker)
            st.sidebar.success(f"✅ Selected: {Path(selected_speaker).stem}")

else:  # Upload Custom
    st.sidebar.markdown("Upload a 10-second reference audio to clone a specific voice.")
    audio_file = st.sidebar.file_uploader(
        "Upload Audio Prompt",
        type=["wav", "mp3", "flac"],
        help="Recommended: 10-second clear speech sample"
    )

    # Save uploaded audio to temp file
    if audio_file is not None:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
            tmp_file.write(audio_file.read())
            audio_prompt_path = tmp_file.name
        st.sidebar.success("✅ Audio prompt uploaded!")

# Advanced settings
with st.sidebar.expander("🔧 Advanced Settings"):
    show_model_info = st.checkbox("Show model info on load", value=False)

# Main panel
st.markdown("---")

# Quick insert buttons for paralinguistic tags (Turbo only)
if model_type == "Chatterbox-Turbo":
    st.markdown("### 💬 Quick Insert Tags")
    col1, col2, col3 = st.columns(3)
    
    if 'text_content' not in st.session_state:
        st.session_state.text_content = ""
    
    with col1:
        if st.button("Insert [laugh]"):
            st.session_state.text_content += "[laugh] "
    with col2:
        if st.button("Insert [chuckle]"):
            st.session_state.text_content += "[chuckle] "
    with col3:
        if st.button("Insert [cough]"):
            st.session_state.text_content += "[cough] "

# Text input area
st.markdown("### 📝 Enter Text")
text = st.text_area(
    "Text to synthesize",
    value=st.session_state.get('text_content', ""),
    height=200,
    placeholder="Enter your text here... You can include paralinguistic tags like [laugh] or [chuckle] with Turbo model.",
    help="Enter the text you want to convert to speech. For long text, the model will process it all."
)

# Update session state
st.session_state.text_content = text

# Example texts
st.markdown("#### 📋 Example Texts")
example_col1, example_col2, example_col3 = st.columns(3)

with example_col1:
    if st.button("Example: Turbo with Tags"):
        st.session_state.text_content = "Hi there, Sarah here from MochaFone calling you back [chuckle], have you got one minute to chat about the billing issue?"
        st.rerun()

with example_col2:
    if st.button("Example: English"):
        st.session_state.text_content = "Ezreal and Jinx teamed up with Ahri, Yasuo, and Teemo to take down the enemy's Nexus in an epic late-game pentakill."
        st.rerun()

with example_col3:
    if st.button("Example: French"):
        st.session_state.text_content = "Bonjour, comment ça va? Ceci est le modèle de synthèse vocale multilingue Chatterbox, il prend en charge 23 langues."
        st.rerun()

st.markdown("---")

# Generate button
if st.button("🎵 Generate Speech", type="primary", use_container_width=True):
    if not text.strip():
        st.error("❌ Please enter some text to synthesize.")
    else:
        try:
            # Clear GPU memory before loading (if GPU available)
            if device == "cuda":
                torch.cuda.empty_cache()
                gc.collect()
            
            with st.spinner(f"Loading {model_type} model... This may take a moment on first run."):
                # Load model based on selection
                if model_type == "Chatterbox-Turbo":
                    from chatterbox.tts_turbo import ChatterboxTurboTTS
                    if 'turbo_model' not in st.session_state:
                        st.session_state.turbo_model = ChatterboxTurboTTS.from_pretrained(device=device)
                        if show_model_info:
                            st.info("✅ Turbo model loaded (350M parameters)")
                    model = st.session_state.turbo_model
                
                elif model_type == "Chatterbox-Multilingual":
                    from chatterbox.mtl_tts import ChatterboxMultilingualTTS
                    if 'multilingual_model' not in st.session_state:
                        st.session_state.multilingual_model = ChatterboxMultilingualTTS.from_pretrained(device=device)
                        if show_model_info:
                            st.info("✅ Multilingual model loaded")
                    model = st.session_state.multilingual_model
                
                else:  # Chatterbox
                    from chatterbox.tts import ChatterboxTTS
                    if 'standard_model' not in st.session_state:
                        st.session_state.standard_model = ChatterboxTTS.from_pretrained(device=device)
                        if show_model_info:
                            st.info("✅ Standard model loaded")
                    model = st.session_state.standard_model
            
            # Generate audio
            with st.spinner("🎵 Generating speech... Please wait."):
                if model_type == "Chatterbox-Multilingual":
                    if audio_prompt_path:
                        wav = model.generate(text, language_id=language, audio_prompt_path=audio_prompt_path)
                    else:
                        wav = model.generate(text, language_id=language)
                else:
                    if audio_prompt_path:
                        wav = model.generate(text, audio_prompt_path=audio_prompt_path)
                    else:
                        wav = model.generate(text)
                
                # Save to temp file using Scipy (avoids TorchCodec errors)
                output_path = tempfile.mktemp(suffix=".wav")
                
                # Convert to numpy and save
                # Ensure it's on CPU and simple array
                wav_cpu = wav.cpu().squeeze().numpy()
                
                # Convert to int16 PCM for best compatibility
                # Clip to prevent overflow
                wav_cpu = np.clip(wav_cpu, -1.0, 1.0)
                wav_int16 = (wav_cpu * 32767).astype(np.int16)
                
                wavfile.write(output_path, model.sr, wav_int16)
                
                # Clear memory after generation
                del wav
                del wav_cpu
                del wav_int16
                if device == "cuda":
                    torch.cuda.empty_cache()
                gc.collect()
                
                st.success("✅ Speech generated successfully!")
                
                # Display audio player
                st.markdown("### 🔊 Generated Audio")
                st.audio(output_path, format="audio/wav")
                
                # Download button
                with open(output_path, "rb") as f:
                    st.download_button(
                        label="⬇️ Download Audio",
                        data=f.read(),
                        file_name="chatterbox_output.wav",
                        mime="audio/wav",
                        use_container_width=True
                    )
                
                # Clean up temp file (but keep it for the session)
                st.session_state.last_output = output_path
                
        except Exception as e:
            error_msg = str(e)
            st.error(f"❌ Error generating speech: {error_msg}")
            
            # Provide specific help for common errors
            if "paging file" in error_msg.lower() or "1455" in error_msg:
                st.error("""
                **MEMORY ERROR: Windows paging file too small!**
                
                To fix this:
                1. Press Windows key, search "View advanced system settings"
                2. Click "Settings" under Performance
                3. Go to "Advanced" tab → "Virtual memory" → "Change"
                4. Uncheck "Automatically manage paging file size"
                5. Select your C: drive
                6. Choose "Custom size"
                7. Set Initial: 16000 MB, Maximum: 32000 MB
                8. Click "Set" → "OK" → Restart computer
                
                **OR** try using Turbo model (most memory efficient)
                """)
            elif "out of memory" in error_msg.lower() or "oom" in error_msg.lower():
                st.error("""
                **Out of memory!**
                
                Try these solutions:
                1. Use **Chatterbox-Turbo** model (most efficient)
                2. Close other applications
                3. Restart Streamlit
                4. If using GPU: Reduce batch size or use CPU
                """)
            else:
                st.error("Please make sure you have the required dependencies installed and sufficient VRAM/RAM.")
            
            # Clear memory on error
            if device == "cuda":
                torch.cuda.empty_cache()
            gc.collect()

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>Powered by <a href='https://github.com/resemble-ai/chatterbox' target='_blank'>Chatterbox TTS</a> by Resemble AI</p>
    <p>Made with ❤️ using Streamlit</p>
</div>
""", unsafe_allow_html=True)

# Cleanup function for temp files
def cleanup_temp_files():
    if audio_prompt_path and os.path.exists(audio_prompt_path):
        try:
            os.unlink(audio_prompt_path)
        except:
            pass

# Register cleanup on session end
import atexit
atexit.register(cleanup_temp_files)

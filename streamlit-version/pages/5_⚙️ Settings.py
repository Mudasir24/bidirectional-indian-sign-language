import streamlit as st
import pyttsx3

# Set dark theme
st.set_page_config(page_title="Settings", page_icon="⚙️", layout="centered")

st.title("Settings")
st.header("Adjust Voice and Speech Options")

# Initialize TTS engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')

# Check if language information is available, otherwise show only the voice name
voice_options = []
for voice in voices:
    language_info = f" ({voice.languages[0]})" if hasattr(voice, 'languages') and voice.languages else ""
    voice_options.append(f"{voice.name}{language_info}")

# Select voice
selected_voice = st.selectbox("Choose a Voice:", voice_options)

# Set voice in session state
voice_index = voice_options.index(selected_voice)
st.session_state.voice_id = voices[voice_index].id

# Adjust rate
rate = st.slider("Speech Rate:", min_value=100, max_value=300, value=150)
st.session_state.rate = rate

# Adjust volume
volume = st.slider("Volume:", min_value=0.0, max_value=1.0, value=1.0)
st.session_state.volume = volume

st.success("Settings updated! Go back to the main page to test.")

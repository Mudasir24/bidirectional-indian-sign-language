import streamlit as st

# Set dark theme
st.set_page_config(page_title="Bidirectional Sign Language Communication System", page_icon="🖐️", layout="wide", initial_sidebar_state="expanded")

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            background-color: #121212;
            color: white;
        }
        .title {
            font-size: 36px;
            font-weight: bold;
            text-align: center;
        }
        .subtitle {
            font-size: 22px;
            text-align: center;
        }
        .section {
            padding: 20px;
            border-radius: 10px;
            background-color: #1E1E1E;
            margin-bottom: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Homepage Content

st.markdown("<h1 class='title'>Bidirectional Sign Language Communication System</h1>", unsafe_allow_html=True)
st.markdown("<h5 class='subtitle'>Breaking Barriers Between Sign Language Users and Non-Signers</h5><br>", unsafe_allow_html=True)

st.write(
    """
    Welcome to the Bidirectional Sign Language Communication System—an innovative application designed to facilitate seamless, real-time communication between individuals who use sign language and those who rely on spoken or written language. Our system leverages advanced technologies to provide accurate and efficient translations, promoting inclusivity and understanding.
    """
)

# # Placeholder for logo/image
# st.image("C:\\Users\\Mohammed Mudasir\\OneDrive\\Desktop\\Mini_Project\\Streamlit\\assets\\logo\\ISL.jpg", use_container_width=True)  

# Introduction Section
st.markdown("""
            <div class='section'><h3> Brief Overview</h3><p>The Bidirectional Sign Language Communication System is an innovative application designed to bridge the communication gap between individuals who use sign language and those who rely on spoken or written language. By leveraging advanced technologies such as computer vision, machine learning, and natural language processing, the system facilitates seamless, real-time translation in both directions: from sign language to speech/text and vice versa.<br>
            <br>In the <b>Sign-to-Speech/Text</b> mode, the system captures hand gestures using a camera, processes these inputs to recognize specific signs, and then converts them into corresponding spoken words or text. Conversely, in the <b>Speech/Text-to-Sign</b> mode, the application takes spoken or written language as input and translates it into sign language, displaying the appropriate gestures visually. This bidirectional functionality ensures effective communication, promoting inclusivity and understanding between sign language users and non-signers.<br>
            <br> The application is designed with user-friendliness in mind, featuring an intuitive interface that allows users to select their preferred mode of communication easily. Its real-time processing capabilities ensure that conversations flow naturally, without significant delays. By providing a tool that accommodates both sign language and spoken/written language, the system aims to foster more inclusive interactions across diverse communication preferences.
            </p></div>
            """, unsafe_allow_html=True)

# How It Works
st.markdown("<div class='section'><h3>⚙️ How It Works</h3><ul><li>Signers can gesture, and the system will translate them into text and speech.</li><li>Non-signers can speak or enter text, and the system will generate the corresponding sign visuals.</li></ul></div>", unsafe_allow_html=True)

# How to Use
st.markdown("<div class='section'><h3>📌 How to Use</h3><ol><li>Select <b>Sign Alphabet Recognition</b> to translate sign language alphabets to speech.</li><li>Select <b>Sign Number Recognition</b> to translate sign language numbers to speech.</li><li>Select <b>Speech-to-Sign Translation</b> to convert speech into signs.</li><li>Select <b>Text-to-Sign Translation</b> to convert speech into signs.</li></ol></div>", unsafe_allow_html=True)

# Model & Technology
st.markdown("<div class='section'><h3>🧠 Model & Technology</h3><p>This system employs machine learning models that utilize <b>hand landmarks</b> for recognizing sign language gestures. It incorporates a <b>Multi-layer Perceptron (MLP) Classifier</b>, enabling accurate interpretation of both sign alphabets and numbers. The system facilitates <b>real-time translation</b> of sign language into speech and text, while also converting speech and text into corresponding sign gestures. By employing <b>deep learning</b> techniques and advanced classification methods, this application aims to enhance communication accessibility for the deaf and hard of hearing, bridging the gap in everyday</p></div>", unsafe_allow_html=True)

# Contact & Credits
st.markdown("<div class='section'><h3>Credits</h3><p> <h5>Team Name: <b>TECH MAVERICKS</b></h5> <h5>Team Members</h5><ul><b><li>Mohammed Mudasir Ahmed</li><li>Ozair Ali</li> <li>Syed Ibrahim Ali</li></b></ul><br> </p></div>", unsafe_allow_html=True)

import streamlit as st
import os

st.set_page_config(page_title="Text to Sign Language", page_icon="📝", layout="wide")

# Add the "Text to Sign Language Conversion" page
st.markdown("""
    <h1 style="text-align: center; color: white;">Text to Sign Language Conversion (Single Alphabet/Digit)</h1>
    <h6 style="text-align: center; color: white;">
        This feature converts a single alphabet or digit entered by the user into its corresponding Indian Sign Language (ISL) gesture representation.
    </h6>
    """, unsafe_allow_html=True)

text = st.text_input('Enter text here:', '')
text = text.lower()

def load_image(file_name):
    
    folder_path = 'D:\\Mini_project\\Streamlit\\assets\\images\\'

    image = os.path.join(folder_path, file_name)
    if os.path.exists(image):
        return image
    else:
        return None 

if st.button('Generate Image'):
    if text == '':
        st.write('Please enter some text.')
    elif len(text.split()) > 1:
        st.write('Please enter only one letter.')

    elif text.isalpha() == False and text.isdigit() == False:
        st.write('Please enter only alphabets.')

    else:
        st.write('Generating image...')

        # Load the image
        image = load_image(text + '.jpg')
        if image is None:
            st.write('Image not found. Please try again.')
        else:
            st.image(image, caption='Generated Image', width=300)


st.markdown("""
    <h2 style="color: white;">How It Works</h2>
    <p style="color: white;">
        When you input a single letter (A-Z) or digit (0-9) into the text box, the system automatically displays the corresponding sign language gesture for that character. You can visualize the gesture and learn the ASL representation for each character in real time.
    </p>
    <h2 style="color: white;">How to Use</h2>
    <ul style="color: white;">
        <li>Type a single letter (A-Z) or digit (0-9) into the input field.</li>
        <li>Click the 'Convert' button to see the corresponding sign language gesture for the character.</li>
        <li>The gesture image for the alphabet or digit will appear below the input field, helping you understand the sign language symbol.</li>
    </ul>
    <h2 style="color: white;">Important Notes</h2>
    <p style="color: white;">
        - Only single alphabets or digits are supported at a time.
        <br>
        - Ensure the input is a valid letter or digit. Special characters or numbers outside the range (A-Z, 0-9) will not be processed.
    </p>
    <h2 style="color: white;">Application Scenarios</h2>
    <p style="color: white;">
        This tool is especially useful for learning the fundamentals of American Sign Language, enabling individuals to start by understanding how to sign basic characters. It can also be used in educational settings for teaching young students sign language in a fun and engaging way.
    </p>
""", unsafe_allow_html=True)

     




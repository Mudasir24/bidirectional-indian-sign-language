from flask import Flask, jsonify, request
import cv2
import numpy as np
import pickle
import mediapipe as mp
import base64
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

# Load models and labels
model_42 = pickle.load(open('mlp_model_1.p', 'rb'))['model']
model_84 = pickle.load(open('mlp_model_2.p', 'rb'))['model']
labels_dict_42 = {0: 'C', 1: 'I', 2: 'L', 3: 'O', 4: 'U', 5: 'V'}
labels_dict_84 = {0: 'A', 1: 'B', 2: 'D', 3: 'E', 4: 'F', 5: 'G', 6: 'H', 7: 'J', 8: 'K', 9: 'M', 10: 'N', 11: 'P', 12: 'Q', 13: 'R', 14: 'S', 15: 'T', 16: 'W', 17: 'X', 18: 'Y', 19: 'Z'}

# Load the math model
math_model = pickle.load(open('mlp_model_num.p', 'rb'))['model']
math_labels_dict = {0: '1', 1: '2', 2: '3', 3: '4', 4: '5', 5: '6', 6: '7', 7: '8', 8: '9', 9: '0'}

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
hands = mp_hands.Hands(static_image_mode=False, min_detection_confidence=0.3, min_tracking_confidence=0.5)


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    if not data or 'image' not in data:
        return jsonify({'letter': ''})

    category = data.get('category', 'general')  # Default to 'general' if not provided
    print(f"Received category: {category}")

    # Decode base64 image
    image_data = data['image'].split(',')[1]
    nparr = np.frombuffer(base64.b64decode(image_data), np.uint8)
    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    frame = cv2.flip(frame, 1)
    H, W, _ = frame.shape

    results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    predicted_character = ''

    if results.multi_hand_landmarks:
        data_aux = []
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw landmarks and connections on the frame
            mp_drawing.draw_landmarks(
                frame, hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style()
            )
            x_ = [lm.x for lm in hand_landmarks.landmark]
            y_ = [lm.y for lm in hand_landmarks.landmark]
            for i in range(len(hand_landmarks.landmark)):
                data_aux.append(x_[i] - min(x_))
                data_aux.append(y_[i] - min(y_))
        # Now data_aux will be 42 (one hand) or 84 (two hands)
        if category == "math":
            if len(data_aux) == 42:  # or whatever your math model expects
                pred = math_model.predict([np.asarray(data_aux)])
                predicted_character = math_labels_dict.get(pred[0], '')
        else:
            if len(data_aux) == 42:
                pred = model_42.predict([np.asarray(data_aux)])
                predicted_character = labels_dict_42.get(pred[0], '')
            elif len(data_aux) == 84:
                pred = model_84.predict([np.asarray(data_aux)])
                predicted_character = labels_dict_84.get(pred[0], '')

    return jsonify({'letter': predicted_character})

if __name__ == "__main__":
    app.run(debug=True)

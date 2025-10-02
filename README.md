# Bidirectional Indian Sign Language Communication System

### Bridging communication between ISL users and the wider community

This project enables **two-way communication** between **Indian Sign Language (ISL)** users and non-signers by combining **real-time sign recognition** and **rule-based text-to-sign translation**.  

It was developed in **two phases**:
1. **Streamlit Prototype** — built quickly to validate the approach.
2. **Web Game Version (Expo)** — an interactive, gamified experience with quizzes, animations, and leaderboard to engage users.

The project was also presented as a **research paper**, demonstrating its technical contribution to accessible communication.

---

## 💡 Motivation

India has over 18 million deaf and hard-of-hearing individuals, yet ISL is not widely understood outside the community. Existing solutions are either one-directional (sign → text) or rely on bulky datasets.  

We set out to design a system that is:
- **Bidirectional** → supports both sign recognition *and* text-to-sign.  
- **Lightweight** → works with MediaPipe landmarks instead of heavy video datasets.  
- **Engaging** → gamified to increase adoption and awareness.

---

## 👨‍👩‍👦 Team
- **Mohammed Mudasir Ahmed** (Team Lead)  
- **Ozair Ali**  
- **Syed Ibrahim Ali**

---

## ✨ Key Features

### 🔹 Sign → Text/Speech
- Real-time hand landmark detection with **MediaPipe**.  
- Gesture classification using **MLP models** (trained on 42- and 84-landmark datasets).  
- Outputs translated **text** and **speech (gTTS)**.  

### 🔹 Text/Speech → Sign
- Rule-based model that maps words/phrases to ISL signs.  
- **SVG animations** used for signs → visually clear representation.  
- **gTTS** for speech playback.  

### 🔹 Streamlit Prototype
- Rapid prototyping and proof-of-concept.  
- Live webcam feed → sign recognition → text/speech output.  
- Minimal UI for quick testing.  

### 🔹 Web Game Version (Expo)
- **Frontend**: HTML, CSS, JS (multi-page static website).  
- **Backend**: Flask (`server.py`) runs in parallel for ML inference.  
- **Game-like interaction**: 
  - Learn ISL signs  
  - Take quizzes with images  
  - Score points & view leaderboard  
- **Assets**: quiz images, SVG animations, JSON mappings.  

### 🔹 Research Contribution
- Paper written and presented, detailing model performance, architecture, and social impact. 

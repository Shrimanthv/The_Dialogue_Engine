# 🤖 The Dialogue Engine — BlenderBot Chatbot Deployment

## Table of Contents
- [Demo](#demo)
- [Overview](#overview)
- [Motivation](#motivation)
- [Features](#features)
- [Installation](#installation)
- [Tech Stack](#tech-stack)
- [Deployment on Streamlit](#deployment-on-streamlit)
- [Project Structure](#project-structure)
- [Bug / Feature Request](#bug--feature-request)
- [Future Scope](#future-scope)
- [Technology Used](#technology-used)
- [Author](#author)
---
## Demo
🚀 Live App – [Insert Link to Live Streamlit App Here]

Click the link above to test The Dialogue Engine! Interact with the BlenderBot model, adjust generation settings (Temperature and Max Tokens), and experience the custom chat interface.

## Overview
The Dialogue Engine is an interactive, web-based conversational AI application built using Streamlit and the BlenderBot-400M-distill model from the Hugging Face Transformers library. The project demonstrates the full lifecycle of deploying a sequence-to-sequence (Seq2Seq) conversational model, from initial model loading in a Jupyter Notebook to a polished, professional web interface.

## Motivation
This project was developed to:

Demonstrate proficiency in deploying a large Hugging Face model in a resource-efficient manner using local file storage.

Showcase the power of Streamlit for rapidly building complex, data-driven user interfaces.

Implement custom CSS styling for a professional and modern chat application aesthetic (asymmetric bubbles, subtle shadows).

Provide a practical, fully functional demonstration of a conversational AI system that is ready for production or further development.

## Features
💬 Real-Time Chat: Seamless interaction with the BlenderBot-400M-distill model.

🎨 Custom UI: Professional and clean chat interface with custom-styled message bubbles.

⚙️ Adjustable Settings: Control response creativity and length using sidebar sliders for Temperature and Max Tokens.

💾 Chat Management: Save, load, or clear the conversation history using saved_chat.json.

✨ Smooth UX: Input box automatically clears upon submission using Streamlit's st.form mechanism.

## Installation
Follow these steps to set up and run the application locally.

### 1. Clone the Repository
``` bash

git clone https://github.com/your-username/the-dialogue-engine.git
cd the-dialogue-engine
```
### 2. Create and Activate a Virtual Environment
```bash

conda create -n chat_env python=3.10
conda activate chat_env
```
### 3. Install Dependencies
Install the required libraries:

```bash

pip install -r requirements.txt
```

### 4. Setup Model Files
Run the cells in the chat_box.ipynb notebook. This notebook downloads the facebook/blenderbot-400M-distill model and tokenizer, and saves the necessary files into the local ./chatbot_model directory, which is required by app.py.

### 5. Run the Application
```bash

streamlit run app.py
```
## Tech Stack
Layer	Tool / Library	Purpose
Model	BlenderBot-400M-distill	Core conversational AI.
Backend	Python, PyTorch	Model inference and logic.
Framework	Streamlit	Web application interface and deployment framework.
Libraries	Hugging Face Transformers	Model loading and generation pipeline.
Design	Custom CSS	Styling the chat bubbles and improving UX.



## Deployment on Streamlit
The application is designed for easy deployment on Streamlit Cloud:

Commit the entire project, including app.py, requirements.txt, and the model files in the ./chatbot_model directory (or host them remotely if the directory is too large).

Connect your GitHub repository to Streamlit Cloud.

Select the repository and specify app.py as the main file.

Ensure the environment is configured to handle the transformers and torch dependencies.

Deploy and share the link!

## Project Structure
The_Dialogue_Engine/
│
├── app.py                      # Main Streamlit application with UI and logic
├── chat_box.ipynb              # Jupyter notebook for initial model setup and saving
├── requirements.txt            # Python dependencies (streamlit, transformers, torch)
├── README.md                   # Project documentation
├
└── chatbot_model/              # Saved BlenderBot-400M-distill files
    └── ...                     # (Contains config.json, pytorch_model.bin, etc.)

## Bug / Feature Request
Please open an issue on the GitHub repository if you encounter any bugs or have suggestions for new features.

Reporting Bugs: Include a clear description, steps to reproduce, and any relevant console errors or screenshots.

Requesting Features: Describe the desired new functionality and explain how it would enhance the user experience or performance of The Dialogue Engine.

## Future Scope
🧠 Contextual Memory: Implement a rolling context window to allow the bot to remember topics from earlier in the conversation.

🌐 Integration: Explore deploying the model via a REST API (e.g., FastAPI) and having Streamlit consume the API.

📊 Performance Metrics: Add latency and token count displays to the sidebar for performance monitoring.

🗣️ Voice Input: Integrate a speech-to-text library to allow users to speak their messages.

## Technology Used
<p align="center">
  <img src="https://www.python.org/static/community_logos/python-logo.png" width="110" title="Python" />
  <img src="https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.svg" width="150" title="Streamlit" />
  <img src="https://huggingface.co/front/assets/huggingface_logo-noborder.svg" width="120" title="Hugging Face Transformers" />
  <img src="https://pytorch.org/assets/images/pytorch-logo.png" width="110" title="PyTorch" />
  <img src="https://upload.wikimedia.org/wikipedia/commons/6/61/HTML5_logo_and_wordmark.svg" width="90" title="HTML" />
  <img src="https://upload.wikimedia.org/wikipedia/commons/d/d5/CSS3_logo_and_wordmark.svg" width="90" title="CSS" />
</p>


## Author
Shrimanth V

Email: shrimanthv99@gmail.com

GitHub: [Your GitHub Profile Link]

LinkedIn: [Your LinkedIn Profile Link]

Feel free to reach out for questions or collaboration!
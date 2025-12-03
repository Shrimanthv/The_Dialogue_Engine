import streamlit as st
import json
import os
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

# ------------ Load Model ------------
model_path = "./chatbot_model"

# Use st.cache_resource for heavy objects like models and tokenizers
@st.cache_resource
def load_model():
    """Loads the tokenizer and model from the specified path."""
    try:
        tokenizer = AutoTokenizer.from_pretrained(model_path)
        model = AutoModelForSeq2SeqLM.from_pretrained(model_path)
        return tokenizer, model
    except Exception as e:
        # Handle case where the model folder might not exist or load properly
        st.error(f"Error loading model from {model_path}: {e}")
        st.stop() # Stop the app if the model can't be loaded

tokenizer, model = load_model()

# ------------ Page Config ------------
st.set_page_config(page_title="The Dialogue Engine", page_icon="🤖", layout="centered")
st.title("🤖  Chatbot")
st.write("Welcome to The Dialogue Engine! Chat with your custom BlenderBot model.")
# ------------ Custom Chat UI (CSS) ------------
chat_css = """
<style>
/* 🎨 General Aesthetics */
:root {
    --primary-color: #007AFF; /* A clean, modern blue for key actions/user */
    --secondary-color: #EFEFEF; /* Light gray for subtle bot background */
    --text-color-dark: #2C3E50; /* Deep charcoal for high contrast text */
    --text-color-light: #FFFFFF;
    --shadow-subtle: 0 1px 3px rgba(0, 0, 0, 0.08), 0 1px 2px rgba(0, 0, 0, 0.1);
}

/* Chat container (Keeping this simple) */
.chat-container {
    display: flex;
    flex-direction: column;
    gap: 10px;
}

/* 👤 USER MESSAGE */
.chat-bubble-user {
    /* Color Change: Use a modern blue or a refined, darker green */
    background-color: #1a73e8; /* Google-style professional blue */
    color: var(--text-color-light) !important;
    
    padding: 12px 16px;
    border-radius: 18px 18px 2px 18px; /* Slightly asymmetric for a dynamic look */
    margin: 6px 0; /* Reduced margin for tighter packing */
    max-width: 70%; /* Slightly smaller max width */
    width: fit-content;
    align-self: flex-end;
    
    font-size: 15px; /* Slightly reduced font size */
    line-height: 1.4;
    
    /* Shadow Change: Softer, less intense shadow */
    box-shadow: var(--shadow-subtle);
    -webkit-font-smoothing: antialiased; /* Better text rendering */
}

/* 🤖 BOT MESSAGE */
.chat-bubble-bot {
    /* Color Change: Very light, subtle background */
    background-color: var(--secondary-color); 
    color: var(--text-color-dark) !important; /* Dark text for contrast */
    
    padding: 12px 16px;
    border-radius: 18px 18px 18px 2px; /* Asymmetric, opposite corner */
    margin: 6px 0;
    max-width: 70%;
    width: fit-content;
    align-self: flex-start;
    
    font-size: 15px;
    line-height: 1.4;
    
    /* Shadow Change: Identical subtle shadow for consistency */
    box-shadow: var(--shadow-subtle);
    -webkit-font-smoothing: antialiased; 
}

/* Bold labels (Keeping this for user/bot distinction) */
.chat-bubble-user b {
    color: var(--text-color-light) !important;
    font-weight: 600; /* Slightly heavier bold */
}

.chat-bubble-bot b {
    color: var(--text-color-dark) !important;
    font-weight: 600;
}

/* Hide the st.text_input label for a cleaner look */
div[data-testid="stForm"] > div > div:nth-child(1) > div > label {
    display: none;
}
</style>
"""

st.markdown(chat_css, unsafe_allow_html=True)

# ------------ Sidebar Settings ------------
st.sidebar.header("⚙️ Settings")

temperature = st.sidebar.slider("Temperature", 0.1, 1.5, 1.0, 0.1)
max_tokens = st.sidebar.slider("Max Tokens", 50, 300, 150, 10)

st.sidebar.header("💾 Chat Management")

if st.sidebar.button("Save Chat"):
    with open("saved_chat.json", "w", encoding="utf-8") as f:
        json.dump(st.session_state.get("messages", []), f, indent=4)
    st.sidebar.success("Chat saved as **saved_chat.json**")

if st.sidebar.button("Load Chat"):
    if os.path.exists("saved_chat.json"):
        with open("saved_chat.json", "r", encoding="utf-8") as f:
            st.session_state["messages"] = json.load(f)
        st.sidebar.success("Chat loaded!")
    else:
        st.sidebar.error("No saved chat found!")

if st.sidebar.button("Clear Chat History"):
    st.session_state["messages"] = []
    st.sidebar.success("Chat cleared!")


# ------------ Chat History State ------------
if "messages" not in st.session_state:
    st.session_state["messages"] = []


# ------------ Display Chat Bubbles ------------
# This section uses the custom CSS to display the conversation
for msg in st.session_state["messages"]:
    if msg["role"] == "user":
        st.markdown(f"<div class='chat-bubble-user'><b>You:</b> {msg['text']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='chat-bubble-bot'><b>Bot:</b> {msg['text']}</div>", unsafe_allow_html=True)

# Separate the chat history from the input box
st.markdown("---") 


# ------------ Chat Input (FIXED: Using st.form for input clearing) ------------
# Use a form with clear_on_submit=True to automatically clear the text box
with st.form(key='chat_form', clear_on_submit=True):
    # Use a hidden label/placeholder for better UI integration
    user_input = st.text_input("Type your message...", key="user_input_field", label_visibility="collapsed", placeholder="Type your message...")
    
    # Use st.form_submit_button
    submit_button = st.form_submit_button(label='Send')

    # Logic runs only when the button is clicked and input is not empty
    if submit_button and user_input:
        # 1. Add user message
        st.session_state["messages"].append({"role": "user", "text": user_input})
        
        # 2. Generate bot response (wrapped in st.spinner for UX)
        with st.spinner('🤖 Generating response...'):
            inputs = tokenizer.encode(user_input, return_tensors="pt")
            
            # Use torch.no_grad() for inference to save memory
            with torch.no_grad():
                outputs = model.generate(
                    inputs,
                    max_new_tokens=max_tokens,
                    do_sample=True,
                    temperature=temperature
                )
            response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

        # 3. Add bot message
        st.session_state["messages"].append({"role": "bot", "text": response})

        # 4. Rerun to display the newly added messages
        st.rerun()
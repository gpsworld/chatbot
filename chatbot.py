import streamlit as st
import time
import google.generativeai as genai
import os
from dotenv import load_dotenv
# Replace with your actual API key

load_dotenv()

genai.configure(api_key=os.environ["api_key"])
model = genai.GenerativeModel(model_name="gemini-2.0-flash-exp")

st.title("AI Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        # Initialize progress bar
        progress_bar = st.progress(0)
        
        # Simulate progress updates
        for percent_complete in range(0, 101, 10):
            progress_bar.progress(percent_complete / 100.0)
            time.sleep(0.1)  # Simulating delay (replace or adjust as needed)

        # Generate model response
        response = model.generate_content(prompt)
        
        # Update the chat with the generated response
        full_response = response.text
        message_placeholder.markdown(full_response)

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})


# Footer styling
footer = """
    <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: transparent;
            color: #716767;
            text-align: center;
            padding: 10px 0;
            font-size: 14px;
            border-top: 1px solid #ccc;
            z-index: 1;
        }
        .footer a {
            color: #0066cc;
            text-decoration: none;
        }
        .footer a:hover {
            text-decoration: underline;
        }
    </style>
    <div class="footer">
        Created with ❤️ by <a href="https://github.com/gpsworld" target="_blank">gpsworld</a>
    </div>
"""
st.markdown(footer, unsafe_allow_html=True)

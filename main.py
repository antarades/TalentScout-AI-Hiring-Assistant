import streamlit as st
import cohere
import os
import re
from dotenv import load_dotenv
from prompts import (
    get_greeting_prompt,
    get_info_prompt,
    get_tech_stack_prompt,
    get_question_generation_prompt,
    get_fallback_prompt,
    get_exit_prompt
)

load_dotenv()
cohere_api_key = os.getenv("COHERE_API_KEY")
co = cohere.Client(cohere_api_key)

st.set_page_config(page_title="TalentScout - AI Hiring Assistant", layout="wide")

# CSS Styles
st.markdown("""
    <style>
        html, body, [class*="css"] {
            font-family: 'Segoe UI', sans-serif;
        }
        .stApp {
            background: linear-gradient(to right, #e0c3fc, #8ec5fc);
            display: flex;
            flex-direction: column;
            justify-content: center;
            min-height: 100vh;
        }
        .block-container {
            background-color: #ffffff;
            padding: 2rem;
            border-radius: 12px;
            margin: auto;
            max-width: 900px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            display: flex;
            flex-direction: column;
            justify-content: center;
        }
        .block-container h1, .block-container h2, .block-container p, .block-container div {
            color: #000000 !important;
        }
        .stTextInput>div>div>input,
        .stTextArea textarea {
            border-radius: 6px;
            padding: 0.4rem;
            border: 1px solid #ccc;
            background-color: #f1ebff;
            color: black !important;
        }
        .stButton>button, div.stForm button {
            background-color: transparent !important;
            border: 2px solid #8c52ff !important;
            color: #8c52ff !important;
            font-weight: 500;
            padding: 0.4rem 0.8rem;
            border-radius: 6px;
        }
        .stButton>button:hover, div.stForm button:hover {
            background-color: #ece0ff !important;
            color: #6a00ff !important;
        }
    </style>
""", unsafe_allow_html=True)

T = {
    "title": "TalentScout - AI Hiring Assistant",
    "begin": "Begin",
    "info_header": "Candidate Information",
    "name": "Full Name",
    "email": "Email Address",
    "phone": "Phone Number",
    "exp": "Years of Experience",
    "pos": "Desired Position(s)",
    "loc": "Current Location",
    "tech": "Tech Stack (Languages, Frameworks, Tools)",
    "submit": "Submit & Generate Questions",
    "invalid_email": "Please enter a valid email address.",
    "invalid_phone": "Phone number should be numeric and 10–15 digits long.",
    "incomplete": "Please fill out all the required fields.",
    "questions_title": "Technical Questions",
    "chat_title": "Follow-Up Chat with TalentScoutBot",
    "end": "End Conversation",
    "send": "Send"
}

chat_history = []

if "stage" not in st.session_state:
    st.session_state.stage = "intro"
if "chat_log" not in st.session_state:
    st.session_state.chat_log = []
if "clear_chat_input" not in st.session_state:
    st.session_state.clear_chat_input = False
if st.session_state.clear_chat_input:
    st.session_state.chat_input = ""
    st.session_state.clear_chat_input = False

# Ask cohere
def ask_cohere(prompt):
    fallback_instruction = get_fallback_prompt()
    user_info = f"The candidate's name is {st.session_state.get('name', 'Unknown')}, they have {st.session_state.get('experience', 'N/A')} years of experience, and are applying for {st.session_state.get('position', 'a position')} in {st.session_state.get('location', 'an unspecified location')}"
    preamble = f"{user_info}\n{fallback_instruction}"

    response = co.chat(
        message=prompt,
        chat_history=chat_history,
        model="command-r",
        temperature=0.7,
        preamble=preamble
    )
    chat_history.append({"role": "USER", "message": prompt})
    chat_history.append({"role": "CHATBOT", "message": response.text})
    return response.text

# UI Workflow
with st.container():
    if st.session_state.stage == "intro":
        st.title(T["title"])
        st.write(get_greeting_prompt("English"))
        if st.button(T["begin"]):
            st.session_state.stage = "form"

    elif st.session_state.stage == "form":
        st.subheader(T["info_header"])
        name = st.text_input(T["name"])
        email = st.text_input(T["email"])
        phone = st.text_input(T["phone"])
        experience = st.slider(T["exp"], 0, 40)
        position = st.text_input(T["pos"])
        location = st.text_input(T["loc"])
        tech_stack = st.text_area(T["tech"])

        email_valid = re.match(r"[^@\s]+@[^@\s]+\.[a-zA-Z0-9]+$", email)
        phone_valid = phone.isdigit() and 10 <= len(phone) <= 15
        fields_filled = all([name.strip(), email_valid, phone_valid, position.strip(), location.strip(), tech_stack.strip()])

        if st.button(T["submit"]):
            if not fields_filled:
                if not email_valid:
                    st.warning(T["invalid_email"])
                if not phone_valid:
                    st.warning(T["invalid_phone"])
                if not all([name.strip(), position.strip(), location.strip(), tech_stack.strip()]):
                    st.warning(T["incomplete"])
            else:
                st.session_state.name = name
                st.session_state.experience = experience
                st.session_state.position = position
                st.session_state.location = location
                prompt = f"You are an AI hiring assistant. Based on the candidate's tech stack: {tech_stack},\ngenerate 3 to 5 technical interview questions that assess real-world proficiency in each technology mentioned.\nEnsure questions are relevant, varied in difficulty, and focus on practical knowledge.\nReturn only the questions in a numbered list."
                st.session_state.questions = ask_cohere(prompt)
                st.session_state.stage = "questions"

    elif st.session_state.stage == "questions":
        st.subheader(T["questions_title"])
        st.markdown(st.session_state.questions)
        if st.button("Continue to Live Chat"):
            st.session_state.stage = "chat"

    elif st.session_state.stage == "chat":
        st.subheader(T["chat_title"])

        for role, msg in st.session_state.chat_log:
            st.markdown(f"**{'You' if role == 'user' else '🤖 TalentScoutBot'}:** {msg}")

        with st.form("chat_form"):
            user_input = st.text_input("", placeholder="Ask a question...", key="chat_input")
            submitted = st.form_submit_button(T["send"])

        if submitted:
            input_text = st.session_state.get("chat_input", "").strip()
            if input_text:
                st.session_state.chat_log.append(("user", input_text))
                reply = ask_cohere(input_text)
                st.session_state.chat_log.append(("bot", reply))
                st.session_state.clear_chat_input = True

        col1, _ = st.columns([2, 5])
        with col1:
            end_clicked = st.button(T["end"])
        if end_clicked:
            st.session_state.stage = "end"

    elif st.session_state.stage == "end":
        st.success(get_exit_prompt("English"))

st.markdown("""
<style>
input::placeholder {
  color: black !important;
  opacity: 0.7;
}
</style>
""", unsafe_allow_html=True)
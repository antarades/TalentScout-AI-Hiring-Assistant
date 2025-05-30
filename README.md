# TalentScout – AI Hiring Assistant 🤖

TalentScout is an intelligent, interactive hiring assistant chatbot built using **Streamlit** and powered by **Cohere's Command-R LLM**. It helps recruitment agencies screen candidates by gathering personal information, assessing technical expertise, and conducting follow-up Q&A chats — all in a sleek, responsive UI.

---

## 🧠 Features

- Clean Streamlit UI for candidate interaction
- Gathers:
  - Full Name
  - Email
  - Phone
  - Years of Experience
  - Desired Position(s)
  - Current Location
  - Tech Stack (Languages, Frameworks, Tools)
- Generates 3–5 **custom technical interview questions** based on candidate’s tech stack
- Allows **live follow-up questions** with context-awareness
- Graceful fallback for unclear prompts
- Personalized responses based on provided user info
- Elegant styling with custom CSS

---

## 🖥️ Demo

https://www.loom.com/share/your-demo-link-here *(Replace with your Loom link if available)*

---

## 🚀 Getting Started

### 1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/talent-scout-chatbot.git
cd talent-scout-chatbot

```

### 2. **Install Dependencies**

```bash
pip install -r requirements.txt
```

### 3. **Set up environment variables**
Create a .env file in the root directory with your Cohere API key:

```ini
COHERE_API_KEY=your_api_key_here
```
💡 Get your free API key at https://dashboard.cohere.com/

### 4. **Run the App**

```bash
streamlit run main.py
```
---

## 🗂️ File Structure

```bash
├── main.py                # Main Streamlit UI + Logic
├── prompts.py             # Modular prompt functions for Cohere
├── .env                   
├── requirements.txt
├── README.md  

```

---

## 🧪 Technologies Used

- Streamlit – Frontend & state management
- Cohere Command-R – LLM for Q&A and context
- dotenv – Manage API secrets

---

## ✨ Optional Enhancements Implemented

- Personalized responses based on candidate information
- Custom UI with styled buttons and layout

---

## 📝 Prompt Engineering Overview

We use structured system prompts to guide the LLM:

- Initial greeting prompt
- Information gathering prompt
- Tech-stack specific question generation
- Fallback instructions for edge cases
- Context-aware follow-up responses
- Conversation exit summary

All prompts are modularized in prompts.py.

---

## 📃 License
This project is for academic purposes under fair use. For commercial or extended use, contact the project creator.

---

## 🙋‍♀️ Author
Built by Antara Srivastava
GitHub: github.com/antarades
Email: antarakyw05@gmail.com
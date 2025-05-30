def get_greeting_prompt(language="English"):
    return (
        "Hello! I’m TalentScout, your friendly hiring assistant.\n"
        "I’ll be asking you a few questions to get to know you better and assess your tech skills.\n"
        "Type 'exit' anytime to end the conversation. Shall we start?"
    )

def get_info_prompt(language="English"):
    return (
        "Great! Let's start with some basic information:\n"
        "- Full Name:\n"
        "- Email Address:\n"
        "- Phone Number:\n"
        "- Years of Experience:\n"
        "- Desired Position(s):\n"
        "- Current Location:"
    )

def get_tech_stack_prompt(language="English"):
    return (
        "Thanks! Now, please list the technologies you're comfortable with.\n"
        "Include programming languages, frameworks, databases, and tools. For example: Python, Django, MySQL, Git."
        )

def get_question_generation_prompt(tech_stack, language, name="", experience="", position="", location=""):
    return (
        f"Given that the candidate's name is {name}, they have {experience} years of experience, "
        f"they're applying for the position of {position}, and they are currently based in {location}, "
        f"suggest personalized technical interview questions based on their tech stack: {tech_stack}. "
        f"Make the questions appropriate for someone with {experience} years of experience. "
        f"Respond in {language.lower()}."
    )

def get_fallback_prompt(language="English"):
    return (
        "I'm sorry, I didn’t quite catch that. Could you please rephrase or provide more details?")

def get_exit_prompt(language="English"):
    return (
        "Thank you for chatting with TalentScout! We’ll review your responses and get back to you soon.\n"
        "Good luck with your application!"
    )

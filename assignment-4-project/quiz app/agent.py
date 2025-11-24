from tools import summarize_text, generate_quiz

def get_agent_response(prompt: str, text: str) -> str:
    """Gets the agent's response based on the prompt and text."""
    if "summarize" in prompt.lower():
        return summarize_text(text)
    elif "quiz" in prompt.lower():
        return generate_quiz(text)
    else:
        return "I can only summarize text and generate quizzes."
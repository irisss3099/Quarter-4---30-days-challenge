import streamlit as st 
from agent import get_agent_response

st.title("📝 Text Summarizer & Quiz Generator")

text_input = st.text_area("Enter the text you want to process:")

col1, col2 = st.columns(2)

with col1:
    if st.button("Summarize"):
        if text_input:
            summary = get_agent_response("summarize", text_input)
            st.success("Summary:")
            st.write(summary)
        else:
            st.warning("Please enter some text to summarize.")

with col2:
    if st.button("Generate Quiz"):
        if text_input:
            quiz = get_agent_response("quiz", text_input)
            st.success("Quiz:")
            st.write(quiz)
        else:
            st.warning("Please enter some text to generate a quiz from.")

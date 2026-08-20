import streamlit as st

from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("user", "Question: {question}")
    ]
)

st.title("Chat GPT")

llm = OllamaLLM(model="gemma2:latest")

output_parser = StrOutputParser()

chain = prompt | llm | output_parser


# Store questions and answers
if "chat" not in st.session_state:
    st.session_state.chat = []


# Display previous questions and answers
for question, answer in st.session_state.chat:
    st.write("You:", question)
    st.write("AI:", answer)


# Question box
input_text = st.text_input(
    "How may I help you?",
    key=f"question_{len(st.session_state.chat)}"
)


if input_text:

    response = chain.invoke(
        {"question": input_text}
    )

    st.session_state.chat.append(
        (input_text, response)
    )

    st.rerun()
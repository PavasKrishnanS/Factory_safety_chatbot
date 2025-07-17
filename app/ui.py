import streamlit as st
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.chatbot import get_answer



st.set_page_config(page_title="Factory Safety Chatbot", page_icon="🦺")

SUGGESTIONS = [
    "What are the basic industrial safety rules?",
    "Explain the lockout/tagout procedure.",
    "How should chemical spills be handled?",
    "What PPE is required for welding?",
    "Describe emergency evacuation steps.",
]

st.title(" 🏭 Factory Safety Chatbot")

if "history" not in st.session_state:
    st.session_state.history = []

for sender, msg in st.session_state.history:
    with st.chat_message("user" if sender=="user" else "assistant"):
        st.markdown(msg)

if len(st.session_state.history) == 0:
    st.info("👋 Hi! I'm your Factory Safety Assistant. Try one of these examples:")
    cols = st.columns(2)
    for i, suggestion in enumerate(SUGGESTIONS):
        if cols[i % 2].button(suggestion, key=f"sugg_{i}"):
            st.session_state.history.append(("user", suggestion))
            with st.chat_message("user"):
                st.markdown(suggestion)
            with st.spinner("Bot is typing..."):
                answer = get_answer(suggestion)
            st.session_state.history.append(("bot", answer))
            with st.chat_message("assistant"):
                st.markdown(answer)
            st.rerun()

if prompt := st.chat_input("Ask me about safety..."):
    st.session_state.history.append(("user", prompt))
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.spinner("Bot is typing..."):
        answer = get_answer(prompt)
    st.session_state.history.append(("bot", answer))
    with st.chat_message("assistant"):
        st.markdown(answer)
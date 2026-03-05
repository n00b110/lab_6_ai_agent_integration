import streamlit as st

from agent import run_agent

st.title("Toyota Stock AI Agent")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.chat_input("Ask about Toyota stock")

if user_input:
    st.session_state.messages.append(("user", user_input))

    with st.spinner("Agent thinking..."):
        response = run_agent(user_input)

    st.session_state.messages.append(("assistant", str(response)))


for role, msg in st.session_state.messages:
    if role == "user":
        st.chat_message("user").write(msg)

    else:
        st.chat_message("assistant").write(msg)

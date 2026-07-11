import streamlit as st
from backend.langgraph_agent import run_agent

st.set_page_config(
    page_title="AI First CRM",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI First CRM")

st.write(
    "AI-powered Customer Relationship Management System using LangGraph"
)


# Sidebar

st.sidebar.title("CRM Menu")

option = st.sidebar.selectbox(
    "Choose Action",
    [
        "Dashboard",
        "Customer Search",
        "Add Customer",
        "Update Customer",
        "Delete Customer",
        "Analytics"
    ]
)


# AI Chat Interface

st.subheader("💬 AI CRM Assistant")

query = st.text_input(
    "Ask your CRM assistant"
)


if st.button("Submit"):

    if query:

        response = run_agent(query)

        st.success(response)

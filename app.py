import streamlit as st
from prompts import get_answer_from_gpt

# Set page title
st.set_page_config(page_title="MedGuide - Medical Device Assistant")

# Title and subtitle
st.title("🩺 MedGuide")
st.subheader("Your AI Assistant for Using Medical Devices")

# Input fields
selected_device = st.selectbox(
    "Select a medical device:",
    ["Blood Pressure Monitor", "Insulin Pen", "Inhaler", "Glucometer", "Thermometer"]
)

user_question = st.text_area("❓ What would you like to know about this device?")

# Ask button
if st.button("Get Answer"):
    if user_question.strip() != "":
        answer = get_answer_from_gpt(selected_device, user_question)
        st.success("💬 Answer:")
        st.write(answer)
    else:
        st.warning("Please enter a question to get started.")

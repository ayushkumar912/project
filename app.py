import streamlit as st
from modules.data_loader import load_data
from modules.qa_engine import get_answer
from modules.vector_search import create_vectorstore
from modules.feedback import send_feedback

df = load_data()
st.set_page_config(page_title="Titanic QA Chatbot")
st.title("🚢 Titanic Dataset Chatbot")
st.write("Ask me anything about the Titanic passengers!")

query_text = st.text_input("Enter your question:", placeholder="Who was in cabin C128?")

def process_query(query):
    context = df.to_string()
    return get_answer(query, context)

if st.button("Submit"):
    with st.spinner("Processing..."):
        result = process_query(query_text)
        st.success(result)

col1, col2 = st.columns(2)
with col1:
    st.button("👍", on_click=send_feedback, args=(1, 1))
with col2:
    st.button("👎", on_click=send_feedback, args=(1, 0))
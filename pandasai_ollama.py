from local_llm import OllamaClientLLM
import streamlit as st
import pandas as pd
from pandasai import SmartDataframe

llm = OllamaClientLLM(model="llama3", host="http://localhost:11434")

st.title("Data analysis with PandasAI and Local Ollama")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write(data.head(3))

    df = SmartDataframe(data, config={"llm": llm})
    prompt = st.text_area("Enter your prompt:")

    if st.button("Generate"):
        if prompt:
            with st.spinner("Generating response..."):
                st.write(df.chat(prompt))

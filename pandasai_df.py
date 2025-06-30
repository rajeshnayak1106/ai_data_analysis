import pandasai as pai
from pandasai_openai.openai import OpenAI
import streamlit as st

st.title("PandasAI with OpenAI")

st.set_page_config(
    page_title="PandasAI with OpenAI", page_icon=":bar_chart:", layout="wide"
)


OPEN_AI_API_KEY = st.sidebar.text_input("Enter OpenAI API key:")
if OPEN_AI_API_KEY:
    display_key = (
        OPEN_AI_API_KEY[:2] + "*" * (len(OPEN_AI_API_KEY) - 5) + OPEN_AI_API_KEY[-3:]
    )
    st.sidebar.write(f"Current key: {display_key}")
else:
    st.sidebar.write("Please enter OpenAI API key.")

llm = OpenAI(OPEN_AI_API_KEY)

pai.config.set({"llm": llm})


# Sample DataFrame
df = pai.DataFrame(
    {
        "country": [
            "United States",
            "United Kingdom",
            "France",
            "Germany",
            "Italy",
            "Spain",
            "Canada",
            "Australia",
            "Japan",
            "China",
        ],
        "revenue": [5000, 3200, 2900, 4100, 2300, 2100, 2500, 2600, 4500, 7000],
    }
)

st.write(df)

prompt = st.text_area("Enter your prompt:")

if st.button("Generate"):
    if prompt:
        with st.spinner("Generating response..."):
            st.write(df.chat(prompt))

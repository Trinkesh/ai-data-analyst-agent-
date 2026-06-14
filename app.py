import streamlit as st 
import pandas as pd
from utils.llm import analyze_data
from utils.analyst import get_dataset_summary
import matplotlib.pyplot as plt
from utils.analyst import detect_chart_request


st.set_page_config(page_title= "AI Data Analyst Agent Trinks")

st.title("AI Data Analyst Agent Trinks")

uploaded_file = st.file_uploader("upload csv file here", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Rows", df.shape[0])
    with col2:
        st.metric("Columns", df.shape[1])


    st.success("file uploaded successfully")
    st.subheader("Data Preview")

    question = st.text_input("Ask question about your data")

    if question:
        if detect_chart_request(question):
            st.success("chart request detected")
        else:
            answer = analyze_data(question, df)
            st.write(answer
            )

    if question:
        with st.spinner("Analyzing data..."):
            answer = analyze_data(question, df)

        st.subheader("AI Analysis...")
        st.write(answer)

    st.dataframe(df.head())

    numeric_cols = df.select_dtypes(include="number").columns
    if len(numeric_cols) > 0:

        selected_col = st.selectbox("select numeric column", numeric_cols)

        fig,ax = plt.subplots()
        df[selected_col].plot(kind="hist", ax=ax)
        st.pyplot(fig)

    summary = get_dataset_summary(df)
    st.subheader("Dataset Summary")
    st.write("rows", summary["Rows"])
    st.write("columns", summary["Columns"]) 
    st.write("column names", summary["Column Names"])



    st.write("Rows", df.shape[0])
    st.write("Columns", df.shape[1])

    


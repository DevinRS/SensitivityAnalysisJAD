import streamlit as st
import pandas as pd
import plotly.express as px



# 1. Page Config
st.set_page_config(
    page_title="Univariate Analysis Tool",
    page_icon='🔧'
)

st.title('Univariate Analysis Tool')
uploaded_file = st.file_uploader("Choose a file", type='csv')
if uploaded_file is not None:
    
    # Can be used wherever a "file-like" object is accepted:
    df = pd.read_csv(uploaded_file)

    columns = df.columns
    options = st.multiselect(
        'Select Variables of Interest',
        columns)

    col1, col2 = st.columns([1, 2])
    if(len(options) != 0):
        for i in range(len(options)):
            with col1:
                st.header(options[i])
                st.dataframe(df[options[i]].describe())
            with col2:
                st.plotly_chart(px.histogram(df[options[i]], x=options[i]), use_container_width=True)

import streamlit as st
import pandas as pd
import plotly.express as px
import scipy.stats

# 1. Page Config
st.set_page_config(
    page_title="Multivariate Analysis Tool",
    page_icon='🔧'
)

st.title('Multivariate Analysis Tool')
uploaded_file = st.file_uploader("Choose a file", type='csv')
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    columns = df.columns
    
    col1, col2 = st.columns(2)
    with col1:
        option1 = st.selectbox(
            'Select Variable of Interest',
            columns)
        column2 = [item for item in columns if item != option1]
    with col2:
        option2 = st.selectbox(
            'Select Variable of Interest',
            column2)
    
    fig = px.scatter(df, x=option1, y=option2, trendline='ols', trendline_color_override='red')
    st.plotly_chart(fig, use_container_width=True)

    df_nan = df.dropna()
    st.info(f'Pearson Correlation Coefficient: {round(scipy.stats.pearsonr(df_nan[option1], df_nan[option2])[0], 2)}')
    st.info(f'Slope: {round(scipy.stats.linregress(df_nan[option1], df_nan[option2]).slope, 2)}')
    st.info(f'y-Intercept: {round(scipy.stats.linregress(df_nan[option1], df_nan[option2]).intercept, 2)}')
    st.info(f'Standard Error: {round(scipy.stats.linregress(df_nan[option1], df_nan[option2]).stderr, 2)}')
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Page title
st.title('CSV Data Dashboard')

# File upload
uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file is not None:
    # Read the uploaded CSV file
    data = pd.read_csv(uploaded_file)

    # Show the data
    st.subheader('Data Preview')
    st.write(data)

    # Summary statistics
    st.subheader('Summary Statistics')
    st.write(data.describe())

    # Data Visualization
    st.subheader('Data Visualization')

    # Histogram
    st.subheader('Histogram')
    selected_column_hist = st.selectbox('Select Column for Histogram', data.columns)
    plt.hist(data[selected_column_hist].dropna(), bins=20, color='skyblue', edgecolor='black')
    st.pyplot()

    # Scatter plot
    st.subheader('Scatter Plot')
    x_column = st.selectbox('X-axis', data.columns)
    y_column = st.selectbox('Y-axis', data.columns)
    plt.scatter(data[x_column], data[y_column], alpha=0.5)
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    st.pyplot()

    # Pairplot
    st.subheader('Pairplot')
    sns.pairplot(data.dropna())
    st.pyplot()

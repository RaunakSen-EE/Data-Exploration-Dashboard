pip install matplotlib
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
@st.cache
def load_data():
    df = pd.read_csv('your_dataset.csv')  # Replace 'your_dataset.csv' with the path to your dataset
    return df

# Main function to run the app
def main():
    # Load the data
    df = load_data()

    # Sidebar - Filters
    st.sidebar.header('Filter Options')

    # Filter by column
    column_to_filter = st.sidebar.selectbox('Filter by Column', df.columns)
    filter_value = st.sidebar.text_input(f'Filter by {column_to_filter}')

    # Filter the data
    filtered_data = df[df[column_to_filter].str.contains(filter_value, case=False)]

    # Display the filtered data
    st.write(filtered_data)

    # Sidebar - Visualization Options
    st.sidebar.header('Visualization Options')

    # Select visualization type
    visualization_type = st.sidebar.selectbox('Select Visualization Type', ['Histogram', 'Line Plot', 'Scatter Plot'])

    # Main content area
    st.subheader('Data Visualization')

    # Plot based on selected visualization type
    if visualization_type == 'Histogram':
        selected_column = st.selectbox('Select column for Histogram', df.columns)
        plt.hist(df[selected_column])
        st.pyplot()
    elif visualization_type == 'Line Plot':
        x_column = st.selectbox('Select X-axis column', df.columns)
        y_column = st.selectbox('Select Y-axis column', df.columns)
        plt.plot(df[x_column], df[y_column])
        st.pyplot()
    elif visualization_type == 'Scatter Plot':
        x_column = st.selectbox('Select X-axis column', df.columns)
        y_column = st.selectbox('Select Y-axis column', df.columns)
        plt.scatter(df[x_column], df[y_column])
        st.pyplot()

if __name__ == '__main__':
    main()

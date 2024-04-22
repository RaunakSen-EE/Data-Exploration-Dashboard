import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
@st.cache
def load_data():
    data = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
    return data

data = load_data()

# Sidebar
st.sidebar.header('Filters')

# Age filter
age_slider = st.sidebar.slider('Age', int(data['Age'].min()), int(data['Age'].max()), (int(data['Age'].min()), int(data['Age'].max())))

# Class filter
class_checkbox = st.sidebar.multiselect('Class', sorted(data['Pclass'].unique()), sorted(data['Pclass'].unique()))

# Filter data
filtered_data = data[(data['Age'] >= age_slider[0]) & (data['Age'] <= age_slider[1]) & (data['Pclass'].isin(class_checkbox))]

# Main content
st.title('Titanic Data Dashboard')

# Show filtered data
st.subheader('Filtered Data')
st.write(filtered_data)

# Visualization
st.subheader('Visualization')

# Bar plot
st.subheader('Survival Rate by Class')
survival_rate_by_class = data.groupby('Pclass')['Survived'].mean()
plt.bar(survival_rate_by_class.index, survival_rate_by_class.values)
plt.xlabel('Class')
plt.ylabel('Survival Rate')
st.pyplot()

# Scatter plot
st.subheader('Age vs Fare')
sns.scatterplot(x='Age', y='Fare', data=data, hue='Survived')
st.pyplot()

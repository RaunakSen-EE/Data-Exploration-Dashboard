# prompt: create a dashboard from data

import pandas as pd
from google.colab import data_table

# Load the data
df = pd.read_csv('data.csv')

# Create a data table
data_table.DataTable(df)

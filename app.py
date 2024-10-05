import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt
import os



# Read the dataset's csv file 
df =pd.read_csv(r"c:\users\nsuka\Desktop\Test_Sample_project\Project_car_analysis\vehicles_us.csv")
df.head()

# Add a header
st.header("Car Analysis Dashboard")


# Create a Plotly express histogram
fig_hist = px.histogram(df, x='price', title='Price Distribution')
st.plotly_chart(fig_hist)

# Add a scatterplot for 'price' vs 'odometer'
fig_hist = px.scatter(df, x='odometer', y='price', color='condition', title='Price vs. Odometer by Condition')
st.write(fig_hist)

# Checkbox to show/hide trendline in scatter plot
show_trendline = st.checkbox("Show Trendline in Scatter Plot")
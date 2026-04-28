python
import pandas as pd
import plotly.express as px

# Load the dataset for Q1 2023
data_q1 = pd.read_excel('Distribution_of_Beneficiaries_per_Gender_Q1_2023.xlsx')

# Data Cleaning and Preparation
data_q1['Percentage'] = data_q1['Count'] / data_q1['Count'].sum() * 100

# Create a bar chart for gender distribution
fig_gender_distribution = px.bar(
    data_q1, 
    x='Type', 
    y='Count', 
    color='Type', 
    title='Gender Distribution for Q1 2023',
    labels={'Count': 'Number of Beneficiaries', 'Type': 'Gender Type'}
)

# Create a pie chart for percentage distribution
fig_percentage_distribution = px.pie(
    data_q1, 
    values='Percentage', 
    names='Type', 
    title='Percentage Distribution of Beneficiaries by Gender for Q1 2023'
)

# Show the charts
fig_gender_distribution.show()
fig_percentage_distribution.show()

# Save cleaned data to a new file
data_q1.to_excel('Cleaned_Distribution_of_Beneficiaries_per_Gender_Q1_2023.xlsx', index=False)

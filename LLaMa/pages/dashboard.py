import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from app import get_data


st.set_page_config(layout="wide")
# Set the title of the app
st.title("Feedback Data Dashboard")

df = get_data()

# Prepare data for visualization
# Count occurrences of each Target_group and calculate mean Confidence per group
grouped_df = df.groupby('Target_group').agg({
    'Confidence': 'mean',  # Calculate average confidence for each group
    'Target_group': 'count'  # Count occurrences of each Target_group
}).rename(columns={'Target_group': 'Count'}).reset_index()

# First Chart - Horizontal Bar for Target_group Count and Line for Confidence
fig1 = go.Figure()

# Create hover text that includes both confidence and sentiment
hover_text = [
    f"Count: {count}<br>Average Confidence: {confidence:.2f}<br>Sentiment: {sentiment}"
    for count, confidence, sentiment in zip(grouped_df['Count'], grouped_df['Confidence'], df.groupby('Target_group')['Sentiment'].first())
]

# Horizontal bar chart for Target_group counts with vibrant colors
fig1.add_trace(go.Bar(
    x=grouped_df['Count'],
    y=grouped_df['Target_group'],
    orientation='h',
    name="Target Group Count",
    marker=dict(color='rgba(33, 150, 243, 0.8)'),  # Bright blue
    hoverinfo='text',
    text=hover_text
))

# Line chart for average Confidence by Target_group with a vibrant red line
fig1.add_trace(go.Scatter(
    x=grouped_df['Confidence'],
    y=grouped_df['Target_group'],
    mode='lines+markers',
    name="Average Confidence",
    line=dict(color='rgba(255, 255, 0, 1)', width=3),  # Bright orange-red
    marker=dict(size=8, color='rgba(255, 87, 34, 0.9)'),
    hoverinfo='text',
    text=hover_text
))

fig1.update_layout(
    title="Target Group Count and Average Confidence",
    xaxis_title="Count / Confidence Level",
    yaxis_title="Target Group",
    barmode='stack',
    template="plotly_white",
    height=500
)
# Second Chart - Pie Chart of Sentiment Distribution with vibrant colors
fig2 = px.pie(
    df,
    names='Sentiment',
    title="Sentiment Distribution of Feedback",
    color_discrete_sequence=px.colors.qualitative.Bold  # Vibrant color palette
)

# Layout to display both charts side-by-side, using full width

# Display the charts side by side with a 2:1 ratio
# col1, col2 = st.columns([4, 1])

# with col1:
#     st.plotly_chart(fig1, use_container_width=True)  # First chart uses 2/3 of the width

# with col2:
#     st.plotly_chart(fig2, use_container_width=True) 
st.plotly_chart(fig1, use_container_width=True) 
st.plotly_chart(fig2, use_container_width=True) 

# Load the CSV file into a DataFrame


# Display the DataFrame in the app
st.write("### Feedback Data Table")
st.write(df)    
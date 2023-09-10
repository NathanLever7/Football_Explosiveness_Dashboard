import streamlit as st
import pandas as pd
import os
from datetime import datetime
import requests

# Base directory where the CSV files are stored.
# This assumes that the data folders are in the same directory as your script.
base_dir = os.path.abspath(os.path.dirname(__file__))

import matplotlib.pyplot as plt  # Import matplotlib here

def load_data(league, season):
    base_url = "https://raw.githubusercontent.com/NathanLever7/Football_Explosiveness_Dashboard/main/"
    season_dir = f'{league.replace(" ", "_")}_{season.replace("/", "_")}/'
    
    # Load data from GitHub using raw file URLs
    team_explosiveness_url = f"{base_url}{season_dir}Team_Explosiveness.csv"
    
    # Explicitly set column names when reading the CSV
    team_explosiveness = pd.read_csv(
        team_explosiveness_url,
        encoding='utf-8-sig',
        names=['Squad', 'Team Explosiveness Index']  # Replace with actual column names
    )
    
    return team_explosiveness

# Streamlit UI
st.title('Football Analysis Dashboard')

# Let users select a league and season
league = st.sidebar.selectbox('Select League', ['Premier League'])  # Add other leagues to the list as needed
season = st.sidebar.selectbox('Select Season', ['2023/24', '2022/23'])  # Add other seasons to the list as needed

# Load the data for the selected league and season
team_explosiveness = load_data(league, season)

# Display the chart
st.header('Team Explosiveness')
fig, ax = plt.subplots(figsize=(8, 6))

team_explosiveness

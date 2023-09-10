import streamlit as st
import pandas as pd
import os
from datetime import datetime  # Import the datetime module

# Base directory where the CSV files are stored.
# This assumes that the data folders are in the same directory as your script.
base_dir = os.path.abspath(os.path.dirname(__file__))

import pandas as pd
import requests

def load_data(league, season):
    base_url = "https://raw.githubusercontent.com/NathanLever7/Football_Explosiveness_Dashboard/main/"
    season_dir = f'{league.replace(" ", "_")}_{season.replace("/", "_")}/'
    
    # Load data from GitHub using raw file URLs
    team_explosiveness_url = f"{base_url}{season_dir}Team_Explosiveness.csv"
    opposition_explosiveness_url = f"{base_url}{season_dir}Opposition_Explosiveness.csv"
    player_explosiveness_url = f"{base_url}{season_dir}Player_Explosiveness.csv"
    player_efficiency_url = f"{base_url}{season_dir}Player_Efficiency.csv"
    
    # Fetch data using requests
    team_explosiveness = pd.read_csv(team_explosiveness_url, encoding='utf-8-sig')
    opposition_explosiveness = pd.read_csv(opposition_explosiveness_url, encoding='utf-8-sig')
    player_explosiveness = pd.read_csv(player_explosiveness_url, encoding='utf-8-sig')
    player_efficiency = pd.read_csv(player_efficiency_url, encoding='utf-8-sig')
    
    return team_explosiveness, opposition_explosiveness, player_explosiveness, player_efficiency

# Streamlit UI
st.title('Football Analysis Dashboard')

# Let users select a league and season
league = st.sidebar.selectbox('Select League', ['Premier League'])  # Add other leagues to the list as needed
season = st.sidebar.selectbox('Select Season', ['2023/24', '2022/23'])  # Add other seasons to the list as needed

# Load the data for the selected league and season
team_explosiveness, opposition_explosiveness, player_explosiveness, player_efficiency = load_data(league, season)

# Display horizontal bar chart for team explosiveness
st.header('Team Explosiveness')

# Create a horizontal bar chart with team names on the y-axis and explosiveness values on the x-axis
st.bar_chart(team_explosiveness.set_index('Team Name')['Explosiveness'], use_container_width=True)

# Display last updated date and time
st.text(f'Last updated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')



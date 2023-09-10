import streamlit as st
import pandas as pd
import os

# Base directory where the CSV files are stored. 
# This assumes that the data folders are in the same directory as your script.
base_dir = os.path.dirname(__file__)

# Function to load data for a selected league and season
def load_data(league, season):
    # Construct the season directory using a relative path
    season_dir = os.path.join(base_dir, 'Explosiveness Seasons', f'{league.replace(" ", "_")}_{season.replace("/", "_")}')
    team_explosiveness = pd.read_csv(os.path.join(season_dir, 'Team_Explosiveness.csv'), encoding='utf-8-sig')
    opposition_explosiveness = pd.read_csv(os.path.join(season_dir, 'Opposition_Explosiveness.csv'), encoding='utf-8-sig')
    player_explosiveness = pd.read_csv(os.path.join(season_dir, 'Player_Explosiveness.csv'), encoding='utf-8-sig')
    player_efficiency = pd.read_csv(os.path.join(season_dir, 'Player_Efficiency.csv'), encoding='utf-8-sig')
    return team_explosiveness, opposition_explosiveness, player_explosiveness, player_efficiency

# Streamlit UI
st.title('Football Analysis Dashboard')

# Let users select a league and season
league = st.sidebar.selectbox('Select League', ['Premier League'])  # Add other leagues to the list as needed
season = st.sidebar.selectbox('Select Season', ['2023/24', '2022/23'])  # Add other seasons to the list as needed

# Load the data for the selected league and season
team_explosiveness, opposition_explosiveness, player_explosiveness, player_efficiency = load_data(league, season)

# Display data and visualizations
st.header('Team Explosiveness')
st.write(team_explosiveness)

# ... (add more Streamlit elements to display other data and create visualizations)

import streamlit as st
import pandas as pd
import os
from datetime import datetime

# Base directory where the CSV files are stored.
base_dir = os.path.abspath(os.path.dirname(__file__))

def load_data(league, season):
    base_url = "https://raw.githubusercontent.com/NathanLever7/Football_Explosiveness_Dashboard/main/"
    season_dir = f'{league.replace(" ", "_")}_{season.replace("/", "_")}/'
    
    # Load data from GitHub using raw file URLs
    team_explosiveness_url = f"{base_url}{season_dir}Team_Explosiveness.csv"
    
    # Debugging: Check the URL
    st.write(f'Team explosiveness URL: {team_explosiveness_url}')
    
    # Fetch data using requests
    team_explosiveness = pd.read_csv(team_explosiveness_url, encoding='utf-8-sig')
    
    # Debugging: Display the DataFrame
    st.write('Team explosiveness DataFrame:', team_explosiveness)
    
    return team_explosiveness

# Streamlit UI
st.title('Football Analysis Dashboard')

# Let users select a league and season
league = st.sidebar.selectbox('Select League', ['Premier League'])
season = st.sidebar.selectbox('Select Season', ['2023/24', '2022/23'])

# Load the data for the selected league and season
team_explosiveness = load_data(league, season)

# Debugging: Check the columns of the DataFrame
st.write('Columns:', team_explosiveness.columns)

# Display last updated date and time
st.text(f'Last updated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')




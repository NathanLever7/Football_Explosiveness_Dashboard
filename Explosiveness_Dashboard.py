import streamlit as st
import pandas as pd
import os
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib import colors

# Base directory where the CSV files are stored.
base_dir = os.path.abspath(os.path.dirname(__file__))

def load_data(league, season, data_type):
    base_url = "https://raw.githubusercontent.com/NathanLever7/Football_Explosiveness_Dashboard/main/"
    season_dir = f'{league.replace(" ", "_")}_{season.replace("/", "_")}/'
    
    data_url = f"{base_url}{season_dir}{data_type}.csv"
    
    data_df = pd.read_csv(data_url, encoding='utf-8-sig')
    
    return data_df

# Streamlit UI
st.title('Football Analysis Dashboard')

# Let users select a league and season
league = st.sidebar.selectbox('Select League', ['Premier League'])  
season = st.sidebar.selectbox('Select Season', ['2023/24', '2022/23'])  

# Load the data for the selected league and season
team_explosiveness = load_data(league, season, "Team_Explosiveness")
opposition_explosiveness = load_data(league, season, "Opposition_Explosiveness")

# Plot Team Explosiveness data
st.subheader('Team Explosiveness Data')
norm = colors.Normalize(vmin=team_explosiveness['Team Explosiveness Index'].min(), vmax=team_explosiveness['Team Explosiveness Index'].max())
cmap = plt.cm.get_cmap("coolwarm")
color_values = cmap(norm(team_explosiveness['Team Explosiveness Index'].values))

plt.figure(figsize=(12, 8))
plt.barh(team_explosiveness['Squad'], team_explosiveness['Team Explosiveness Index'], color=color_values)
plt.xlabel('Team Explosiveness Index')
plt.ylabel('Team')
plt.title(f'Team Explosiveness Index {league} {season}')
plt.gca().invert_yaxis()
st.pyplot(plt.gcf())

# Plot Opposition Explosiveness data
st.subheader('Opposition Explosiveness Data')
norm = colors.Normalize(vmin=opposition_explosiveness['Team Explosiveness Index'].min(), vmax=opposition_explosiveness['Team Explosiveness Index'].max())
cmap = plt.cm.get_cmap("coolwarm_r")  # Reversed colormap
color_values = cmap(norm(opposition_explosiveness['Team Explosiveness Index'].values))

plt.figure(figsize=(12, 8))
plt.barh(opposition_explosiveness['Squad'], opposition_explosiveness['Team Explosiveness Index'], color=color_values)
plt.xlabel('Team Explosiveness Index')
plt.ylabel('Team')
plt.title(f'Opposition Explosiveness Index {league} {season}')
plt.gca().invert_yaxis()
st.pyplot(plt.gcf())

# Load and display Player Explosiveness data
player_explosiveness_data = load_data(league, season, "Player_Explosiveness")
st.subheader('Player Explosiveness Data')
st.dataframe(player_explosiveness_data)

# Load and display Player Efficiency data
player_efficiency_data = load_data(league, season, "Player_Efficiency")
st.subheader('Player Efficiency Data')
st.dataframe(player_efficiency_data)

st.text(f'Last updated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')

st.write("Explanation: All xG is not made equal. For example, we take 2 players in a match, players A and B. Let's say A has 1 shot of 1 xG, and B has 10 shots of 0.1 xG. Both have an xG of 1. However, the chances that both score 1 goal are different. A is guaranteed to score 1 goal, but B could score anywhere between 0-10 goals. The aim of these metrics are to find which players belong to which category. Players who take many shots, and have a high npxG per 90 tend will have high explosiveness - they have the opportunity to score many goals, and teh high number of shots makes their actual goals scored variable. In contrast, players with high consistency are rewarded for both their npxG per 90, and their average chance being higher quality. In both cases, we expect players to score highly to score goals often. Explosive players are more likley to have greater variance in goals per game than consistent players.")

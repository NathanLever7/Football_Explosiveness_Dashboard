import streamlit as st
import pandas as pd
import os
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np

# Base directory where the CSV files are stored.
base_dir = os.path.abspath(os.path.dirname(__file__))

def load_data(league, season, data_type):
    base_url = "https://raw.githubusercontent.com/NathanLever7/Football_Explosiveness_Dashboard/main/"
    season_dir = f'{league.replace(" ", "_")}_{season.replace("/", "_")}/'
    
    data_url = f"{base_url}{season_dir}{data_type}.csv"
    
    data_df = pd.read_csv(data_url, encoding='utf-8-sig')
    
    return data_df

league = 'Premier League'
seasons = ['2023/24', '2022/23']
all_season_data_explosiveness = pd.concat([load_data(league, season, "Team_Explosiveness") for season in seasons])
all_season_data_consistency = pd.concat([load_data(league, season, "Team_Consistency") for season in seasons])


all_season_player_explosiveness_data = pd.concat([load_data(league, season, "Player_Explosiveness") for season in seasons])
all_season_player_consistency_data = pd.concat([load_data(league, season, "Player_Consistency") for season in seasons])

# Streamlit UI
st.title('Explosiveness vs Consistency')

st.write("Skip to the bottom for metric explanation")

# Let users select a league and season
league = st.sidebar.selectbox('Select League', ['Premier League'])  
season = st.sidebar.selectbox('Select Season', ['2023/24', '2022/23'])  

# Load the data for the selected league and season
player_explosiveness_data = load_data(league, season, "Player_Explosiveness")
player_consistency_data = load_data(league, season, "Player_Consistency")
team_explosiveness = load_data(league, season, "Team_Explosiveness")
opposition_explosiveness = load_data(league, season, "Opposition_Explosiveness")
team_consistency = load_data(league, season, "Team_Consistency")
opposition_consistency = load_data(league, season, "Opposition_Consistency")

# Display Player Explosiveness data
st.subheader('Player Explosiveness Data')
st.dataframe(player_explosiveness_data)

# Display Player Consistency data
st.subheader('Player Consistency Data')
st.dataframe(player_consistency_data)


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

# Plot Team Consistency data
st.subheader('Team Consistency Data')
norm = colors.Normalize(vmin=team_consistency['Team Consistency Index'].min(), vmax=team_consistency['Team Consistency Index'].max())
cmap = plt.cm.get_cmap("coolwarm")
color_values = cmap(norm(team_consistency['Team Consistency Index'].values))

plt.figure(figsize=(12, 8))
plt.barh(team_consistency['Squad'], team_consistency['Team Consistency Index'], color=color_values)
plt.xlabel('Team Consistency Index')
plt.ylabel('Team')
plt.title(f'Team Consistency Index {league} {season}')
plt.gca().invert_yaxis()
st.pyplot(plt.gcf())

# Plot Opposition Consistency data
st.subheader('Opposition Consistency Data')
norm = colors.Normalize(vmin=opposition_consistency['Team Consistency Index'].min(), vmax=opposition_consistency['Team Consistency Index'].max())
cmap = plt.cm.get_cmap("coolwarm_r")  # Reversed colormap for the opposition data
color_values = cmap(norm(opposition_consistency['Team Consistency Index'].values))

plt.figure(figsize=(12, 8))
plt.barh(opposition_consistency['Squad'], opposition_consistency['Team Consistency Index'], color=color_values)
plt.xlabel('Team Consistency Index')
plt.ylabel('Team')
plt.title(f'Opposition Consistency Index {league} {season}')
plt.gca().invert_yaxis()
st.pyplot(plt.gcf())




# Merging data for teams
team_data = team_explosiveness.merge(team_consistency, on='Squad', suffixes=('_Explosiveness', '_Consistency'))

# Merging data for opposition
opposition_data = opposition_explosiveness.merge(opposition_consistency, on='Squad', suffixes=('_Explosiveness', '_Consistency'))

# Plot Team Explosiveness vs Consistency
st.subheader('Team Explosiveness vs Consistency')
plt.figure(figsize=(12, 8))
plt.scatter(team_data['Team Explosiveness Index'], team_data['Team Consistency Index'], c='blue')
plt.xlabel('Team Explosiveness Index')
plt.ylabel('Team Consistency Index')
plt.title(f'Team Explosiveness vs Consistency {league} {season}')
for i, team in enumerate(team_data['Squad']):
    plt.annotate(team, (team_data['Team Explosiveness Index'][i], team_data['Team Consistency Index'][i]), fontsize=8, alpha=0.7)
st.pyplot(plt.gcf())

# Plot Opposition Explosvieness vs Consistency
st.subheader('Opposition Explosiveness vs Consistency')
plt.figure(figsize=(12, 8))
plt.scatter(opposition_data['Team Explosiveness Index'], opposition_data['Team Consistency Index'], c='red')
plt.xlabel('Opposition Explosiveness Index')
plt.ylabel('Opposition Consistency Index')
plt.title(f'Opposition Explosiveness vs Consistency {league} {season}')
for i, team in enumerate(opposition_data['Squad']):
    plt.annotate(team, (opposition_data['Team Explosiveness Index'][i], opposition_data['Team Consistency Index'][i]), fontsize=8, alpha=0.7)
st.pyplot(plt.gcf())


player_explosiveness_data = load_data(league, season, "Player_Explosiveness")
player_consistency_data = load_data(league, season, "Player_Consistency")

# Create a new variable to merge the player data for the selected season only
selected_season_player_data = player_explosiveness_data.merge(player_consistency_data, on='Player', suffixes=('_Explosiveness', '_Consistency'))

max_explosiveness = player_explosiveness_data['Explosiveness'].max() * 1.1
max_consistency = player_consistency_data['Consistency'].max() * 1.1

# Plot Player Explosiveness vs Consistency
st.subheader('Player Explosiveness vs Consistency')
plt.figure(figsize=(12, 8))
plt.scatter(selected_season_player_data['Explosiveness'], selected_season_player_data['Consistency'], c='purple')
plt.xlabel('Player Explosiveness Index')
plt.ylabel('Player Consistency Index')
plt.xlim(0, max_explosiveness)
plt.ylim(0, max_consistency)
plt.title(f'Player Explosiveness vs Consistency {league} {season}')
for i, player in enumerate(selected_season_player_data['Player']):
    plt.annotate(player, (selected_season_player_data['Explosiveness'][i], selected_season_player_data['Consistency'][i]), fontsize=8, alpha=0.7)
st.pyplot(plt.gcf())
 
st.text(f'Last updated: 02/11/2023 12:15')







st.markdown("""**Player Explanation:**

Not all xG is made equal.

Let's take 2 players in a match, players A and B. Let's say A has 1 shot of 1 xG, and B has 10 shots of 0.1 xG. Both have an xG of 1. However, the chances that both score 1 goal are different. A is guaranteed to score 1 goal, but B could score anywhere between 0-10 goals.

The aim of these metrics are to find which players belong to which category.

Players who take many shots, and have a high npxG per 90 tend will have high explosiveness - they have the opportunity to score many goals, and the high number of shots makes their actual goals scored variable. In contrast, players with high consistency are rewarded for both their npxG per 90, and their average chance being higher quality.

In both cases, we expect players that score highly, to score goals often. Explosive players are more likely to have greater variance in goals per game than consistent players.""")


st.markdown("""**Team Explanation:**

Team explosiveness orders the teams who take a lot of shots and generate high xG. They are the teams likely to score many goals in a given game, but outcome can be quite variable.

In contrast, the opposition data shows the teams that concede a lot of shots, and high xG. They are the teams likely to concede many goals in a given game, but again, how many goals can be more variable.

In terms of consistency, teams high up create a high number of good chances, they should score a less variable amount of goals than those at the top of the explosiveness rankings.

The opposition data shows teams that should have conceded a more stable amount of goals that those at the top of the explosiveness opposition metric""")



st.markdown("""**Key Definitions:**

xG = Expected Goals

np = Non-penalty

Sh = Shots""")


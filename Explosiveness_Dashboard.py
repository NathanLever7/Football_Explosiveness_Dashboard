import streamlit as st
import pandas as pd
import os
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
from sklearn.linear_model import LinearRegression

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
all_season_data_efficiency = pd.concat([load_data(league, season, "Team_Efficiency") for season in seasons])

# Linear regression for trendline calculation
lr_team = LinearRegression()
lr_team.fit(all_season_data_explosiveness['Team Explosiveness Index'].values.reshape(-1,1), 
            all_season_data_efficiency['Team Efficiency Index'].values.reshape(-1,1))
team_slope = lr_team.coef_[0]
team_intercept = lr_team.intercept_

all_season_player_explosiveness_data = pd.concat([load_data(league, season, "Player_Explosiveness") for season in seasons])
all_season_player_consistency_data = pd.concat([load_data(league, season, "Player_Efficiency") for season in seasons])

# Linear regression for trendline calculation
lr_player = LinearRegression()
lr_player.fit(all_season_player_explosiveness_data['Explosiveness'].values.reshape(-1,1), 
              all_season_player_consistency_data['Efficiency'].values.reshape(-1,1))
player_slope = lr_player.coef_[0]
player_intercept = lr_player.intercept_

# Streamlit UI
st.title('Explosiveness vs Consistency')

st.write("Skip to the bottom for metric explanation")

# Let users select a league and season
league = st.sidebar.selectbox('Select League', ['Premier League'])  
season = st.sidebar.selectbox('Select Season', ['2023/24', '2022/23'])  

# Load the data for the selected league and season
player_explosiveness_data = load_data(league, season, "Player_Explosiveness")
player_consistency_data = load_data(league, season, "Player_Efficiency")
team_explosiveness = load_data(league, season, "Team_Explosiveness")
opposition_explosiveness = load_data(league, season, "Opposition_Explosiveness")
team_consistency = load_data(league, season, "Team_Efficiency")
opposition_consistency = load_data(league, season, "Opposition_Efficiency")

# Display Player Explosiveness data
st.subheader('Player Explosiveness Data')
st.dataframe(player_explosiveness_data)

# Display Player Efficiency data
st.subheader('Player Consistency Data')
st.dataframe(player_consistency_data)

# Plot Team Explosiveness data
st.subheader('Team Explosiveness Data')
norm = colors.Normalize(vmin=team_explosiveness['Team Explosiveness Index'].min(), vmax=team_explosiveness['Team Explosiveness Index'].max())
cmap = plt.cm.get_cmap("coolwarm")
color_values = cmap(norm(team_explosiveness['Team Explosiveness Index'].values))

fig, ax = plt.subplots()
ax.scatter(team_explosiveness['Team Explosiveness Index'], team_consistency['Team Efficiency Index'], color=color_values)
ax.plot(team_explosiveness['Team Explosiveness Index'], team_slope*team_explosiveness['Team Explosiveness Index'] + team_intercept, color='red')
ax.set_xlabel('Team Explosiveness Index')
ax.set_ylabel('Team Efficiency Index')
st.pyplot(fig)

# Display Opposition Explosiveness data
st.subheader('Opposition Explosiveness Data')
st.dataframe(opposition_explosiveness)

# Display Opposition Efficiency data
st.subheader('Opposition Efficiency Data')
st.dataframe(opposition_consistency)

# Explanation of Metrics
st.subheader('Explanation of Metrics')

st.write('''
### Explosiveness
The Explosiveness metric is a measure of how explosive a player or team's actions are on average throughout a match. It is calculated based on various statistics such as the number of shots taken, the number of dribbles attempted, etc.

### Consistency
The Consistency metric is a measure of how consistently a player or team performs over time. It is calculated based on various statistics such as the standard deviation of the performance metrics over a number of matches.

### Efficiency
The Efficiency metric is a measure of how efficiently a player or team uses their opportunities to score goals. It is calculated based on various statistics such as the conversion rate of shots to goals.

#### Note
The scatter plot above shows the relationship between the Team Explosiveness Index and the Team Efficiency Index. The trendline in red indicates the general trend in the data, with the slope of the trendline indicating the strength of the relationship between the two metrics. 
''')

# The above description might need adjustments based on the exact calculations for your metrics.

if __name__ == "__main__":
    st.write("This streamlit app is running")



st.text(f'Last updated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')







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


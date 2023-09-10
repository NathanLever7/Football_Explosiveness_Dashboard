import streamlit as st
import pandas as pd
import os
from datetime import datetime
import requests
import numpy as np
import matplotlib.pyplot as plt

# Base directory where the CSV files are stored.
# This assumes that the data folders are in the same directory as your script.
base_dir = os.path.abspath(os.path.dirname(__file__))

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

# Create your matplotlib figure and plot your data
arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

# Set the x-axis range to be between 0 and 50
ax.set_xlim(0, 50)

# Display the chart using st.pyplot()
st.pyplot(fig)

# Display last updated date and time
st.text(f'Last updated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
With the addition of ax.set_xlim(0, 50), the x-axis of your histogram will be limited to the range between 0 and 50. You can adjust the values in ax.set_xlim() to fit your desired range.




User
No No No. It was fine before just except the axis wasnt consistent, it was like 0.5 then 20, then 7 based on the score of each team. I want all the teams to be on the same, horizontal x axis. Do you get me
ChatGPT
I understand now. You want to ensure that all teams have the same horizontal x-axis range for consistency. To achieve this, you can set a fixed range for the x-axis that accommodates all possible values. Here's how you can modify your code to achieve this:

python
Copy code
import streamlit as st
import pandas as pd
import os
from datetime import datetime
import requests
import numpy as np
import matplotlib.pyplot as plt

# Base directory where the CSV files are stored.
# This assumes that the data folders are in the same directory as your script.
base_dir = os.path.abspath(os.path.dirname(__file__))

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

# Create your matplotlib figure and plot your data
arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20, range=(0, 50))  # Set a fixed range for the x-axis

# Display the chart using st.pyplot()
st.pyplot(fig)

# Display last updated date and time
st.text(f'Last updated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
In the modified code, I added range=(0, 50) to the ax.hist() function, which sets a fixed range for the x-axis between 0 and 50. This ensures that all teams are displayed on the same horizontal x-axis with consistent tick marks. You can adjust the range as needed to fit your data.






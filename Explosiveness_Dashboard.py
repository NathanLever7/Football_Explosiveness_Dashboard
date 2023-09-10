import streamlit as st
import pandas as pd
import os
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib import colors

# Base directory where the CSV files are stored.
# This assumes that the data folders are in the same directory as your script.
base_dir = os.path.abspath(os.path.dirname(__file__))

def load_data(league, season, analysis_type):
    base_url = "https://raw.githubusercontent.com/NathanLever7/Football_Explosiveness_Dashboard/main/"
    season_dir = f'{league.replace(" ", "_")}_{season.replace("/", "_")}/'
    
    # Load data from GitHub using raw file URLs
    explosiveness_url = f"{base_url}{season_dir}{analysis_type}_Explosiveness.csv"
    
    # Explicitly set column names when reading the CSV
    explosiveness_data = pd.read_csv(
        explosiveness_url,
        encoding='utf-8-sig',
        names=['Squad', f'{analysis_type} Explosiveness Index']  # Replace with actual column names
    )
    explosiveness_data[f'{analysis_type} Explosiveness Index'] = pd.to_numeric(explosiveness_data[f'{analysis_type} Explosiveness Index'], errors='coerce')
    return explosiveness_data

def plot_data(explosiveness_data, league, season, analysis_type):
    # Remove the first row from the DataFrame
    explosiveness_data = explosiveness_data.iloc[1:]

    # Convert 'Explosiveness Index' to numeric
    explosiveness_data[f'{analysis_type} Explosiveness Index'] = pd.to_numeric(explosiveness_data[f'{analysis_type} Explosiveness Index'], errors='coerce')

    # Create a colormap
    norm = colors.Normalize(vmin=explosiveness_data[f'{analysis_type} Explosiveness Index'].min(), vmax=explosiveness_data[f'{analysis_type} Explosiveness Index'].max())
    cmap = plt.cm.get_cmap("coolwarm")
    color_values = cmap(norm(explosiveness_data[f'{analysis_type} Explosiveness Index'].values))

    plt.figure(figsize=(12, 8))
    plt.barh(explosiveness_data['Squad'], explosiveness_data[f'{analysis_type} Explosiveness Index'], color=color_values)
    plt.xlabel(f'{analysis_type} Explosiveness Index')
    plt.ylabel('Team')
    plt.title(f'{analysis_type} Explosiveness Index {league} {season}')
    plt.gca().invert_yaxis()

    # Display the plot in the Streamlit application
    st.pyplot(plt.gcf())

# Streamlit UI
st.title('Football Analysis Dashboard')

# Let users select a league and season
league = st.sidebar.selectbox('Select League', ['Premier League'])  # Add other leagues to the list as needed
season = st.sidebar.selectbox('Select Season', ['2023/24', '2022/23'])  # Add other seasons to the list as needed

# Now, call your functions with the defined league and season variables
team_data = load_data(league, season, "Team")
plot_data(team_data, league, season, "Team")

opposition_data = load_data(league, season, "Opposition")
plot_data(opposition_data, league, season, "Opposition")

st.text(f'Last updated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')


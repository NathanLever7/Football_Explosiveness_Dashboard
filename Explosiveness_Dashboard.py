def load_data(league, season, analysis_type):
    base_url = "https://raw.githubusercontent.com/NathanLever7/Football_Explosiveness_Dashboard/main/"
    season_dir = f'{league.replace(" ", "_")}_{season.replace("/", "_")}/'
    
    # Load data from GitHub using raw file URLs
    explosiveness_url = f"{base_url}{season_dir}{analysis_type}_Explosiveness.csv"
    
    # Explicitly set column names when reading the CSV
    explosiveness_data = pd.read_csv(
        explosiveness_url,
        encoding='utf-8-sig',
        names=['Squad', 'Team Explosiveness Index']  # Replace with actual column names
    )
    explosiveness_data['Team Explosiveness Index'] = pd.to_numeric(explosiveness_data['Team Explosiveness Index'], errors='coerce')
    return explosiveness_data

def plot_data(team_explosiveness, league, season, analysis_type):
    # Convert 'Team Explosiveness Index' to numeric
    team_explosiveness['Team Explosiveness Index'] = pd.to_numeric(team_explosiveness['Team Explosiveness Index'], errors='coerce')

    # Create a colormap
    norm = colors.Normalize(vmin=team_explosiveness['Team Explosiveness Index'].min(), vmax=team_explosiveness['Team Explosiveness Index'].max())
    cmap = plt.cm.get_cmap("coolwarm")
    color_values = cmap(norm(team_explosiveness['Team Explosiveness Index'].values))

    plt.figure(figsize=(12, 8))
    plt.barh(team_explosiveness['Squad'], team_explosiveness['Team Explosiveness Index'], color=color_values)
    plt.xlabel('Team Explosiveness Index')
    plt.ylabel('Team')
    plt.title(f'{analysis_type} Explosiveness Index {league} {season}')
    plt.gca().invert_yaxis()

    # Display the plot in the Streamlit application
    st.pyplot(plt.gcf())

# In your main part of the script, you would call these functions like this:

# Load and plot team data
team_data = load_data(league, season, "Team")
plot_data(team_data.iloc[1:], league, season, "Team")

# Load and plot opposition data
opposition_data = load_data(league, season, "Opposition")
plot_data(opposition_data.iloc[1:], league, season, "Opposition")

st.text(f'Last updated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')


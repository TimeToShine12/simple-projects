import streamlit as st
from utils import load_data, file_load


st.title('NHL players stats')

st.markdown("""
App to scrap players stats
* **Python: streamlit, pandas, request**
* **Data source: https://www.hockey-reference.com/**
""")

# sidebar for year which we will use to load data from URL
st.sidebar.header('Input Information')
selected_season = st.sidebar.selectbox('Season', list(reversed(range(2000, 2025))))

# load our dataframe from url request
stats = load_data(selected_season)

# sidebars for teams filter
unique_team = stats.Tm.unique()
selected_teams = st.sidebar.multiselect('Teams', unique_team, unique_team[:3])

# sidebar for players filter
unique_name = stats.Player.unique()
selected_players = st.sidebar.multiselect('Players', unique_name, unique_name[:2])

df_selected_team = stats
st.header('Display Player Stats')
st.write('Data Dimension: ' + str(df_selected_team.shape[0]) + ' rows and ' + str(df_selected_team.shape[1]) + ' columns.')


# filtering dataframe
if not selected_players and selected_teams:
    df_selected_team = stats[stats.Tm.isin(selected_teams)]
    st.dataframe(df_selected_team)
elif not selected_teams and selected_players:
    df_selected_team = stats[stats.Player.isin(selected_players)]
    st.dataframe(df_selected_team)
elif selected_teams and selected_players:
    df_selected_team = stats[(stats.Tm.isin(selected_teams)) & (stats.Player.isin(selected_players))]
    st.dataframe(df_selected_team)
elif not selected_teams and not selected_players:
    st.dataframe(df_selected_team)

# save dataframe as scv file
st.markdown(file_load(df_selected_team), unsafe_allow_html=True)

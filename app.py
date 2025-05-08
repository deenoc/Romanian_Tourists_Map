import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static

# Set page config
st.set_page_config(page_title="Romanian Tourist Map", layout="wide")

# Title
st.title("🗺️ Romanian Tourist Attractions Map")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("romania_attractions.csv")

df = load_data()

# Sidebar filters (optional)
st.sidebar.header("Filter Options")
regions = st.sidebar.multiselect("Select Region(s)", df['region'].unique(), default=df['region'].unique())

# Filtered DataFrame
filtered_df = df[df['region'].isin(regions)]

# Map setup
m = folium.Map(location=[45.9432, 24.9668], zoom_start=6)

# Add markers
for _, row in filtered_df.iterrows():
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        popup=f"<b>{row['name']}</b><br>{row['description']}",
        tooltip=row['name'],
        icon=folium.Icon(color="green", icon="info-sign")
    ).add_to(m)

# Show map
folium_static(m, width=1200, height=600)

# Optional: Show data table
with st.expander("See the full dataset"):
    st.dataframe(filtered_df)

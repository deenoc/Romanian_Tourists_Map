import streamlit as st
import folium
from streamlit_folium import folium_static

# Set Streamlit config
st.set_page_config(page_title="Romanian Tourist Map", layout="wide")
st.title("🗺️ Romanian Tourist Attractions Map")

# Hardcoded data (from Colab)
locations = [
    {
        "name": "Bran Castle",
        "lat": 45.5156,
        "lon": 25.3672,
        "region": "Brașov",
        "description": "Commonly known as Dracula's Castle."
    },
    {
        "name": "Peleș Castle",
        "lat": 45.3592,
        "lon": 25.5424,
        "region": "Prahova",
        "description": "A Neo-Renaissance castle in the Carpathian Mountains."
    },
    {
        "name": "Merry Cemetery",
        "lat": 47.9736,
        "lon": 23.6952,
        "region": "Maramureș",
        "description": "Famous for colorful tombstones with poetic epitaphs."
    },
    {
        "name": "Corvin Castle",
        "lat": 45.7489,
        "lon": 22.8886,
        "region": "Hunedoara",
        "description": "One of the largest castles in Europe, Gothic-Renaissance style."
    }
]

# Sidebar region filter
regions = list(set(loc["region"] for loc in locations))
selected_regions = st.sidebar.multiselect("Filter by Region", regions, default=regions)

# Filtered locations
filtered = [loc for loc in locations if loc["region"] in selected_regions]

# Create map
m = folium.Map(location=[45.9432, 24.9668], zoom_start=6)
for loc in filtered:
    folium.Marker(
        location=[loc["lat"], loc["lon"]],
        popup=f"<b>{loc['name']}</b><br>{loc['description']}",
        tooltip=loc["name"],
        icon=folium.Icon(color="green", icon="info-sign")
    ).add_to(m)

# Show map
folium_static(m, width=1200, height=600)

# Optional: Show raw data
with st.expander("Show Data"):
    st.write(filtered)

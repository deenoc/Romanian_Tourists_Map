import streamlit as st
import folium
from streamlit_folium import folium_static

# Page config and title
st.set_page_config(page_title="Romanian Tourist Cities Map", layout="wide")
st.title("🇷🇴 Romanian Tourist Cities Map")

# City data
locations = [
    {"name": "Bucharest", "lat": 44.4268, "lon": 26.1025, "rank": 1, "visitors": 2000000},
    {"name": "Brașov", "lat": 45.6579, "lon": 25.6012, "rank": 2, "visitors": 1500000},
    {"name": "Constanța", "lat": 44.1733, "lon": 28.6383, "rank": 3, "visitors": 1200000},
    {"name": "Sibiu", "lat": 45.7983, "lon": 24.1256, "rank": 4, "visitors": 1100000},
    {"name": "Cluj-Napoca", "lat": 46.7712, "lon": 23.6236, "rank": 5, "visitors": 1000000},
    {"name": "Iași", "lat": 47.1585, "lon": 27.6014, "rank": 6, "visitors": 900000},
    {"name": "Timișoara", "lat": 45.7489, "lon": 21.2087, "rank": 7, "visitors": 850000},
    {"name": "Oradea", "lat": 47.0465, "lon": 21.9189, "rank": 8, "visitors": 800000},
    {"name": "Suceava", "lat": 47.6514, "lon": 26.2556, "rank": 9, "visitors": 750000},
    {"name": "Sinaia", "lat": 45.3501, "lon": 25.5504, "rank": 10, "visitors": 700000},
    {"name": "Alba Iulia", "lat": 46.0741, "lon": 23.5781, "rank": 11, "visitors": 650000},
    {"name": "Târgu Mureș", "lat": 46.5425, "lon": 24.5575, "rank": 12, "visitors": 600000},
    {"name": "Baia Mare", "lat": 47.6573, "lon": 23.5681, "rank": 13, "visitors": 550000},
    {"name": "Arad", "lat": 46.1866, "lon": 21.3123, "rank": 14, "visitors": 500000},
    {"name": "Piatra Neamț", "lat": 46.9275, "lon": 26.3731, "rank": 15, "visitors": 450000},
    {"name": "Bistrița", "lat": 47.1351, "lon": 24.5002, "rank": 16, "visitors": 400000},
    {"name": "Râmnicu Vâlcea", "lat": 45.0997, "lon": 24.3693, "rank": 17, "visitors": 350000},
    {"name": "Craiova", "lat": 44.3302, "lon": 23.7949, "rank": 18, "visitors": 300000},
    {"name": "Deva", "lat": 45.8763, "lon": 22.9117, "rank": 19, "visitors": 250000},
    {"name": "Tulcea", "lat": 45.1716, "lon": 28.7918, "rank": 20, "visitors": 200000},
]

# Define marker color by rank
def get_marker_color(rank):
    if rank <= 5:
        return "red"
    elif rank <= 10:
        return "blue"
    elif rank <= 15:
        return "purple"
    else:
        return "green"

# Create folium map
m = folium.Map(location=[45.9432, 24.9668], zoom_start=6)

for loc in locations:
    folium.Marker(
        location=[loc["lat"], loc["lon"]],
        popup=f"<b>{loc['name']}</b><br>Rank: {loc['rank']}<br>Visitors: {loc['visitors']:,}",
        tooltip=loc["name"],
        icon=folium.Icon(color=get_marker_color(loc["rank"]), icon="info-sign")
    ).add_to(m)

# Layout: map on the left, legend on the right
col1, col2 = st.columns([4, 1])

with col1:
    folium_static(m, width=1000, height=600)

with col2:
    st.markdown("### 🗺️ Legend")
    st.markdown("""
    <div style="line-height: 1.6; font-size: 16px;">
        <span style='color:red;'>🔴</span> <b>Rank 1–5</b><br>
        <span style='color:blue;'>🔵</span> <b>Rank 6–10</b><br>
        <span style='color:purple;'>🟣</span> <b>Rank 11–15</b><br>
        <span style='color:green;'>🟢</span> <b>Rank 16–20</b>
    </div>
    """, unsafe_allow_html=True)

# Optional: expandable data table
with st.expander("Show raw data"):
    st.write(locations)

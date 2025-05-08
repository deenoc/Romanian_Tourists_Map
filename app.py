import streamlit as st
import folium
from streamlit_folium import folium_static
from folium.plugins import HeatMap, FeatureGroupSubGroup

st.set_page_config(page_title="Romanian Tourist Cities Map", layout="wide")
st.title("🇷🇴 Romanian Tourist Cities Map")

# Extended city list with image URLs
locations = [
    {"name": "Bucharest", "lat": 44.4268, "lon": 26.1025, "rank": 1, "visitors": 2000000, "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Palatul_Parlamentului_Bucuresti.jpg/320px-Palatul_Parlamentului_Bucuresti.jpg"},
    {"name": "Brașov", "lat": 45.6579, "lon": 25.6012, "rank": 2, "visitors": 1500000, "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Brasov_-_panoramio_%283%29.jpg/320px-Brasov_-_panoramio_%283%29.jpg"},
    {"name": "Constanța", "lat": 44.1733, "lon": 28.6383, "rank": 3, "visitors": 1200000, "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/Cazino_Constanta.jpg/320px-Cazino_Constanta.jpg"},
    {"name": "Sibiu", "lat": 45.7983, "lon": 24.1256, "rank": 4, "visitors": 1100000, "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Sibiu_Romania_Piata_Mare.JPG/320px-Sibiu_Romania_Piata_Mare.JPG"},
    {"name": "Cluj-Napoca", "lat": 46.7712, "lon": 23.6236, "rank": 5, "visitors": 1000000, "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Piata_Unirii_Cluj-Napoca.jpg/320px-Piata_Unirii_Cluj-Napoca.jpg"},
    # (Add image_url for the remaining cities as needed)
]

# Get marker color based on rank
def get_marker_color(rank):
    if rank <= 5:
        return "red"
    elif rank <= 10:
        return "blue"
    elif rank <= 15:
        return "purple"
    else:
        return "green"

# Create base map
m = folium.Map(location=[45.9432, 24.9668], zoom_start=6)
layer_control = folium.map.LayerControl()

# Feature group for markers
marker_group = folium.FeatureGroup(name="City Markers", show=True).add_to(m)

# Add markers with image popups
for loc in locations:
    html_popup = f"""
    <div style="width:200px">
        <b>{loc['name']}</b><br>
        Rank: {loc['rank']}<br>
        Visitors: {loc['visitors']:,}<br>
        <img src="{loc['image_url']}" width="180">
    </div>
    """
    folium.Marker(
        location=[loc["lat"], loc["lon"]],
        popup=folium.Popup(html_popup, max_width=250),
        tooltip=loc["name"],
        icon=folium.Icon(color=get_marker_color(loc["rank"]), icon="info-sign")
    ).add_to(marker_group)

# Draw route between top 5 cities
top5 = sorted(locations, key=lambda x: x["rank"])[:5]
route_coords = [[city["lat"], city["lon"]] for city in top5]
folium.PolyLine(route_coords, color="orange", weight=4, tooltip="Top 5 Tourist Route").add_to(m)

# Heatmap layer
heat_data = [[loc["lat"], loc["lon"], loc["visitors"]] for loc in locations]
HeatMap(heat_data, name="Tourist Heatmap", radius=25, blur=15, max_zoom=6).add_to(m)

# Add layer control
folium.LayerControl(collapsed=False).add_to(m)

# Streamlit layout with legend
col1, col2 = st.columns([4, 1])
with col1:
    folium_static(m, width=1000, height=650)

with col2:
    st.markdown("### 🗺️ Legend")
    st.markdown("""
    <div style="line-height: 1.6; font-size: 16px;">
        <span style='color:red;'>🔴</span> <b>Rank 1–5</b><br>
        <span style='color:blue;'>🔵</span> <b>Rank 6–10</b><br>
        <span style='color:purple;'>🟣</span> <b>Rank 11–15</b><br>
        <span style='color:green;'>🟢</span> <b>Rank 16–20</b><br><br>
        <span style='color:orange;'>➖</span> <b>Top 5 Tourist Trail</b><br>
        <b>🔥 Heatmap</b> shows visitor density
    </div>
    """, unsafe_allow_html=True)

# Optional data table
with st.expander("Show city data"):
    st.write(locations)

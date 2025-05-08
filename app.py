import streamlit as st
import folium
from streamlit_folium import folium_static
from folium.plugins import HeatMap

st.set_page_config(page_title="Romanian Tourist Cities Map", layout="wide")
st.title("🇷🇴 Romanian Tourist Cities Map")

# City data
locations = [
    {"name": "Bucharest", "lat": 44.4268, "lon": 26.1025, "rank": 1, "visitors": 2000000,
     "image_url": "https://images.unsplash.com/photo-1583771797879-7e67c04fbd10?auto=format&fit=crop&w=600&q=80"},
    {"name": "Brașov", "lat": 45.6579, "lon": 25.6012, "rank": 2, "visitors": 1500000,
     "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Brasov_-_panoramio_%283%29.jpg/320px-Brasov_-_panoramio_%283%29.jpg"},
    {"name": "Constanța", "lat": 44.1733, "lon": 28.6383, "rank": 3, "visitors": 1200000,
     "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/Cazino_Constanta.jpg/320px-Cazino_Constanta.jpg"},
    {"name": "Sibiu", "lat": 45.7983, "lon": 24.1256, "rank": 4, "visitors": 1100000,
     "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Sibiu_Romania_Piata_Mare.JPG/320px-Sibiu_Romania_Piata_Mare.JPG"},
    {"name": "Cluj-Napoca", "lat": 46.7712, "lon": 23.6236, "rank": 5, "visitors": 1000000,
     "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Piata_Unirii_Cluj-Napoca.jpg/320px-Piata_Unirii_Cluj-Napoca.jpg"},
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

def get_marker_color(rank):
    if rank <= 5:
        return "red"
    elif rank <= 10:
        return "blue"
    elif rank <= 15:
        return "purple"
    else:
        return "green"

# Sidebar city selector
city_names = [loc["name"] for loc in locations]
selected_city = st.sidebar.selectbox("📍 Select a city", city_names)
selected_info = next(loc for loc in locations if loc["name"] == selected_city)

# Display city info (no image in sidebar)
st.sidebar.markdown(f"### {selected_info['name']}")
st.sidebar.markdown(f"**Rank**: {selected_info['rank']}")
st.sidebar.markdown(f"**Visitors**: {selected_info['visitors']:,}")

# Map
m = folium.Map(location=[45.9432, 24.9668], zoom_start=6)
marker_group = folium.FeatureGroup(name="City Markers", show=True).add_to(m)

for loc in locations:
    folium.Marker(
        location=[loc["lat"], loc["lon"]],
        tooltip=loc["name"],
        icon=folium.Icon(color=get_marker_color(loc["rank"]), icon="info-sign")
    ).add_to(marker_group)

heat_data = [[loc["lat"], loc["lon"], loc["visitors"]] for loc in locations]
HeatMap(heat_data, name="Tourist Heatmap", radius=25, blur=15, max_zoom=6).add_to(m)
folium.LayerControl(collapsed=False).add_to(m)

# Main map section
st.markdown("### 🗺️ Interactive Map")
folium_static(m, width=1100, height=600)

# City image and stats below map
st.markdown("---")
st.markdown(f"### 📸 {selected_info['name']} – Tourist Snapshot")
st.markdown(f"**Rank**: {selected_info['rank']} &nbsp;&nbsp;|&nbsp;&nbsp; **Visitors**: {selected_info['visitors']:,}")
if "image_url" in selected_info:
    st.image(selected_info["image_url"], use_container_width=True)

# Legend
st.markdown("---")
st.markdown("### 🗺️ Legend")
st.markdown("""
<div style="line-height: 1.6; font-size: 16px;">
    <span style='color:red;'>🔴</span> <b>Rank 1–5</b><br>
    <span style='color:blue;'>🔵</span> <b>Rank 6–10</b><br>
    <span style='color:purple;'>🟣</span> <b>Rank 11–15</b><br>
    <span style='color:green;'>🟢</span> <b>Rank 16–20</b><br><br>
    <b>🔥 Heatmap</b> shows visitor density
</div>
""", unsafe_allow_html=True)

# Raw data table
with st.expander("📊 View city data table"):
    st.write(locations)

###################################################
##      YSC2244 Programming for Data Science     ##
##                    #######                    ##
## Singapore Neighbourhood Recommendation System ##
##                Streamlit Script               ##
##               Scratch (Map Test)              ##
###################################################

# Authors: Elizabeth STEPTON, Sean LIM, Joshua VARGAS, NING Xinran
# UI code borrowed from Streamlit BERT Keyword Extractor sample https://github.com/streamlit/example-app-bert-keyword-extractor/blob/main/app.py
# Map code borrowed from Streamlit Uber pickup sample https://github.com/streamlit/demo-uber-nyc-pickups/blob/main/streamlit_app.py

### Import necessary packages ###

# Frontend frameworks
import streamlit as st

# Data processing
import pandas as pd
import geopandas as gpd

# Data visualisation
import seaborn as sns
import pydeck as pdk

### Streamlit setup ###

# Caching

# Page information
st.set_page_config(
    page_title="Singapore Neighbourhood Recommendation System",
    page_icon="🏡"
)

### Header ###
st.title("ProgData Map Test")

st_load_state = st.text('Loading...')
### Import functions code ###
import functions as fn

def map(data, lat, lon, zoom):
    data = data.to_crs(4326)
    st.write(
        pdk.Deck(
            map_style="mapbox://styles/mapbox/light-v9",
            initial_view_state={
                "latitude": lat,
                "longitude": lon,
                "zoom": zoom,
                "pitch": 50,
            },
            layers=[
                pdk.Layer(
                    "TextLayer",
                    data=(gpd.read_file('Generated Files/subzones_all_stats_with_travel_centroid.shp')).to_crs(4326),
                    get_position="geometry.coordinates",
                    get_size=16,
                    get_color=[50, 50, 50],
                    get_text="SUBZONE_N",
                ),
                pdk.Layer(
                    "GeoJsonLayer",
                    data=data,
                    get_position=["lon", "lat"],
                    radius=100,
                    elevation_scale=4,
                    elevation_range=[0, 1000],
                    pickable=True,
                    extruded=False,
                    stroked=True,
                    get_elevation="realpric-2",
                    get_fill_color="[200, 50, 50, 50]",
                    get_line_color=[100, 50, 50],
                    getLineWidth = 12,

                ),
            ],
        )
    )
st_load_state.text('')

### Streamlit layout ###

row2a, row2b = st.columns((1, 3))

with row2a:
    st.write("Controls column")

with row2b:
    st.write("Map and results column")
    map(fn.travel_time, 1.33, 103.8, 12)
    st.write(fn.travel_time)

st.header = ""

# About this app box (stolen from Streamlit sample)
with st.expander("ℹ️ - About this app", expanded=True):

    st.write(
        """     
-   Lorem ipsum
-   Dolor sit amet
	    """
    )

    st.markdown("")



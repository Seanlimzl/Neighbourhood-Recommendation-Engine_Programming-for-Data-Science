###################################################
##      YSC2244 Programming for Data Science     ##
##                    #######                    ##
## Singapore Neighbourhood Recommendation System ##
##                Streamlit Script               ##
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
#import seaborn as sns
import pydeck as pdk

### Streamlit setup ###

# Caching

# Page information
st.set_page_config(
    layout="wide",
    page_title="Singapore Neighbourhood Recommendation System",
    page_icon="🏡"
)

### Header ###
row1a, row1b = st.columns((2,2))
with row1a:
    st.title("🏡 Singapore Neighbourhood Recommendation System")
with row1b:
    st.write(
        """
    ##
    It can sometimes be hard to make a decision on where to live in Singapore, especially if you are buying a new or resale HDB.
    This tool aims to help you find a URA subzone within your income bracket that still has the amenities and characteristics you desire.
    This may be of help if you are comparing potential properties between neighbourhoods.
    """
    )

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

    st.markdown('## Filter')
    
    travel_slider = st.slider(
        'Travel Time to City Centre',
        min_value = 10,
        max_value = 80,
        value = 40,
        step = 10,
        help = 'What is the maximum travel time you are willing to endure between home and City Centre? (This assumes you will be using public transportation, including bus and MRT.)'
    )

    resale_slider = st.slider(
        'Resale Range',
        min_value = 90000,
        max_value = 710000,
        value = [150000,450000],
        step = 10000,
        help = 'What is the range of resale price that fits within your budget?'
    )

    st.markdown('## Amenities')
    st.markdown('#### Rate the importance of proximity to these amenities from 1 to 10')

    bus_slider = st.slider(
        'Bus Stops',
        min_value = 1,
        max_value = 10,
        value = 5,
        help = 'From 1-10, how important is it that you have many bus stops nearby?'
    )

    hawker_slider = st.slider(
        'Hawker Centres',
        min_value = 1,
        max_value = 10,
        value = 5,
        help = 'From 1-10, how important is it that you have many hawker centres nearby?'
    )

    malls_slider = st.slider(
        'Malls',
        min_value = 1,
        max_value = 10,
        value = 5,
        help = 'From 1-10, how important is it that your neighbourhood has many malls?'
    )

    mrt_slider = st.slider(
        'MRT Stations',
        min_value = 1,
        max_value = 10,
        value = 5,
        help = 'From 1-10, how important is it that you have more than 1 MRT station nearby?'
    )

    schools_slider = st.slider(
        'Schools',
        min_value = 1,
        max_value = 10,
        value = 5,
        help = 'From 1-10, how important is it that you have many schools nearby? This slider does NOT account for school type or programmes such as Integrated Programme, IB, etc.'
    )

    supermarket_slider = st.slider(
        'Supermarkets',
        min_value = 1,
        max_value = 10,
        value = 5,
        help = 'From 1-10, how important is it that you have many supermarkets nearby?'
    )


### Computation ###
slider_inputs = [bus_slider, hawker_slider, malls_slider, mrt_slider, schools_slider, supermarket_slider]
result_df = fn.our_algorithm(resale_slider, fn.get_tuples(slider_inputs), travel_slider)
result_gdf = gpd.GeoDataFrame(result_df)
result_clean = fn.clean_algorithm_results(result_df)

with row2b:
    map(result_gdf, 1.33, 103.8, 12)
    st.caption('Map of top 10 subzones given your filter parameters')
    #map(fn.travel_time, 1.33, 103.8, 12)
    #st.write(fn.clean_algorithm_results(result_gdf))
    st.markdown('## Top 10 Subzones for Your Needs')
    st.write(result_clean)

# About this app box (stolen from Streamlit sample)
with st.expander("ℹ️ - About This App", expanded=True):
    
    st.markdown('## Singapore Neighbourhood Recommendation System')
    st.write(
        """     
    This web app is produced by Elizabeth STEPTON, Sean LIM, Joshua VARGAS, and NING Xinran as part of the Yale-NUS College course YSC2244 Programming for Data Science.
    The aim of this project is to demonstrate proficiency in large dataset processing, geospatial data handling and visualisation, and front-end design.
	    """
    )

    st.markdown('#### Data sources')
    st.write(
        """     
    Geospatial and price data sources sources include:
    - data.gov.sg
    - Singapore Land Authority
    Transit time data is collected through API queries from Google. © Google 2022.
    In addition, OpenStreetMap data was used in matching different point datasets together, but is not present in this program. © OpenStreetMap contributors.
	    """
    )

    st.markdown('#### Libraries, frameworks, and IDE')
    st.write(
        """     
    This web app was built using Streamlit, based on a script written using VS Code and Anaconda.
    Packages used for geospatial data processing include pandas, geopandas, fiona, and the Python API for QGIS. The QGIS engine was used for large-scale geospatial data processing.
    Deck.gl was used for geospatial data visualisation using the Pydeck package, with mapping technology from Mapbox.
	    """
    )

    st.markdown('#### Licensing')
    st.write('Program code is provided under the Apache 2.0 license.')
    st.write('This does not cover the datasets. You are advised to download data directly from data.gov.sg instead of using the custom datasets processed for this program.')

    st.markdown("")



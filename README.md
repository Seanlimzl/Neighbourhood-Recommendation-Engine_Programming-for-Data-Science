# Singapore Neighbourhood Recommendation System
Yale-NUS College | YSC2244 Programming for Data Science
Elizabeth STEPTON, Joshua VARGAS, Sean LIM, NING Xinran

## About this project
This project aimed to help people find the best value neighbourhood in Singapore via a Streamlit app that lets users enter their own unique priorities across neighborhood features like amenities, nature, access to transport, and travel times. I lead data collection especially for travel time data, testing and integrating options like Google Maps, MapBox, OpenStreetMap, Singapore's own national mapping service OneMap, with a focus on balancing accuracy and cost. I learnt the intricacies of mapping services (routing, distance, time), bulk API querying, and how to work with geographic data in Python, GeoPandas.

## Dependencies
The Jupyter Notebook `Dependencies.ipynb` includes pip install commands for each of the dependencies. However, `fiona` requires a working installation of GDAL on the computer where the Python kernel is installed. GDAL is a translator library for geospatial data formats and can be downloaded [here](https://gdal.org).
GeoPandas and its dependencies:
<ul>
<li> fiona </li>
<li> pyproj </li>
<li> rtree </li>
<li> shapely </li>
<li> geopandas </li>
</ul>
GeoPandas SQL support:
<ul>
<li> psycopg2 </li>
<li> geoalchemy2 </li>
<li> geopy </li>
<li> pygeos </li>
</ul>
Geospatial data visualisation:
<ul>
<li> ipyleaflet </li>
<li> geos </li>
<li> pyshp </li>
<li> mapclassify </li>
<li> folium </li>
</ul>
Front-end implementation
<ul>
<li> Streamlit </li>
<li> Deck.gl / Pydeck </li>


## Folder Structure
Root: notebooks and scripts with data processing, EDA, and other tasks are stored in the root directory to simplify the management of file paths.  

`/Data Sources/`: Includes different data sources used in the project. Unfortunately some of these folders must be set to private when the repository is made public due to proprietary sourcing (especially LTA DataMall).  

`/Generated Files/`: Includes files generated using GeoPandas or other packages in ournotebooks.  

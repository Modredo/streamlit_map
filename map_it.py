import streamlit as st
import pandas as pd
import pydeck as pdk

# DATA
data = {
    "city": ["London", "Paris", "Berlin"],
    "lat": [51.5074, 48.8566, 52.5200],
    "lon": [-0.1278, 2.3522, 13.4050]
}
df = pd.DataFrame(data)

# STREAMLIT PAGE
st.title("City Locations on Map")

## Map
st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/light-v9',
    initial_view_state=pdk.ViewState(
        latitude=51.5074,
        longitude=-0.1278,
        zoom=4,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
        'ScatterplotLayer',
        data=df,
        get_position='[lon, lat]',
        get_color='[200, 30, 0, 160]',
        get_radius=20000,
        ),
    ],
))

## table 
st.write(df)

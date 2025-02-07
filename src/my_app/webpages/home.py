# src/my_app/pages/home.py
import streamlit as st
import os
from my_app.utils.path_util import get_asset_path
# from PIL import Image

def home():
    st.title("ML Showcase")
    st.subheader("Welcome to my Machine Learning portfolio!")
    st.write(
        """
        Explore interactive machine learning projects with a sleek UI.
        """
    )

    image_path = get_asset_path("ML.png")
    st.image(image_path, use_container_width=True)
    st.markdown("---")
    st.info("Select a menu item on the left to get started.")

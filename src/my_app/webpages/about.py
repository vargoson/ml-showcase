import sys
import os
from my_app.utils.path_util import get_asset_path
# src/my_app/pages/about.py
import streamlit as st

def about():
    st.title("About This Project")
    st.write(
        """
        **ML Project Showcase** is an interactive web application built with Streamlit.
        It demonstrates machine learning projects in a user-friendly interface with a modern design.
        
        **Features include:**
        - A custom sidebar menu for easy navigation.
        - A slick UI with custom CSS styling.
        - Smart features such as a dark mode toggle and real-time ML model predictions.
        
        Check out the source code on [GitHub](https://github.com/vargoson/ml-showcase).
        """
    )
    st.markdown("---")
    st.write("Developed by: Soňa Vargová")
    image_path = get_asset_path("fine.webp")
    st.image(image_path, use_container_width=True)
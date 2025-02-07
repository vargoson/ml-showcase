import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from my_app.utils.custom_css import set_custom_css
from my_app.webpages.home import home
from my_app.webpages.image_classifier import image_classifier
from my_app.webpages.about import about
from my_app.webpages.settings import settings
from my_app.webpages.chest_xray_classifier import chest_xray_classifier

def main():
    set_custom_css()

    menu = st.sidebar.radio("Navigation", ["Home", "Image Classifier", "About", "Settings", "Chest X Ray Classifier"])

    if menu == "Home":
        home()
    elif menu == "Image Classifier":
        image_classifier()
    elif menu == "About":
        about()
    elif menu == "Settings":
        settings()
    elif menu == "Chest X Ray Classifier":
        chest_xray_classifier()

if __name__ == '__main__':
    main()

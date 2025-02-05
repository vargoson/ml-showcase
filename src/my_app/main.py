import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from my_app.utils.custom_css import set_custom_css
from my_app.webpages.home import home
from my_app.webpages.image_classifier import image_classifier
from my_app.webpages.about import about
from my_app.webpages.settings import settings

def main():
    # Apply custom CSS
    set_custom_css()

    # Sidebar Menu Navigation
    menu = st.sidebar.radio("Navigation", ["Home", "Image Classifier", "About", "Settings"])

    if menu == "Home":
        home()
    elif menu == "Image Classifier":
        image_classifier()
    elif menu == "About":
        about()
    elif menu == "Settings":
        settings()

if __name__ == '__main__':
    main()

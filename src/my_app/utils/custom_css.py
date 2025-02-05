# src/my_app/utils/custom_css.py
import streamlit as st

def set_custom_css():
    custom_css = """
    <style>
    /* Overall body styling */
    body {
        background-color: #f0f2f6;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    /* Main container adjustments */
    .block-container {
        padding: 2rem 1rem;
    }
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: #ffffff;
        font-weight: bold;
    }
    [data-testid="stSidebar"] .sidebar-content {
        color: #ffffff;
    }
    /* Title style for headers */
    .css-18e3th9 {
        background: #667eea;
        color: #ffffff;
        padding: 10px;
        border-radius: 5px;
        text-align: center;
    }
    /* Styling for the file uploader */
    .stFileUploader {
        border: 2px dashed #667eea;
        border-radius: 10px;
        padding: 20px;
    }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

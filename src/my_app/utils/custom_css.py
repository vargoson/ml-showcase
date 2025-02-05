# src/my_app/utils/custom_css.py
import streamlit as st

def set_custom_css():
    custom_css = """
    <style>
    /* Global CSS variables */
    :root {
        --primary-color: #4CAF50;
        --accent-color: #FFC107;
        --hover-bg: #f5f5f5;
        --active-bg: #C8E6C9;
        --active-border: #2E7D32;
        --transition-speed: 0.3s;
    }

    /* Sidebar background (optional if you want to override) */
    [data-testid="stSidebar"] {
        background: #F7F7F7;
        padding: 1.5rem;
        border-right: 1px solid #ddd;
    }

    /* ---- Custom styles for the radio navigation buttons ---- */
    /* This selector targets the container that uses BaseWeb for radio groups.
       Note: The exact data attribute selectors might need adjustment if Streamlit updates its internals. */
    div[data-baseweb="radio"] > label {
        display: block;
        border: 1px solid transparent;
        border-radius: 8px;
        padding: 0.8rem 1.2rem;
        margin-bottom: 0.5rem;
        background: #ffffff;
        transition: background-color var(--transition-speed), transform var(--transition-speed), box-shadow var(--transition-speed);
        cursor: pointer;
    }

    /* Hover effect for navigation items */
    div[data-baseweb="radio"] > label:hover {
        background-color: var(--hover-bg);
        transform: translateX(5px);
    }

    /* Active state (when the radio button is selected) */
    div[data-baseweb="radio"] input:checked + div {
        background-color: var(--active-bg);
        border-color: var(--active-border);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }

    /* Remove the default radio circle indicator */
    div[data-baseweb="radio"] > label > div {
        display: none;
    }

    /* Optional: Adjust the container of the radio group */
    div[data-baseweb="radio"] {
        padding: 0;
    }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

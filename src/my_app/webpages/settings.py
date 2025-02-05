# src/my_app/pages/settings.py
import streamlit as st

def settings():
    st.title("Settings")
    st.write("Customize your viewing experience.")
    
    dark_mode = st.checkbox("Enable Dark Mode")
    if dark_mode:
        st.markdown(
            """
            <style>
            body {
                background-color: #2e2e2e;
                color: #f5f5f5;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        st.success("Dark mode enabled!")
    else:
        st.markdown(
            """
            <style>
            body {
                background-color: #f0f2f6;
                color: #333333;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        st.info("Dark mode disabled.")

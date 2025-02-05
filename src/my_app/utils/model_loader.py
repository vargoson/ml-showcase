# utils/model_loader.py
import streamlit as st
import tensorflow as tf

@st.cache_resource
def load_model():
    import tensorflow as tf
    return tf.keras.applications.MobileNetV2(weights='imagenet')

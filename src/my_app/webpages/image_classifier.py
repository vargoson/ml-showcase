# src/my_app/pages/image_classifier.py
import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image
import time
from my_app.utils.model_loader import load_model_mn


def image_classifier():
    st.title("Image Classifier")
    st.write("Upload an image, and a pre-trained MobileNet model will classify it in real-time.")
    
    uploaded_file = st.file_uploader("Choose an image file (JPG, JPEG, PNG)", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        try:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_container_width=True)
            
            with st.spinner("Processing and classifying the image..."):
                time.sleep(1) 
                
                # Resize and preprocess image
                target_size = (224, 224)
                image = image.resize(target_size)
                image_array = np.array(image)
                if image_array.ndim == 2:
                    image_array = np.stack((image_array,) * 3, axis=-1)
                elif image_array.shape[-1] == 4:
                    image_array = image_array[..., :3]
                image_array = np.expand_dims(image_array, axis=0)
                image_array = tf.keras.applications.mobilenet_v2.preprocess_input(image_array)
                
                # Predict and decode the results
                model = load_model_mn()
                preds = model.predict(image_array)
                results = tf.keras.applications.mobilenet_v2.decode_predictions(preds, top=3)[0]
                
                st.success("Classification Complete!")
                st.markdown("### Prediction Results:")
                for pred in results:
                    st.write(f"**{pred[1]}**: {pred[2]*100:.2f}%")
        except Exception as e:
            st.error("Error processing the image. Please try a different file.")
            st.exception(e)
    else:
        st.info("Awaiting image upload...")

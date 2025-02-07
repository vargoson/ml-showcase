import streamlit as st
from PIL import Image
from io import BytesIO
from my_app.utils.models import ChestXRayModel
from my_app.utils.path_util import get_asset_path
import pandas as pd
import time

def load_chest_xray_model():
    model_path = get_asset_path("best_model.pth")
    
    @st.cache_resource
    def load_model():
        return ChestXRayModel(model_path=model_path)

    return load_model()

def chest_xray_classifier():
    st.title("Chest X-Ray Classifier")

    st.write(
        "Upload a chest X-ray image to see model predictions for various pathologies."
    )
    
    model = load_chest_xray_model()

    uploaded_file = st.file_uploader("Choose a chest X-ray image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        try:
            image = Image.open(BytesIO(uploaded_file.read())).convert("RGB")
            st.image(image, caption="Uploaded Chest X-Ray", use_container_width=True)

            with st.spinner("Processing and classifying the image..."):
                time.sleep(1)
                results = model.predict(image)

            st.success("Classification Complete!")

            st.subheader("Model Predictions")

            df = pd.DataFrame([
                {
                    "Pathology": pathology,
                    "Probability": f"{prob:.3f}",
                    "Prediction": "Positive" if binary_label == 1 else "Negative"
                }
                for pathology, prob, binary_label in results
            ])
            st.dataframe(df)

        except Exception as e:
            st.error("Error processing the image. Please try a different file.")
            st.exception(e)
    else:
        st.info("Awaiting image upload...")

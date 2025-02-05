import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image
import time

# ------------------------------------------------------------------------------
# 1. Model Loading with Caching (to speed up reloads)
# ------------------------------------------------------------------------------
@st.cache(allow_output_mutation=True)
def load_model():
    model = tf.keras.applications.MobileNetV2(weights='imagenet')
    return model

model = load_model()

# ------------------------------------------------------------------------------
# 2. Custom CSS for a Slick UI
# ------------------------------------------------------------------------------
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

# ------------------------------------------------------------------------------
# 3. Main App Structure with a Sidebar Menu
# ------------------------------------------------------------------------------
def main():
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

# ------------------------------------------------------------------------------
# 4. Home Page
# ------------------------------------------------------------------------------
def home():
    st.title("ML Project Showcase")
    st.subheader("Welcome to the Next-Generation ML Showcase!")
    st.write(
        """
        Explore our interactive machine learning projects with a sleek UI.
        Use the sidebar to navigate to our Image Classifier, learn about the project,
        or customize your settings.
        """
    )
    # A placeholder image for the homepage (replace with your own)
    st.image("https://via.placeholder.com/800x300?text=Welcome+to+ML+Project+Showcase", use_column_width=True)
    st.markdown("---")
    st.info("Select a menu item on the left to get started.")

# ------------------------------------------------------------------------------
# 5. Image Classifier Page with Smart Features
# ------------------------------------------------------------------------------
def image_classifier():
    st.title("Image Classifier")
    st.write("Upload an image, and our ML model (MobileNetV2) will classify it in real-time!")
    
    uploaded_file = st.file_uploader("Choose an image file (JPG, JPEG, PNG)", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        try:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_column_width=True)
            
            # Add a spinner while processing the image
            with st.spinner("Processing and classifying the image..."):
                time.sleep(1)  # simulate a brief delay
                
                # Resize and process image
                target_size = (224, 224)
                image = image.resize(target_size)
                image_array = np.array(image)
                # Handle grayscale images or images with alpha channel
                if image_array.ndim == 2:
                    image_array = np.stack((image_array,)*3, axis=-1)
                elif image_array.shape[-1] == 4:
                    image_array = image_array[..., :3]
                image_array = np.expand_dims(image_array, axis=0)
                image_array = tf.keras.applications.mobilenet_v2.preprocess_input(image_array)
                
                # Predict and decode the results
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

# ------------------------------------------------------------------------------
# 6. About Page
# ------------------------------------------------------------------------------
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
        
        Check out the source code on [GitHub](https://github.com/yourusername/ml-project-showcase).
        """
    )
    st.markdown("---")
    st.write("Developed by: Your Name")
    st.image("https://via.placeholder.com/400x200?text=ML+Project", use_column_width=True)

# ------------------------------------------------------------------------------
# 7. Settings Page (e.g., Toggle Dark Mode)
# ------------------------------------------------------------------------------
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

# ------------------------------------------------------------------------------
# 8. Run the App
# ------------------------------------------------------------------------------
if __name__ == '__main__':
    main()

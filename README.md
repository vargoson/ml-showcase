# ML Showcase

ML Showcase is an interactive web application built with Streamlit that demonstrates various machine learning projects I have taken part in. The base version of the app demonstrates real-time prediction using pre-trained MobileNet model. As a learning data scientist, any feedback on this project/portfolio attempt would be much appreciated.

---

## Installation

1. **Ensure you have Python 3.11+ installed.**

2. **Clone the Repository**:
   ```bash
   git clone https://github.com/vargoson/ml-showcase.git
   cd ml-showcase
   ```

3. **Install Dependencies Using PDM**:
   - If you haven’t already, install PDM:
     ```bash
     pip install pdm
     ```
   - Then install project dependencies:
     ```bash
     pdm install
     ```

## Usage

After installing the dependencies, run the app locally using the Streamlit CLI with PDM:

```bash
pdm run streamlit run src/my_app/main.py
```

> **Note**: If you encounter issues with relative paths for assets, ensure your working directory is set correctly.


## Project Structure

```plaintext
ml-showcase/
├── .github/
│   └── workflows/
│       └── ci.yml             # CI/CD configuration for GitHub Actions
├── webpages/                  # Static files (e.g., assets, images)
│   └── assets/
│       └── ML.png             # Example image asset
├── pyproject.toml             # PDM project configuration
├── pdm.lock                   # PDM lock file
└── src/
    └── my_app/
        ├── __init__.py
        ├── main.py            # Main entry point with custom navigation
        ├── utils/
        │   ├── __init__.py
        │   └── path_util.py   # Utility for constructing asset paths
        └── webpages/
            ├── __init__.py
            ├── home.py        # Home page content
            ├── image_classifier.py  # Image classification page
            ├── about.py       # About page
            └── settings.py    # Settings page (e.g., dark mode toggle)

```

## Features

1. **Interactive Image Classification**  
   Upload an image and see predictions from MobileNetV2 in real time

2. **Custom Navigation**  
   An intuitive sidebar to switch between pages

3. **Custom CSS Styling**  
   A modern UI with a custom CSS theme that enhances the look and feel of the app

4. **Modular Structure**  
   Organized into multiple pages and utilities, making the codebase easy to maintain and scale


## Development

- **Custom Navigation & Pages**  
  The app uses a custom navigation system defined in `main.py`. If you add or modify pages, update the navigation links accordingly.

- **Custom CSS**  
  A custom CSS file is used (in `utils/custom_css.py`). Modify it to change the look and feel.

- **Testing**  
  GitHub Actions (see `.github/workflows/ci.yml`) helps maintain code quality through Continuous Integration. Testing will be added as the codebase grows.



## Deployment

This app will eventually be deployed on a webpage, either using Streamlit Community Cloud, or other options will be explored.


## Contributing

Contributions are welcome! To contribute:

1. **Fork** the repository.
2. **Create a new branch** for your feature or bug fix.
3. **Commit** your changes.
4. **Open a Pull Request** with a description of your changes.


## License

This project is licensed under the [GNU License](LICENSE).

## Thank you for stopping by! 



import pandas as pd
import pickle as pickel
import streamlit as st
import numpy as np
#streamlit run streamlit_1.py


def add_sidebar():
    st.sidebar.header('Cell Nuclei Details')

    slider_labels = [
        ("Radius (mean)", "radius_mean"),
        ("Texture (mean)", "texture_mean"),
        ("Perimeter (mean)", "perimeter_mean"),
        ("Area (mean)", "area_mean"),
        ("Smoothness (mean)", "smoothness_mean"),
        ("Compactness (mean)", "compactness_mean"),
        ("Concavity (mean)", "concavity_mean"),
        ("Concave points (mean)", "concave points_mean"),
        ("Symmetry (mean)", "symmetry_mean"),
        ("Fractal dimension (mean)", "fractal_dimension_mean"),
        ("Radius (se)", "radius_se"),
        ("Texture (se)", "texture_se"),
        ("Perimeter (se)", "perimeter_se"),
        ("Area (se)", "area_se"),
        ("Smoothness (se)", "smoothness_se"),
        ("Compactness (se)", "compactness_se"),
        ("Concavity (se)", "concavity_se"),
        ("Concave points (se)", "concave points_se"),
        ("Symmetry (se)", "symmetry_se"),
        ("Fractal dimension (se)", "fractal_dimension_se"),
        ("Radius (worst)", "radius_worst"),
        ("Texture (worst)", "texture_worst"),
        ("Perimeter (worst)", "perimeter_worst"),
        ("Area (worst)", "area_worst"),
        ("Smoothness (worst)", "smoothness_worst"),
        ("Compactness (worst)", "compactness_worst"),
        ("Concavity (worst)", "concavity_worst"),
        ("Concave points (worst)", "concave points_worst"),
        ("Symmetry (worst)", "symmetry_worst"),
        ("Fractal dimension (worst)", "fractal_dimension_worst"),
    ]

    for label, key in slider_labels:

        random_value = np.random.uniform(5, 100)
        max_value = np.random.uniform(79, 265)

        st.sidebar.slider(
            label,
            min_value=float(0),
            max_value=float(max_value),
            value = float(random_value)
        )


def main():

    st.set_page_config(
        page_title="Breast Cancer Predictor",
        page_icon="👧",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            'Get Help': 'https://www.linkedin.com/in/maheshgowda47/',
            'About': "# https://github.com/MaheshGowda47"
    }
)
    add_sidebar()
    
    with st.container():
        st.title('Breast Cancer Predictor')
        st.write('Please connect this app to your cytology lab to help diagnose breast cancer form your tissue sample. This app predicts using a machine learning model whether a breast mass is benign or malignant based on the measurements it receives from your cytosis lab. You can also update the measurements by hand using the sliders in the sidebar')

    col1, col2 = st.columns([4,1])

    with col1:
        st.write('column1')
    with col2:
        st.write('column2')







if __name__ == '__main__':
    main()




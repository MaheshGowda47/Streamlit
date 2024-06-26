import pandas as pd
import streamlit as st
import numpy as np
import plotly.graph_objects as go
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

    input_dict = {}

    for label, key in slider_labels:

# NOTE : we use random value generating, changing an single value in any slider, it reflects to all sliders
        random_value = np.random.uniform(5, 100)
        min_value = np.random.uniform(1,100)
        max_value = np.random.uniform(79, 265)

        input_dict[key] = st.sidebar.slider(
            label,
            min_value=float(min_value),
            max_value=float(max_value),
            value = float(random_value)
        )

    return input_dict

def add_radar_chart(input_data):

    categories = ['Radius', 'Texture', 'Perimeter', 'Area', 
                'Smoothness', 'Compactness', 
                'Concavity', 'Concave Points',
                'Symmetry', 'Fractal Dimension']

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=[
          input_data['radius_mean'], input_data['texture_mean'], input_data['perimeter_mean'],
          input_data['area_mean'], input_data['smoothness_mean'], input_data['compactness_mean'],
          input_data['concavity_mean'], input_data['concave points_mean'], input_data['symmetry_mean'],
          input_data['fractal_dimension_mean']
        ],
        theta=categories,
        fill='toself',
        name='Mean Value'
    ))

    fig.add_trace(go.Scatterpolar(
        r=[
          input_data['radius_se'], input_data['texture_se'], input_data['perimeter_se'], input_data['area_se'],
          input_data['smoothness_se'], input_data['compactness_se'], input_data['concavity_se'],
          input_data['concave points_se'], input_data['symmetry_se'],input_data['fractal_dimension_se']
        ],
        theta=categories,
        fill='toself',
        name='Standard value'
    ))

    fig.add_trace(go.Scatterpolar(
        r=[
          input_data['radius_worst'], input_data['texture_worst'], input_data['perimeter_worst'],
          input_data['area_worst'], input_data['smoothness_worst'], input_data['compactness_worst'],
          input_data['concavity_worst'], input_data['concave points_worst'], input_data['symmetry_worst'],
          input_data['fractal_dimension_worst']
        ],
        theta=categories,
        fill='toself',
        name='Worst Value'
    ))

    fig.update_layout(
      polar=dict(
        radialaxis=dict(
          visible=True,
          range=[0, 100]
        )),
      showlegend=False
    )

    return fig


def add_prediction(input_data):
    mean = round(sum(input_data.values()) / len(input_data), 2)
    input_array = np.array(list(input_data.values())).reshape(1, -1)

    return mean, input_array



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
    input_data = add_sidebar()
    # st.write(input_data)

    with st.container():
        st.title('Breast Cancer Predictor')
        st.write('Please connect this app to your cytology lab to help diagnose breast cancer form your tissue sample. This app predicts using a machine learning model whether a breast mass is benign or malignant based on the measurements it receives from your cytosis lab. You can also update the measurements by hand using the sliders in the sidebar')

    col1, col2 = st.columns([3,1])

    with col1:
        radar_chart = add_radar_chart(input_data)
        st.plotly_chart(radar_chart)
    with col2:
        prediction, input_array = add_prediction(input_data)

        st.markdown (''' **:red[Input Data]** ''')
        st.write(input_array)

        st.markdown("**:red[Prediction] - Mean Value**")
        button = st.button("Predict")
        if button:
            st.write(prediction)

        st.markdown("**:red[Image View]**")
        button = st.button("Image")
        if button:
            st.image("Images\download.jpeg")
        
        st.button('Reset', type='primary')

if __name__ == '__main__':
    main()

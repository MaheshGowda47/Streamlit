import pandas as pd
import pickle as pickel
import streamlit as st
#streamlit run streamlit_1.py


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
    
    with st.container():
        st.title('Breast Cancer Predictor')
        st.write('Please connect this app to your cytology lab to help diagnose breast cancer form your tissue sample. This app predicts using a machine learning model whether a breast mass is benign or malignant based on the measurements it receives from your cytosis lab. You can also update the measurements by hand using the sliders in the sidebar')

    col1, col2 = st.columns([4,1])

    with col1:
        st.write('colum1')
    with col2:
        st.write('column2')

if __name__ == '__main__':
    main()




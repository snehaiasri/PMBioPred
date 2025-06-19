import streamlit as st

st.set_page_config( page_title="PM-BioPred", initial_sidebar_state="expanded", layout="wide")
col1, col2, col3 = st.columns([1.5, 20, 2])

with col1:
    st.image("static/images/icarlogo.png", width=150)

with col2:
    st.markdown("<h1 style='text-align:center;'> PM-BioPred: A Web-Server for Prediction of Compound Bioactivity against Plant and Microbes Proteins</h1>", unsafe_allow_html=True)

with col3:
    st.image("static/images/iasri-logo.png", width=150)

st.markdown("---")
st.text("")

st.header("Welcome to PM-BioPred")
st.markdown("""
    **PM-BioPred** predicts the **bioactivity of small molecules** against different biological targets using machine learning and chemical descriptors computed from SMILES.
    
    -	PM-BioPred is a web-based prediction server for assessing the bioactivity of compounds against plant and microbial proteins.
    -	The tool is built on curated datasets of experimentally validated active and inactive compounds, offering prediction accuracy of 86% (plants) and >90% (microbes).
    -	It addresses the gap in computational bioactivity prediction resources for non-human systems, particularly in agricultural and microbial research.
    -	The web interface allows users to query SMILES-formatted compounds and retrieve bioactivity classifications with interpretability.
    -	PM-BioPred is freely accessible to the academic community and supports early-stage screening of agrochemicals and antimicrobial agents.


    **Input:** CSV file with `molecule_id` and `SMILES`  
    **Output:** Bioactivity prediction with probabilities  
    **Target Options:** Bacteria, Fungi, Virus, Plant
""")

st.text("")
st.markdown("<div style='background-color:#32CD32; text-align:center'><p style='color:white'>Copyright © 2025 ICAR-Indian Agricultural Statistics Research Institute, New Delhi-110012. All rights reserved.</p></div>", unsafe_allow_html=True)
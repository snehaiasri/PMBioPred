import streamlit as st
import base64

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


st.subheader("User Manual")

file_path = "static/PM-BioPred_Tutorial.pdf"

with open(file_path, "rb") as f:
    st.download_button(
        label="📄 Open / Download PDF",
        data=f,
        file_name="help.pdf",
        mime="application/pdf"
    )

st.markdown(
    """
    <p>
    After clicking, your browser will open the PDF in a new tab.
    </p>
    """,
    unsafe_allow_html=True
)




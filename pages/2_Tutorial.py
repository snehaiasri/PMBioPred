import streamlit as st
import pandas as pd

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

st.title("📘 PM-BioPred: User Tutorial")

st.write(
"""
*Web server for predicting compound bioactivity against Plant, Bacterial, Fungal, and Viral proteins.*
"""
)
st.header("1. Access the Web Server")
st.markdown("Open your browser and visit: [https://pmbiopred.streamlit.app/](https://pmbiopred.streamlit.app/)")

st.write(
"""
You will see the homepage with navigation options (Home, Prediction, Developers, Contact Us):
"""
)
st.image("static/images/fig1_homepage.png", caption="Figure 1: Homepage", width=700)
st.write("This page introduces the tool and gives basic information about its purpose and use.")

st.header("2. Navigate to the Prediction Page")

st.write("Click **Prediction** from the left sidebar.")

st.image("static/images/fig2_prediction.png", caption="Figure 2: Navigation to Prediction Page", width=700)
st. write("This opens the prediction interface where you can submit your compounds.")

st.header("3. Choose Target Organism")
st.write("In the dropdown menu **“Select Target Organism”**, choose the type of biological target:")
df_targets = pd.DataFrame({
    "Option": ["Bacteria", "Fungi", "Virus", "Plant"],
    "Meaning": [
        "Predict antibacterial compound activity",
        "Predict antifungal compound activity",
        "Predict antiviral compound activity",
        "Predict plant-protein modulator activity"
    ]
})

#st.table(df_targets)
st.markdown(df_targets.style.hide(axis="index").to_html(), unsafe_allow_html=True)

st.info("**Note:** Models are trained separately for each organism group for improved accuracy.")

st.header("4. Prepare Your Input File")

st.write("PM-BioPred accepts a CSV file with two required columns:")

df_ex = pd.DataFrame({"molecule_id":["CHEMBL132431", "CHEMBL275309"], "SMILES":["CN(Cc1...)", "Nc1nc..."]})
st.markdown(df_ex.style.hide(axis="index").to_html(), unsafe_allow_html=True)
#st.code(
#"""molecule_id,SMILES
#CHEMBL132431,CN(Cc1...)
#CHEMBL275309,Nc1nc...
#""")
st.write("Example:")
st.image("static/images/fig3_sample_csv.png", caption="Figure 3: Sample CSV", width=700)

st.subheader("Guidelines")

st.markdown("""
- molecule_id can be any identifier  
- SMILES must be valid chemical notation   
- File must be CSV format  
- Maximum file size: 200 MB  
""")

st.write("Click *Download Sample File* to obtain a template.")

st.header("5. Upload Your File")

st.write("Drag and drop your CSV file or click Browse files.")

st.header("6. Run Prediction")

st.write("Press the **Predict** button. The server processes compounds and displays results.")

st.header("7. Interpreting Results")

df_cols = pd.DataFrame({
    "Column": [
        "Molecule ID",
        "SMILES",
        "Probability (Active)",
        "Probability (Inactive)",
        "Prediction"
    ],
    "Description": [
        "User identifier",
        "Input structure",
        "Likelihood of activity",
        "Likelihood of inactivity",
        "Active / Inactive"
    ]
})

#st.table(df_cols)
st.markdown(df_cols.style.hide(axis="index").to_html(), unsafe_allow_html=True)

st.image("static/images/fig4_results.png", caption="Figure 4: Result Table", width=700)

st.subheader("Interpretation Example")

df_interpret = pd.DataFrame({
    "Molecule": ["CHEMBL132431", "CHEMBL2005366"],
    "Active Prob": ["0.616", "0.19"],
    "Inactive Prob": ["0.384", "0.81"],
    "Prediction": ["Active", "Inactive"]
})
#st.table(df_cols)
st.markdown(df_interpret.style.hide(axis="index").to_html(), unsafe_allow_html=True)

st.write("Higher probability = higher confidence in prediction.")

st.subheader("Exporting Results")
st.write("Click **Download** (built-in browser table download) to save results.")

st.header("8. Next Steps")
st.write("You can now take **Active-predicted compounds** forward for:")
st.markdown("""
✅ Molecular docking  
✅ Molecular dynamics  
✅ Laboratory testing  
✅ Lead optimization  
""")

st.text("")
st.markdown("<div style='background-color:#32CD32; text-align:center'><p style='color:white'>Copyright © 2025 ICAR-Indian Agricultural Statistics Research Institute, New Delhi-110012. All rights reserved.</p></div>", unsafe_allow_html=True)

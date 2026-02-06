import streamlit as st
import pandas as pd
import joblib
from rdkit import Chem
from rdkit.Chem import Descriptors
import numpy as np

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

# Load model, scaler, descriptor columns

with open("static/descriptor_columns.txt") as f:
    descriptor_names = f.read().splitlines()

# RDKit descriptor functions
descriptor_funcs = {
    "MolWt": Descriptors.MolWt,
    "MolLogP": Descriptors.MolLogP,
    "NumHDonors": Descriptors.NumHDonors,
    "NumHAcceptors": Descriptors.NumHAcceptors,
    "TPSA": Descriptors.TPSA,
    "NumRotatableBonds": Descriptors.NumRotatableBonds
}

st.markdown("### Predict Bioactivity of Compound against Selected Target Organisms")

file_path = 'static/example.csv'  # update filename & extension as needed

with open(file_path, "rb") as file:
    file_content = file.read()

st.download_button(
    label="📥 Download Sample File",
    data=file_content,
    file_name="example.csv",  # this will be the filename for the download
    mime="text/csv"  # change MIME type based on file format
)

target = st.selectbox("Select Target Organism", ["Bacteria", "Fungi", "Virus", "Plant"])

@st.cache_resource
def load_model(target):
    return joblib.load(f"static/models/{target}.pkl")

uploaded_file = st.file_uploader("Upload CSV with columns: `molecule_id`, `SMILES`", type=["csv"])
# Function to compute RDKit descriptors
def compute_descriptors(smiles):
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return None
    return [descriptor_funcs[name](mol) for name in descriptor_names]

if st.button("Predict"):
    if uploaded_file is not None:
        input_df = pd.read_csv(uploaded_file)
        results = []

        model = load_model(target)
        
        for i, row in input_df.iterrows():
            desc = compute_descriptors(row["SMILES"])
            if desc:
                scaled = np.array(desc).reshape(1, -1)
                prob = model.predict_proba(scaled)[0]
                pred = model.predict(scaled)[0]
                results.append({
                    "S.No.": i + 1,
                    "Molecule ID": row["molecule_id"],
                    "SMILES": row["SMILES"],
                    "Probability (Active)": round(prob[1], 3),
                    "Probability (Inactive)": round(prob[0], 3),
                    "Prediction": "Yes" if pred == 1 else "No"
                })
            else:
                results.append({
                    "S.No.": i + 1,
                    "Molecule ID": row["molecule_id"],
                    "SMILES": row["SMILES"],
                    "Probability (Active)": "Invalid",
                    "Probability (Inactive)": "Invalid",
                    "Prediction": "Invalid SMILES"
                })

        result_df = pd.DataFrame(results)
        st.dataframe(result_df, hide_index = True)


    

st.text("")
st.markdown("<div style='background-color:#32CD32; text-align:center'><p style='color:white'>Copyright © 2025 ICAR-Indian Agricultural Statistics Research Institute, New Delhi-110012. All rights reserved.</p></div>", unsafe_allow_html=True)

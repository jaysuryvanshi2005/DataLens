import streamlit as st
import pandas as pd

st.set_page_config(page_title="Upload Data", layout="wide")

st.title("📤 Upload Your CSV Dataset")

# Instruction
st.info("Upload a CSV file to begin analysis.")

# File uploader
file = st.file_uploader("Choose a CSV file", type=["csv"])

if file is not None:
    try:
        # Read CSV
        df = pd.read_csv(file, low_memory=False)

        # Clean column names
        df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

        # Success message
        st.success("✅ File uploaded successfully!")

        # Dataset preview
        st.subheader("🔍 Dataset Preview")
        st.write(df.head())

        # Dataset shape
        st.subheader("📊 Dataset Overview")
        col1, col2 = st.columns(2)
        col1.metric("Rows", df.shape[0])
        col2.metric("Columns", df.shape[1])

        # Column list
        st.subheader("📌 Column Names")
        st.write(list(df.columns))

        # Save to session state
        st.session_state['df'] = df

        # Navigation hint
        st.success("🚀 Data is ready! Go to the 'Analysis' page.")

    except Exception as e:
        st.error(f"❌ Error loading file: {e}")

else:
    st.warning("⚠️ Please upload a CSV file to continue.")
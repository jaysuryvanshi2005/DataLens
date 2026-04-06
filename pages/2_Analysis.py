import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Analysis", layout="wide")

st.title("📊 Data Analysis & Insights")

# Check if data exists
if 'df' not in st.session_state:
    st.warning("⚠️ Please upload a dataset first from the Upload Page.")
else:
    df = st.session_state['df']

    # Preview
    st.subheader("🔍 Dataset Preview")
    st.write(df.head())

    # 📊 Dataset Overview
    st.subheader("📊 Dataset Overview")

    col1, col2, col3 = st.columns(3)
    col1.metric("Rows", df.shape[0])
    col2.metric("Columns", df.shape[1])
    col3.metric("Total Missing Values", df.isnull().sum().sum())

    # ⚠️ Missing Values Analysis
    st.subheader("⚠️ Missing Values Analysis")

    missing = df.isnull().sum()
    missing = missing[missing > 0]

    if not missing.empty:
        st.warning("Columns with missing values detected!")

        st.write(missing)

        # Bar chart
        import matplotlib.pyplot as plt

        fig, ax = plt.subplots(figsize=(5, 3))  # smaller size

        missing.plot(kind='bar', ax=ax)
        ax.set_title("Missing Values per Column")

        st.pyplot(fig)

    else:
        st.success("✅ No missing values found!")

    # 🔁 Duplicate Rows
    st.subheader("🔁 Duplicate Rows")

    duplicates = df.duplicated().sum()

    if duplicates > 0:
        st.warning(f"⚠️ Found {duplicates} duplicate rows")
    else:
        st.success("✅ No duplicate rows found!")

   
    # 🧠 Column Type Detection

    st.subheader("🧠 Column Type Detection")

    num_cols = df.select_dtypes(include=['int64', 'float64']).columns
    cat_cols = df.select_dtypes(include=['object']).columns

    st.write("🔢 Numerical Columns:", list(num_cols))
    st.write("🔤 Categorical Columns:", list(cat_cols))


    # 📈 Statistical Summary

    st.subheader("📈 Statistical Summary")

    if len(num_cols) > 0:
        st.write(df[num_cols].describe())
    else:
        st.info("No numerical columns available.")


    # 📊 Data Quality Score

    st.subheader("⭐ Data Quality Score")

    total_cells = df.shape[0] * df.shape[1]
    missing_cells = df.isnull().sum().sum()

    quality_score = round((1 - (missing_cells / total_cells)) * 100, 2)

    if quality_score > 80:
        st.success(f"✅ Data Quality Score: {quality_score}% (Good)")
    elif quality_score > 50:
        st.warning(f"⚠️ Data Quality Score: {quality_score}% (Moderate)")
    else:
        st.error(f"❌ Data Quality Score: {quality_score}% (Poor)")



    st.success("🎉 Analysis Complete! You can now can visualize the columns.")
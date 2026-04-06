import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from style import apply_theme

apply_theme()

st.set_page_config(page_title="Visualization", layout="wide")

st.title("📊 Data Visualization")

# Check dataset
if 'df' not in st.session_state:
    st.warning("⚠️ Please upload a dataset first.")
else:
    df = st.session_state['df']

    # 🔧 Missing Value Handling
    st.subheader("⚙️ Data Cleaning (for Visualization)")

    threshold = st.slider(
        "Select missing value threshold (%)",
        0, 100, 50
    ) / 100

    missing_percent = df.isnull().mean()

    removed_cols = missing_percent[missing_percent >= threshold].index

    if len(removed_cols) > 0:
        st.warning(f"Removing columns: {list(removed_cols)}")

    # Create cleaned dataframe
    clean_df = df.loc[:, missing_percent < threshold]

    st.success("✅ Data cleaned for visualization")

    # Safety check
    if clean_df.shape[1] == 0:
        st.error("❌ No columns left after filtering! Reduce threshold.")
    else:


        # 📊 Single Column Visualization

        st.subheader("📊 Visualize Individual Column")

        column = st.selectbox("Choose a column", clean_df.columns)

        if clean_df[column].dtype in ['int64', 'float64']:

            st.info("Numerical Column Detected")

            chart_type = st.selectbox(
                "Select Chart Type",
                ["Histogram", "Box Plot"]
            )

            fig, ax = plt.subplots(figsize=(6,3))

            if chart_type == "Histogram":
                ax.hist(clean_df[column].dropna(),edgecolor = "black")
                ax.set_title(f"Histogram of {column}")

            elif chart_type == "Box Plot":
                ax.boxplot(clean_df[column].dropna())
                ax.set_title(f"Box Plot of {column}")

            st.pyplot(fig)

        else:
            st.info("Categorical Column Detected")

            chart_type = st.selectbox(
                "Select Chart Type",
                ["Bar Chart", "Pie Chart"]
            )

            data = clean_df[column].value_counts().head(10)

            fig, ax = plt.subplots(figsize=(6,3))

            if chart_type == "Bar Chart":
                data.plot(kind='bar', ax=ax,edgecolor = "black")
                ax.set_title(f"Top Categories in {column}")

            elif chart_type == "Pie Chart":
                ax.pie(data, labels=data.index, autopct='%1.1f%%')
                ax.set_title(f"Distribution of {column}")

            st.pyplot(fig)


        # 📊 Visualize All Columns

        st.subheader("📊 Visualize All Columns")

        if st.button("Generate All Visualizations"):

            for col in clean_df.columns:
                st.markdown(f"### 🔹 {col}")

                fig, ax = plt.subplots(figsize=(5,2))

                if clean_df[col].dtype in ['int64', 'float64']:
                    ax.hist(clean_df[col].dropna())
                else:
                    clean_df[col].value_counts().head(10).plot(kind='bar', ax=ax)

                st.pyplot(fig)
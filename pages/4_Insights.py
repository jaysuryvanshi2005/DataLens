import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv
from style import apply_theme

apply_theme()


# Load env
load_dotenv()
client = Groq(api_key=os.getenv("GSK_API_KEY"))

# Page config
st.set_page_config(page_title="AI Insights", layout="wide")
st.title("🔍 AI INSIGHTS")


# Check dataset
if 'df' not in st.session_state:
    st.warning("⚠️ Please upload a dataset first.")
else:
    df = st.session_state['df']



# 🧠 Title Section
st.markdown('<p class="main-title">🧠 AI Insights Dashboard</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-text">Understand what your data is trying to tell you 🚀</p>', unsafe_allow_html=True)

# Check dataset
if 'df' not in st.session_state:
    st.warning("⚠️ Please upload a dataset first.")
    st.stop()

df = st.session_state['df']

# 🧾 Info Cards
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f'<div class="card">📊 <b>Rows:</b><br>{df.shape[0]}</div>', unsafe_allow_html=True)

with col2:
    st.markdown(f'<div class="card">📈 <b>Columns:</b><br>{df.shape[1]}</div>', unsafe_allow_html=True)

with col3:
    st.markdown(f'<div class="card">🧮 <b>Features:</b><br>{", ".join(df.columns[:5])}...</div>', unsafe_allow_html=True)

st.write("")

# 🧠 Function
def generate_insights(df):
    summary = df.describe(include='all').fillna(0).head().to_string()
    columns = ", ".join(df.columns[:10])
    missing = df.isnull().sum().head().to_string()
    prompt = f"""
        You are an expert data scientist.

        Analyze the dataset deeply and focus ONLY on meaningful patterns and relationships.

        Dataset Info:
        Columns: {columns}

        Missing Values:
        {missing}

        Statistics:
        {summary}

        Your tasks:

        1. Identify strong relationships between columns (correlations, dependencies, cause-effect).
        2. Explain patterns and trends in the data (e.g., increasing/decreasing behavior, clusters, seasonality).
        3. Highlight any surprising or non-obvious insights hidden in the data.
        4. Explain what the data is "telling" in simple terms (storytelling).
        5. Suggest what could happen in the future based on observed patterns (predictions or trends).
        6. Suggest which columns are most important (feature importance intuition).

        ⚠️ Do NOT mention:
        - Missing values
        - Duplicates
        - Basic dataset description

        Focus only on deep insights, patterns, and future predictions.

        Make the output:
        - Clear
        - Insightful
        - Easy to understand
        - Structured with bullet points
        - give in short points and effective manner this are to shown in the model so it should look good
        """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are a smart data analyst."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content

# 🚀 Button Centered
st.markdown("###")
col_btn1, col_btn2, col_btn3 = st.columns([1,2,1])

with col_btn2:
    if st.button("Generate Insights"):
        with st.spinner("Analyzing data..."):
            insights = generate_insights(df)

            # ✅ SAVE IT HERE
            st.session_state['insights'] = insights

            st.markdown(insights)

            st.markdown("### 📌 Insights")
            st.markdown(f"""
            <div class="card">
            {insights}
            </div>
            """, unsafe_allow_html=True)
import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Data Lens | AI Analysis", layout="wide", page_icon="🔍")

# 2. Custom CSS for Styling
st.markdown("""
    <style>
    /* Main background and font */
    .main {
        background-color: #0E1117;
    }
    /* Custom Card Styling */
    .feature-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #00D4FF;
        box-shadow: 2px 2px 15px rgba(0,0,0,0.05);
        margin-bottom: 20px;
        height: 100%;
    }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        background-color: #00D4FF;
        color: #0E1117;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Header Section with Columns
col1, col2 = st.columns([2, 1])

with col1:
    st.title("🔍 Data Lens")
    st.subheader("AI-Powered Data Dictionary & Analysis Tool")
    st.write("""
    **Data Lens** is an intelligent system designed to automatically analyze CSV datasets 
    and generate meaningful insights quickly and accurately. 
    Stop spending hours on manual cleaning—let AI do the heavy lifting.
    """)
    
    if st.button("🚀 Get Started / Upload CSV"):
        st.info("Please select the **'Upload Data'** page from the sidebar to continue!")

with col2:
    # This acts as a visual placeholder or hero area
    st.image("https://cdn-icons-png.flaticon.com/512/2103/2103633.png", width=200)

st.divider()

# 4. Features Section (Using Columns for a Grid Layout)
st.markdown("### 🚀 Key Capabilities")
f_col1, f_col2, f_col3 = st.columns(3)

with f_col1:
    st.markdown("""<div class="feature-card">
    <h4>📂 Smart Upload</h4>
    <p>Seamlessly upload CSVs and let the system detect structure, types, and delimiters automatically.</p>
    </div>""", unsafe_allow_html=True)

with f_col2:
    st.markdown("""<div class="feature-card">
    <h4>🤖 AI Descriptions</h4>
    <p>Generate human-readable descriptions for every column using advanced LLMs.</p>
    </div>""", unsafe_allow_html=True)

with f_col3:
    st.markdown("""<div class="feature-card">
    <h4>📊 Deep Insights</h4>
    <p>Identify missing values, duplicates, and statistical patterns in seconds.</p>
    </div>""", unsafe_allow_html=True)

st.write("") # Spacer

# 5. Why Data Lens Section
with st.expander("💡 Why choose Data Lens over manual analysis?", expanded=True):
    st.write("""
    Manual data analysis is prone to human error and consumes nearly 80% of a data scientist's time. 
    **Data Lens** automates the repetitive "Data Cleaning" and "Dictionary Creation" phases, allowing 
    you to focus on decision-making and high-level strategy.
    """)

# 6. Success Banner
st.success("✨ Transform raw data into insights instantly with AI 🚀")

# 7. Sidebar
st.sidebar.title("Navigation")
st.sidebar.markdown("---")
st.sidebar.info("Navigate to **Upload Data** to begin your analysis.")
import streamlit as st

def apply_theme():
    st.markdown("""
    <style>
    
    /* ===== GLOBAL BACKGROUND ===== */
    .main {
        background-color: #f5f7fb;
    }

    /* ===== HEADINGS ===== */
    .main-title {
        font-size: 40px;
        font-weight: 700;
        color: #111827;
        margin-bottom: 5px;
    }

    .sub-text {
        font-size: 18px;
        color: #6b7280;
        margin-bottom: 25px;
    }

    /* ===== CARD DESIGN ===== */
    .card {
        background: white;
        padding: 20px;
        border-radius: 16px;
        box-shadow: 0px 4px 20px rgba(0,0,0,0.06);
        margin-bottom: 20px;
    }

    /* ===== METRIC CARDS ===== */
    .metric-card {
        background: linear-gradient(135deg, #6366f1, #4f46e5);
        color: white;
        padding: 20px;
        border-radius: 14px;
        text-align: center;
        font-weight: 600;
    }

    .metric-value {
        font-size: 28px;
        font-weight: 700;
    }

    .metric-label {
        font-size: 14px;
        opacity: 0.9;
    }

    /* ===== BUTTON ===== */
    .stButton>button {
        background: linear-gradient(135deg, #6366f1, #4f46e5);
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        border: none;
        font-weight: 600;
        transition: 0.3s;
    }

    .stButton>button:hover {
        transform: scale(1.03);
        box-shadow: 0px 5px 15px rgba(0,0,0,0.2);
    }

    /* ===== UPLOAD BOX ===== */
    .upload-box {
        border: 2px dashed #6366f1;
        padding: 30px;
        border-radius: 12px;
        text-align: center;
        background-color: #eef2ff;
    }

    /* ===== SECTION TITLE ===== */
    .section-title {
        font-size: 20px;
        font-weight: 600;
        color: #374151;
        margin-bottom: 10px;
    }

    /* ===== INSIGHTS BOX ===== */
    .insight-box {
        background: #111827;
        color: #f9fafb;
        padding: 20px;
        border-radius: 12px;
        max-height: 400px;
        overflow-y: auto;
        font-size: 14px;
        line-height: 1.6;
    }

    </style>
    """, unsafe_allow_html=True)
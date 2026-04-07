import streamlit as st
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
import io
import re
from style import apply_theme

apply_theme()

def clean_markdown(text):
    """Converts basic markdown bold/bullets to ReportLab HTML-like tags."""
    # Convert **text** to <b>text</b>
    text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
    # Convert * or + at the start of a line to a bullet symbol
    text = re.sub(r'^(\s*)[\*\+]\s+', r'\1• ', text, flags=re.MULTILINE)
    # Remove any remaining '■' or similar symbols if you don't want them
    text = text.replace('■', '')
    return text


def create_pdf(report_text, df):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()
    content = []

    # 1. Add Title to PDF
    content.append(Paragraph("<b>Data Analysis Report</b>", styles["Title"]))
    content.append(Spacer(1, 0.2 * inch))

    # 2. Add Dataset Overview Section
    content.append(Paragraph("<b>Dataset Overview</b>", styles["Heading2"]))
    content.append(Paragraph(f"Rows: {df.shape[0]}", styles["Normal"]))
    content.append(Paragraph(f"Columns: {df.shape[1]}", styles["Normal"]))
    
    # List columns
    cols_str = ", ".join(list(df.columns))
    content.append(Paragraph(f"<b>Columns:</b> {cols_str}", styles["Normal"]))
    
    # Optional: Add Missing Values info
    missing_info = df.isnull().sum().sum()
    content.append(Paragraph(f"Total Missing Values: {missing_info}", styles["Normal"]))
    content.append(Spacer(1, 0.3 * inch))

    # 3. Add AI Insights Section
    content.append(Paragraph("<b> AI Generated Insights</b>", styles["Heading2"]))
    for line in report_text.split("\n"):
        if line.strip():
            # Bold keywords if they look like headers
            if any(k in line.lower() for k in ["overview", "trend", "insight", "prediction"]):
                content.append(Paragraph(f"<b>{line}</b>", styles["Heading3"]))
            else:
                content.append(Paragraph(line, styles["Normal"]))

    doc.build(content)
    buffer.seek(0)
    return buffer

# --- Streamlit UI Logic ---
st.title("Data Report")

if 'insights' not in st.session_state or 'df' not in st.session_state:
    st.warning("Please generate insights and upload data first")
    st.stop()

insights = st.session_state['insights']
df = st.session_state['df']

# Display on UI
st.write("Click the button below to download the Report of the dataset.")

# Generate and Download PDF
# Pass BOTH insights and df to the function
text1 = clean_markdown(insights)
pdf_file = create_pdf(text1, df)

st.download_button(
    label="Download Full Report (PDF)",
    data=pdf_file,
    file_name="data_report.pdf",
    mime="application/pdf"
)

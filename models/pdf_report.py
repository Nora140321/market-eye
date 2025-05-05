from fpdf import FPDF
import os
from datetime import datetime

def create_pdf_report(ticker, max_price, min_price, average_price, predicted_price, recommendation, chart_image_path=None):
    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Title
        pdf.set_title(f"{ticker} Market Insight Report")
        pdf.set_font("Arial", "B", 16)
        pdf.cell(200, 10, txt=f"{ticker} Stock Report", ln=True, align="C")
        pdf.ln(10)

        # Date
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt=f"📅 Report Date: {datetime.today().strftime('%Y-%m-%d')}", ln=True)
        pdf.ln(10)

        # Stats
        pdf.set_font("Arial", "B", 12)
        pdf.cell(200, 10, txt="📊 Historical Stats:", ln=True)
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt=f"- Max Close Price: ${max_price:.2f}", ln=True)
        pdf.cell(200, 10, txt=f"- Min Close Price: ${min_price:.2f}", ln=True)
        pdf.cell(200, 10, txt=f"- Average Close Price: ${average_price:.2f}", ln=True)

        pdf.ln(10)
        pdf.set_font("Arial", "B", 12)
        pdf.cell(200, 10, txt="🧠 LSTM Prediction:", ln=True)
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt=f"- Predicted Next Close: ${predicted_price:.2f}", ln=True)

        # Recommendation
        pdf.ln(10)
        pdf.set_font("Arial", "B", 12)
        pdf.cell(200, 10, txt="💬 Gemini Recommendation:", ln=True)
        pdf.set_font("Arial", size=12)
        for line in recommendation.strip().split("\n"):
            pdf.multi_cell(0, 10, txt=line)

        # Chart image
        if chart_image_path and os.path.exists(chart_image_path):
            pdf.ln(10)
            pdf.set_font("Arial", "B", 12)
            pdf.cell(200, 10, txt="📈 Closing Price Chart:", ln=True)
            pdf.image(chart_image_path, x=10, w=180)

        # Save PDF
        output_dir = "reports"
        os.makedirs(output_dir, exist_ok=True)
        file_path = os.path.join(output_dir, f"{ticker}_report.pdf")
        pdf.output(file_path)

        return file_path

    except Exception as e:
        print(f"PDF generation failed: {e}")
        return None

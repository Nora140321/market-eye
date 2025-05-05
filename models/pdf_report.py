# models/pdf_report.py
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def create_pdf_report(ticker, max_price, min_price, average_price, predicted_price, recommendation, chart_image_path):
    output_path = os.path.join("reports", f"{ticker}_report.pdf")
    try:
        c = canvas.Canvas(output_path, pagesize=letter)
        width, height = letter

        c.setFont("Helvetica-Bold", 16)
        c.drawString(50, height - 50, f"{ticker} Stock Report")

        c.setFont("Helvetica", 12)
        c.drawString(50, height - 90, f"Max Close: ${max_price:.2f}")
        c.drawString(50, height - 110, f"Min Close: ${min_price:.2f}")
        c.drawString(50, height - 130, f"Average Close: ${average_price:.2f}")
        c.drawString(50, height - 150, f"Predicted Next Close: ${predicted_price:.2f}")

        c.drawString(50, height - 190, "Gemini Recommendation:")
        text = c.beginText(50, height - 210)
        text.setFont("Helvetica", 11)
        for line in recommendation.split('\n'):
            text.textLine(line)
        c.drawText(text)

        if os.path.exists(chart_image_path):
            c.drawImage(chart_image_path, 50, 100, width=500, preserveAspectRatio=True)

        c.save()
        return output_path
    except Exception as e:
        print(f"Failed to create PDF: {e}")
        return None

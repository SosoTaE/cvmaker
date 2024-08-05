from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

doc = SimpleDocTemplate("cv_reportlab.pdf", pagesize=letter)
story = []
styles = getSampleStyleSheet()

# Heading
heading_style = ParagraphStyle(' ', parent=styles['Heading1'], alignment=1, spaceAfter=12)  # Centered heading
story.append(Paragraph("Your Name", heading_style))
story.append(Spacer(1, 12))  # Add some space

# Contact Information
contact_style = ParagraphStyle('BodyText', parent=styles['Normal'], fontSize=10)
contact_data = [
    ["Email:", "your.email@example.com"],
    ["Phone:", "+1 (123) 456-7890"],
    ["Website:", "yourwebsite.com"]
]
contact_table = Table(contact_data)
contact_table.setStyle(TableStyle([
    ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),  # Set text color for all cells
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
]))
story.append(contact_table)
story.append(Spacer(1, 24))  # Add more space

# Sections (Experience, Education, Skills, etc.)
story.append(Paragraph("Experience", styles['Heading2']))
# ... add your experience details here ...

# More sections...

doc.build(story)

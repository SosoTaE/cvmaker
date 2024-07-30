from fpdf import FPDF

# Create FPDF object
pdf = FPDF()
pdf.add_page()

# Set fill color (optional)
pdf.set_fill_color(255, 0, 0)  # Red

# Draw a rectangle
pdf.rect(50, 50, 100, 50, 'F')  # x, y, width, height, 'F' for filled

# Save the PDF
pdf.output("rectangle.pdf", 'F')

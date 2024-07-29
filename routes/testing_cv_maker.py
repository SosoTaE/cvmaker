from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

pdf.cell(200, 10, txt="Hello, World!", ln=1, align="C")

pdf.set_font("Times", style="B", size=14)
pdf.cell(200, 10, txt="This is bold text.", ln=10)

pdf.set_font("Courier", size=10)
pdf.cell(200, 10, txt="This is Courier font.", ln=1)
pdf.multi_cell(100, 10, txt="This is some text that spans multiple lines.\nAnd another line...", align="R")

pdf.output("simple_text.pdf")

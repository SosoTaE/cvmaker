from fpdf import FPDF

import json


with open("./json_example.json", "r") as f:
    data = json.load(f)


def generate_cv(filename="my_cv.pdf", data=None):
    pdf = FPDF()
    for key, value in data.items():
        y = 72
        x = 0
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        if isinstance(value, list):
            for each in value:
                for each_key, each_val in each.items():
                    if not isinstance(each_key, str):
                        continue
                    pdf.set_xy(x, y)
                    pdf.cell(len(str(each_val)) * 6, 10, txt=str(each_val), ln=1, align="C")

                    y += 72
                    x += 6 * len(str(each_val))
        else:
            for each_key, each_val in value.items():
                if not isinstance(each_key, str):
                    continue
                pdf.set_xy(x, y)
                pdf.cell(len(str(each_val)) * 6, 10, txt=str(each_val), ln=1, align="C")
                y += 72
                x += 6 * len(str(each_val))

    pdf.output("simple_text.pdf")



generate_cv(filename="my_cv.pdf", data=data)

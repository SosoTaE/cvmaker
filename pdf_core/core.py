import json
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


class PDFDriver:
    def __init__(self, instruction, output_file):
        if not isinstance(instruction, dict):
            raise TypeError("instruction must be a dictionary")

        self.__instruction = instruction
        self.__canvas = canvas.Canvas(output_file, pagesize=A4)

    def __relative_y(self, y, height):
        return self.__canvas._pagesize[1] - y - height

    def __text(self, text_object):
        self.__canvas.setFillColorRGB(0, 0, 0, 1)

        if not isinstance(text_object, dict):
            raise TypeError("text_object must be a string")

        text = text_object.get("text")
        if not isinstance(text, dict):
            raise TypeError("text must be a dictionary")

        value = text.get("value")
        if not isinstance(value, str):
            raise TypeError("value must be a string")

        fontname = text.get("fontname")
        if not isinstance(fontname, str):
            raise TypeError("fontname must be a string")

        fontsize = text.get("fontsize")
        if not isinstance(fontsize, int):
            raise TypeError("fontsize must be a string")
        self.__canvas.setFont(fontname, size=fontsize)

        x = text_object.get("x")
        if not isinstance(x, float):
            raise TypeError("x must be a float")

        y = self.__relative_y(text_object.get("y"), fontsize * 1.2)
        if not isinstance(y, float):
            raise TypeError("y must be a float")

        self.__canvas.drawString(x, y, value)

    def __rect(self, rect_object):
        self.__canvas.setFillColorRGB(0, 0, 0, 1)

        if not isinstance(rect_object, dict):
            raise TypeError("rect_object must be a dictionary")

        rect = rect_object.get("rect")
        if not isinstance(rect, dict):
            raise TypeError("rect_object must be a dictionary")

        color = rect.get("color")
        if not isinstance(color, list) or len(color) != 4:
            raise TypeError("color must be a list of 4 elements (RGBA)")
        self.__canvas.setFillColorRGB(*color)

        size = rect_object.get("size")
        if not isinstance(size, dict):
            raise TypeError("size must be a dictionary")

        width = size.get("width")
        if not isinstance(width, float):
            raise TypeError("width must be a float")

        height = size.get("height")
        if not isinstance(height, float):
            raise TypeError("height must be a float")

        x = rect_object.get("x")
        if not isinstance(x, float):
            raise TypeError("x must be a float")

        y = self.__relative_y(rect_object.get("y"), height)
        if not isinstance(y, float):
            raise TypeError("y must be a float")

        fill = rect.get("fill")
        if not isinstance(fill, int):
            raise TypeError("fill must be a intf")

        self.__canvas.rect(x, y, width, height, fill=fill, stroke=0)

    def __line(self, line_object):
        if not isinstance(line_object, dict):
            raise TypeError("ln_object must be a dictionary")

        coordinates = line_object.get("coordinates")
        if not isinstance(coordinates, list):
            raise TypeError("coordinates must be a list")

        x1, y1, x2, y2 = coordinates

        size = line_object.get("size")
        if not isinstance(size, int):
            raise TypeError("size must be a int")

        self.__canvas.setLineWidth(size)
        self.__canvas.line(x1, y1, x2, y2)

    def __image(self, image_object):
        if not isinstance(image_object, dict):
            raise TypeError("No image object given")

        image = image_object.get("image")
        if not isinstance(image, dict):
            raise TypeError("image must be a dictionary")

        source = image.get("source")
        if not isinstance(source, str):
            raise TypeError("source must be a string")
        size = image_object.get("size")
        if not isinstance(size, dict):
            raise TypeError("size must be a dictionary")

        width = size.get("width")
        if not isinstance(width, float):
            raise TypeError("width must be a float")
        height = size.get("height")
        if not isinstance(height, float):
            raise TypeError("height must be a float")

        x = image_object.get("x")
        if not isinstance(x, float):
            raise TypeError("x must be a float")
        y = self.__relative_y(image_object.get("y"), height)
        if not isinstance(y, float):
            raise TypeError("y must be a float")

        self.__canvas.saveState()
        path = self.__canvas.beginPath()
        self.__canvas.setStrokeColorRGB(255, 255, 255, 0)
        path.circle(x + width / 2, y + height / 2, width / 2)
        self.__canvas.clipPath(path)
        self.__canvas.drawImage(source, x, y, width=width, height=height)
        self.__canvas.restoreState()

    def __multiline(self, multiline_object):
        self.__canvas.setFillColorRGB(0, 0, 0, 1)

        if not isinstance(multiline_object, dict):
            raise TypeError("multiline_object must be a dictionary")

        text = multiline_object.get("text")
        if not isinstance(text, dict):
            raise TypeError("text must be a dictionary")

        value = text.get("value")
        if not isinstance(value, str):
            raise TypeError("value must be a string")

        fontsize = text.get("fontsize")
        if not isinstance(fontsize, int):
            raise TypeError("fontsize must be a string")

        fontname = text.get("fontname")
        if not isinstance(fontname, str):
            raise TypeError("fontname must be a string")
        self.__canvas.setFont(fontname, size=fontsize)

        x = multiline_object.get("x")
        if not isinstance(x, float):
            raise TypeError("x must be a float")
        y = self.__relative_y(multiline_object.get("y"), 0)
        if not isinstance(y, float):
            raise TypeError("y must be a float")
        lines = value.split("\n")

        for line in lines:
            y -= fontsize * 1.2
            self.__canvas.drawString(x, y, line)

    def execute(self):
        pages = self.__instruction.get('pages')

        if not pages:
            raise ValueError("No objects found")

        for page in pages:

            objects = page.get('objects')

            if not objects:
                raise ValueError("No objects found")

            # draw objects
            for each in objects:
                object_type = each.get('type')

                if object_type == "text":
                    self.__text(each)

                if object_type == "image":
                    self.__image(each)

                if object_type == "rect":
                    self.__rect(each)

                if object_type == "line":
                    self.__line(each)

                if object_type == "multiline":
                    self.__multiline(each)

            self.__canvas.showPage()

    def output(self):
        self.__canvas.save()


if __name__ == "__main__":
    with open("instruction.json", "r") as f:
        instruction = json.load(f)

    pdf_object = PDFDriver(instruction, output_file="test.pdf")
    pdf_object.execute()
    pdf_object.output()

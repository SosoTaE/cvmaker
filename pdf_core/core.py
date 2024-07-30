import json

from fpdf import FPDF


class PDFDriver:
    def __init__(self, instruction):
        if not isinstance(instruction, dict):
            raise TypeError("instruction must be a dictionary")

        self.__instruction = instruction
        self.__pdf = FPDF()

    def __text(self, text_object):
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
        self.__pdf.set_font("Arial", size=fontsize)

        size = text_object.get("size")
        if not isinstance(size, dict):
            raise TypeError("size must be a dictionary")

        width = size.get("width")
        if not isinstance(width, int):
            raise TypeError("width must be a int")

        height = size.get("height")
        if not isinstance(height, int):
            raise TypeError("height must be a int")

        x = text_object.get("x")
        if not isinstance(x, int):
            raise TypeError("x must be a int")

        y = text_object.get("y")
        if not isinstance(y, int):
            raise TypeError("y must be a int")

        # set coordinate for text object
        self.__pdf.set_xy(x, y)

        align = text_object.get("align")
        if not isinstance(align, str):
            raise TypeError("align must be a string")

        self.__pdf.cell(width, height, txt=value, ln=1, align=align)

    def __image(self, image_object):
        if not isinstance(image_object, dict):
            raise TypeError("No image object given")

        image = image_object.get("image")
        if not isinstance(image, dict):
            raise TypeError("image must be a dictionary")

        source = image.get("source")
        if not isinstance(source, str):
            raise TypeError("source must be a string")

        x = image_object.get("x")
        if not isinstance(x, int):
            raise TypeError("x must be a int")
        y = image_object.get("y")
        if not isinstance(y, int):
            raise TypeError("y must be a int")

        size = image_object.get("size")
        if not isinstance(size, dict):
            raise TypeError("size must be a dictionary")

        width = size.get("width")
        if not isinstance(width, int):
            raise TypeError("width must be a int")
        height = size.get("height")
        if not isinstance(height, int):
            raise TypeError("height must be a int")

        self.__pdf.image(source, x=x, y=y, w=width, h=height)

    def execute(self):
        pages = self.__instruction.get('pages')

        if not pages:
            raise ValueError("No objects found")

        for page in pages:

            objects = page.get('objects')

            if not objects:
                raise ValueError("No objects found")

            # add page
            self.__pdf.add_page()

            # draw objects
            for each in objects:
                object_type = each.get('type')

                if object_type == "text":
                    self.__text(each)
                elif object_type == "image":
                    self.__image(each)

    def output(self, filename):
        self.__pdf.output(filename, 'F')


if __name__ == "__main__":
    with open("instuction.json", "r") as f:
        instruction = json.load(f)

    pdf_object = PDFDriver(instruction)
    pdf_object.execute()
    pdf_object.output("test2.pdf")

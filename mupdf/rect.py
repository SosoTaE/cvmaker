import fitz


# create rectangle
rect = fitz.Rect(56, 56, 156, 156)

# insert image
page.insert_image(rect, stream=img)
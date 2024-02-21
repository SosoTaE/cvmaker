# import fitz  # Import the fitz library
#
# # Function to wrap text
# def wrap_text(text, fontname, fontsize, max_width):
#     words = text.split()
#     wrapped_lines = []
#     current_line = ""
#     for word in words:
#         # Check if adding the next word exceeds the max width
#         test_line = f"{current_line} {word}".strip()
#         text_width = fitz.getTextlength(test_line, fontname, fontsize)
#         if text_width <= max_width:
#             current_line = test_line
#         else:
#             # If the line is too wide, start a new line
#             wrapped_lines.append(current_line)
#             current_line = word
#     wrapped_lines.append(current_line)  # Add the last line
#     return wrapped_lines
#
# doc = fitz.open()
# page = doc.new_page()
#
# # Define the text to add and text parameters
text = "In this corrected version, the insert_text method now correctly uses a tuple (x, y) directly for the text position, instead of using origin as a keyword argument. This should resolve the TypeError you encountered and allow your script to run successfully, creating the PDF as intended."
# fontname = "helv"
# fontsize = 12
# color = (0, 0, 0)
# x, y = 50, 100  # Starting position of the text
# max_width = 500  # Maximum width of the text block
#
# # Wrap text
# wrapped_text = wrap_text(text, fontname, fontsize, max_width)
#
# # Add the wrapped text to the page
# for line in wrapped_text:
#     page.insert_text((x, y), line, fontname=fontname, fontsize=fontsize, color=color)
#     y += fontsize * 1.5  # Move to the next line, adjust spacing as needed
#
# # Save the document to a file
# doc.save("hello_world_wrapped.pdf")
#
# # Close the document
# doc.close()
#
# # print

import fitz  # Make sure to import fitz (PyMuPDF)

doc = fitz.open()  # Create a new document
page = doc.new_page()  # Add a new page
rect = fitz.Rect(50, 100, 200, 200)  # Define a rectangle for the text
page.draw_rect(rect, color=(0,0,1), fill=(1,0,0))  # fill parameter colors the inside


# Create a TextWriter object for the page
tw = fitz.TextWriter(page.rect)
# Add text within the specified rectangle, with optional attributes like font size
tw.fill_textbox(rect, text, fontsize=11, align=0)  # Alignment, font, etc., can be adjusted
# Write the text to the page
tw.write_text(page)

doc.save("your_output.pdf")  # Save your document
doc.close()


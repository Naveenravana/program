from PIL import Image
import pytesseract

Quotes = "Quotes.jpeg"

img_obj = Image.open(Quotes)

text_1 = pytesseract.image_to_string(img_obj)
print(text_1)

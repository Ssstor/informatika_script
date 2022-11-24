import pytesseract
from PIL import Image

img = Image.open('rus_text.jpg')

file_name = img.filename
file_name = file_name.split('.')[0]

custom_config = r'--oem 3 --psm 6'

text = pytesseract.image_to_string(img, lang='rus', config=custom_config)
print(text)

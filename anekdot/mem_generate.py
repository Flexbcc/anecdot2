import json
from PIL import Image, ImageDraw, ImageFont

image = Image.open("Frame 9 (1).png")

font = ImageFont.truetype("arial.ttf", 25)
drawer = ImageDraw.Draw(image)
drawer.text((50, 100), "Hello World!\nПривет мир!", font=font, fill='black')

image.save('new_img.jpg')
image.show()

# def json_load(file_name):
#     with open(file_name, 'r') as file:
#         links = json.load(file)
#         return links
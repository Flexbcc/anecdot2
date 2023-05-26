import textwrap

from PIL import Image, ImageDraw, ImageFont

# image = Image.open("Frame 9 (1).png")
# rgb_im = image.convert('RGB')
# rgb_im.save('Frame 9 (1).jpg')
image = Image.open("shablon.jpeg")
print(image.height)
print(image.width)
text1 = "— А123123123123 я вот себе машинку присмотрела классненькую, буду брать.\n" \
        "— Ниче себе! Покажи место, где ты деньги берешь, я тоже хочу!\n" \
        "— Нету, Вася, у тебя такого места, нету!"
ttf = "/Users/admin/PycharmProjects/anekdot/Bowler.ttf"
font = ImageFont.truetype(ttf, 25)
w, h = font.getsize(text1)
print(w, h)
drawer = ImageDraw.Draw(image)

MAX_W, MAX_H = 1200, 720
im = Image.open("shablon2.jpeg")
draw = ImageDraw.Draw(im)

novo = textwrap.wrap(text1, width=60)

current_h, pad = 100, 10
for liner in novo:
    w, h = draw.textsize(liner, font=font)
    draw.text(((MAX_W - w) / 2, current_h), liner, font=font , fill='black')
    if liner.find('\n'):
        print(liner)
        draw.text(((MAX_W - w) / 2, current_h), '\n\n', font=font , fill='black')
        print('dsfdsf')
    current_h += h + pad

im.save('tes1t.png')

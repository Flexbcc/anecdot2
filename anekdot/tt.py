from PIL import Image, ImageDraw, ImageFont

im = Image.new("RGB", (500, 200), "#fff")
box = ((10, 10, 490, 190))
draw = ImageDraw.Draw(im)
draw.rectangle(box, outline="#000")
ttf = "/Users/admin/PycharmProjects/anekdot/Bowler.ttf"
text = "— А123123123123 я вот себе машинку присмотрела классненькую, буду брать.\n" \
        "— Ниче себе! Покажи место, где ты деньги берешь, я тоже хочу!\n" \
        "— Нету, Вася, у тебя такого места, нету!"
# font = ImageFont.truetype(ttf, 25)
font_size = 100
size = None
while (size is None or size[0] > box[2] - box[0] or size[1] > box[3] - box[1]) and font_size > 0:
    font = ImageFont.truetype(ttf, font_size)
    size = font.getsize_multiline(text)
    font_size -= 1
draw.multiline_text((box[0], box[1]), text, "#000", font)
im.save("out.png")

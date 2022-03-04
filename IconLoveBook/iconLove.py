# coding:utf-8

from PIL import Image, ImageDraw, ImageFont

img_child_size = 15
img_times=5
text = "摸鱼办提醒您"
font = ImageFont.truetype('AliPuHui-Bold.ttf', img_child_size)
img_path = './testX.jpg'

img = Image.open(img_path)
w,h=img.size
thumb_size = (w/img_times, h/img_times)
img.thumbnail(thumb_size)
img_w, img_h = ((img.size))
print("img.size:",img.size);
img_child = Image.new("RGB", (img_child_size, img_child_size))
img_ans = Image.new("RGB", (int(img_w)*img_child_size,  int(img_h)*img_child_size))

text_w, text_h = font.getsize("中")  # 获单个文字的宽、高
print("font.size:",font.getsize("中"));
offset_x = (img_child_size - text_w) >> 1  # 文字水平居中
offset_y = (img_child_size - text_h) >> 1  # 文字垂直居中
print("offset:",(offset_x,offset_y))

char_index = 0
draw = ImageDraw.Draw(img_child)  # 小图的绘图对象，用于绘制文字

for x in range(int(img_w)):  # 宽在外 高在内，因此文字的方向是从左到右，从上到下排列的
    for y in range(int(img_h)):
        draw.rectangle((0, 0, img_child_size, img_child_size), fill='lightgray')  # 绘制背景，看起来会好一些
        draw.text((offset_x, offset_y), text[char_index], font=font, fill=img.getpixel((x, y)))  # 用（x,y）处像素点的色值绘制字体
        img_ans.paste(img_child, (x*img_child_size , y*img_child_size ))
        char_index = (char_index + 1) % len(text)

img_ans.save('testX-text.png')
print("over:")
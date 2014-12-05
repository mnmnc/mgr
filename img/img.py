from PIL import Image, ImageDraw
import sys

im = Image.open("1.jpg")


for i in range(100):
	x, y = (i,i)
	print(im.getpixel((x,y)))

draw = ImageDraw.Draw(im)
draw.line((0, 0) + im.size, fill=(255, 255, 255))
del(draw)

im.save("5.jpg")



from PIL import Image, ImageDraw

# Создаем белый квадрат
img = Image.new('RGBA', (4096, 4096), (255, 255, 255))
idraw = ImageDraw.Draw(img)

x = 0
y = 0
red = 0
blue = 0
green = 0

for i in range(16777216):
    idraw.point((x, y), fill=(red, green, blue))
    x += 1
    red += 1
    if red > 255:
        green += 1
        red = 0
        if green > 255:
            blue += 1
            green = 0
    if x > 4095:
        x = 0
        y += 1

img.save('rectangle.png')
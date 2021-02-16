from PIL import Image
from PIL import ImageColor

img = Image.open('sumoringer.png')

print("format: " +img.format)
print("size: " +str(img.size))

#img.save("test.png")

width, height = img.size
print("wdith: " + str(width))
print("height: " + str(height))

print(img.getpixel((10,10)))

#red=255,0,0,255
#yellow = 

for i in range(width):
    for j in range(height):
        if(img.getpixel((i,j))==(0,0,0,255)):
            print("true")
            newPixel=(ImageColor.getcolor('yellow','RGBA'))
            img.putpixel((i,j),newPixel)
        else:
            print("not true")

img.save("yellow.png")

print(ImageColor.getcolor('yellow','RGBA'))

#https://automatetheboringstuff.com/2e/chapter19/
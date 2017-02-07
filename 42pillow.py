from PIL import Image

img = Image.open("Activity.PNG")
print(img.size)
print(img.format)
area = (100,100,300,200)
cropped_image = img.crop(area)
cropped_image.show()




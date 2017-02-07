from PIL import Image

img = Image.open("Activity.PNG")
print(img.size)
print(img.format)
img.show()


from PIL import Image
activity = Image.open("communication.PNG")
cls = Image.open("class.PNG")

area = (100, 100, 500, 500)
activity.paste(cls, area)

activity.show()

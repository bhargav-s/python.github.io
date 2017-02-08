from PIL import Image
from PIL import ImageFilter

new_img1 = Image.open("Activity.PNG")
black_white = new_img1.convert("L")
blur = new_img1.filter(ImageFilter.BLUR)
Detail = new_img1.filter(ImageFilter.DETAIL)
edges = new_img1.filter(ImageFilter.FIND_EDGES)

#blur.show()
#Detail.show()
edges .show()

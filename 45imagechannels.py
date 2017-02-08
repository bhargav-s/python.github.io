from  PIL import Image

test = Image.open("Activity.PNG")
test2 = Image.open("class.PNG")
print(test.mode)
r1, g1, b1, a1 = test.split()
r2, g2, b2, a2 = test2.split()

#new_img = Image.merge("RGBA",(a1, g2, r1, b1))
new_img1 = test.transpose(Image.FLIP_TOP_BOTTOM)
new_img2 = test.transpose(Image.ROTATE_90)

#new_img.show()
#new_img1.show()
new_img2.show()
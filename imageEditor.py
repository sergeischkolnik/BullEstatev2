from PIL import Image

im=Image.open(r"C:\Users\serge\Pictures\9145172050.jpg")
width, height = im.size
# Setting the points for cropped image
left = width / 4
top = height / 4
right = 3* width / 4
bottom = 3* height / 4

# Cropped image of above dimension
# (It will not change orginal image)
im1 = im.crop((left, top, right, bottom))

im1.show()
# Shows the image in image viewer
im1.save("geeks.jpg")

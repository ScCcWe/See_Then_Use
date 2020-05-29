from PIL import Image


img = Image.open('dog.jpg')
print(img.format)
print(img.mode)
print(img.size)

img_resize = img.resize((32, 32))
img_resize.save('test_2.ico')

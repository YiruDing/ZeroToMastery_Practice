from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')
# filtered_img = img.filter(ImageFilter.BLUR)
filtered_img = img.convert('L')
filtered_img.save("blur.png", 'png')
# Why converted to png? Because png support these filter.

# print(dir(img)) will print its dictionary
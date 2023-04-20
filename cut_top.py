from PIL import Image

img = Image.open('start.png')
w, h = img.size
img_crop = img.crop((w*0.035,h*0.11,w-w*0.035,h)) # режем картинку 10% сверху, и по краям на 3,5%
black = img_crop.convert("L").save('first_cut.png')

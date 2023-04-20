from PIL import Image, ImageFilter


# Open image
img = Image.open("first_cut.png")

# Resize smoothly down to 16x16 pixels

black = img.convert("L")
porog = 150
img_porog = black.point(lambda x: 255 if x > porog else 0)
imgSmall = img_porog.resize((256,1024), resample=Image.Resampling.BILINEAR)

# Scale back up using NEAREST to original size
result = imgSmall.resize(img.size, Image.Resampling.NEAREST)
smooth = result.filter(ImageFilter.BoxBlur(65)) #ТУТ МЫ ВЫСТАВЛЯЕМ СТЕПЕНЬ РАЗМЫТИЯ

after_smooth = smooth.resize((256,1024), resample=Image.Resampling.BILINEAR)
final0 = after_smooth.resize(img.size, Image.Resampling.NEAREST)

after_final0 = final0.resize((256,256), resample=Image.Resampling.BILINEAR)
final1 = after_final0.resize(img.size, Image.Resampling.NEAREST)



final1.save("blur.png")



# from PIL import ImageFilter
# from PIL import Image



# img = Image.open("first_cut.png")
# kraya = img.convert("L")
# smoth = kraya.filter(ImageFilter.SMOOTH)
# blurred_image = smoth.filter(ImageFilter.BoxBlur(15)).show()


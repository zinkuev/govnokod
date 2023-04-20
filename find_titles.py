###ЭТОТ КОД НАХОДИТ ГРАНИЦЫ ЗАГОЛОВКОК, САМАЯ СТАБИЛЬНАЯ ВЕРСИЯ

import cv2
from pytesseract import pytesseract

path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.tesseract_cmd = path_to_tesseract

img = cv2.imread("blur.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU |
                                          cv2.THRESH_BINARY_INV)
# cv2.imwrite('threshold_image.jpg',thresh1)

rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (12, 12))

dilation = cv2.dilate(thresh1, rect_kernel, iterations = 2)
# cv2.imwrite('dilation_image.jpg',dilation)

contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
                                            cv2.CHAIN_APPROX_NONE)

im2 = img.copy()

for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    if (w > 400): #если ширина обнаруженной области больше 400 пикселей(чуть меньше 1 столбца газеты)
        # print(x,y, w)

        if(x + w < 1503):
            print("находится слева")
        else:
            print("находимся справа")
        if (w < 601):
            print("занимает 1 столбец")
        elif(w > 601 and w < 1202):
            print("занимает 2  столбца")
        elif(w > 1202 and w < 1803):
            print("занимает 3  столбца")
        elif(w > 1803 and w < 2404):
            print("занимает 4  столбца")
        else:
            print("занимает 5  столбцов")

        # Рисуем ограничительную рамку на текстовой области
        rect=cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # Обрезаем область ограничительной рамки
        cropped = im2[y:y + h, x:x + w]
        cv2.imwrite('rectanglebox.jpg',rect)
    
    


import cv2

# Görüntüyü yükle
image = cv2.imread('kisi.jpeg')

# Gaussian Blur uygula
#blurlaştırma oranı tek sayı olmalı
blurred = cv2.GaussianBlur(image, (41, 41), 0) 

# Sonucu göster
cv2.imshow('Bulanık', blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()

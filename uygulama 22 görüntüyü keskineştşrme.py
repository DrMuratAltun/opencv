import cv2
import numpy as np

# Görüntüyü yükle
image = cv2.imread('kisi.jpeg')

# Keskinleştirme kernel'i oluştur
# Daha güçlü keskinleştirme için katsayıları artır
kernel_sharpening = np.array([[-1, -1, -1],
                             [-1,  9, -1],
                             [-1, -1, -1]])

# Kernel ile konvolüsyon yaparak keskinleştirme uygula
sharpened = cv2.filter2D(image, -1, kernel_sharpening)

# Sonucu göster
cv2.imshow('Sharpened Image', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()

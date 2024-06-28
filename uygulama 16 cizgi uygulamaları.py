import cv2
import numpy as np

# Boş bir tuval oluştur (500x500 piksel, 3 kanal, beyaz arka plan)
tuval = np.ones((500, 500, 3), dtype="uint8") * 255

# Kırmızı renkte ince bir çizgi
cv2.line(tuval, (10, 10), (490, 10), (0, 0, 255), thickness=1)

# Yeşil renkte orta kalınlıkta bir çizgi
cv2.line(tuval, (10, 50), (490, 50), (0, 255, 0), thickness=3)

# Mavi renkte kalın bir çizgi
cv2.line(tuval, (10, 100), (490, 100), (255, 0, 0), thickness=5)

# RGB renklerde farklı kalınlıklarda çizgiler
cv2.line(tuval, (10, 150), (490, 150), (255, 0, 0), thickness=2)  # Kırmızı
cv2.line(tuval, (10, 200), (490, 200), (0, 255, 0), thickness=4)  # Yeşil
cv2.line(tuval, (10, 250), (490, 250), (0, 0, 255), thickness=6)  # Mavi

# Renkli çizgiler
for i in range(10, 501, 10):
    renk = (i % 256, (i * 2) % 256, (i * 3) % 256)  # Değişen renk değerleri
    cv2.line(tuval, (i, 300), (i, 400), renk, thickness=2) # Koordinatlar (x1,y1), (x2,y2) ve kalınlık değeri

# Tuvali göster
cv2.imshow("Cizgili Tuval", tuval)
cv2.waitKey(0)
cv2.destroyAllWindows()

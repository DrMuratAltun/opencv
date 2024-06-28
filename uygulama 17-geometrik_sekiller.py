import cv2
import numpy as np

# Boş bir tuval oluştur (500x500 piksel, 3 kanal, beyaz arka plan)
tuval = np.ones((500, 500, 3), dtype="uint8") * 255

# İçi dolu bir kare çiz
cv2.rectangle(tuval, (50, 50), (150, 150), (255, 0, 0), -1)  # Mavi, içi dolu

# İçi boş bir kare çiz
cv2.rectangle(tuval, (200, 50), (300, 150), (0, 255, 0), 3)  # Yeşil, 3 piksel kalınlık

# İçi dolu bir daire çiz
cv2.circle(tuval, (100, 300), 50, (0, 0, 255), -1)  # Kırmızı, içi dolu

# İçi boş bir daire çiz
cv2.circle(tuval, (300, 300), 50, (255, 255, 0), 3)  # Sarı, 3 piksel kalınlık


# İçi dolu bir üçgen çiz
pts2 = np.array([[150, 400], [100, 500], [200, 500]], np.int32)
cv2.fillPoly(tuval, [pts2], (255, 0, 255))  # Pembe, içi dolu

# Bir üçgen çiz
pts = np.array([[250, 400], [300, 500], [200, 500]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.polylines(tuval, [pts], True, (0, 255, 255), 3)  # Sarı, 3 piksel kalınlık


# Tuvali göster
cv2.imshow("Geometrik Şekiller", tuval)
cv2.waitKey(0)
cv2.destroyAllWindows()

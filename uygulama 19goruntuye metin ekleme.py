import cv2
import numpy as np

# Boş bir tuval oluştur
tuval = np.ones((500, 800, 3), dtype="uint8") * 255

# Font tipleri
fontlar = [cv2.FONT_HERSHEY_SIMPLEX, cv2.FONT_HERSHEY_COMPLEX, 
           cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, cv2.FONT_HERSHEY_PLAIN]

# Metinleri ve stillerini belirle
metinler = ["MEB YEGITEK", "Hello World!", "Python", "OpenCV"]
font_olcekleri = [1, 1.5, 2, 1.2]  # Font boyutları
renkler = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 0, 0)]  # BGR formatında renkler
kalinliklar = [2, 3, 4, 2]  # Çizgi kalınlıkları

# Metinleri tuval üzerine çiz
for i in range(len(metinler)):
    cv2.putText(tuval, metinler[i], (50, 50 + i * 100), fontlar[i % len(fontlar)], 
                font_olcekleri[i % len(font_olcekleri)], renkler[i % len(renkler)], 
                kalinliklar[i % len(kalinliklar)])

# Tuvali göster
cv2.imshow("Metinli Tuval", tuval)
cv2.waitKey(0)
cv2.destroyAllWindows()

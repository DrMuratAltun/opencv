import cv2
import numpy as np

def draw_circles(canvas, center, radius, depth):
    if depth > 0:
        # Daire çiz
        cv2.circle(canvas, center, radius, (255 - depth * 20, depth * 20, depth * 10), 1)

        # Yeni yarıçap ve derinlik değerleriyle dört yeni daire çiz
        new_radius = radius // 2
        draw_circles(canvas, (center[0] - new_radius, center[1]), new_radius, depth - 1)
        draw_circles(canvas, (center[0] + new_radius, center[1]), new_radius, depth - 1)
        draw_circles(canvas, (center[0], center[1] - new_radius), new_radius, depth - 1)
        draw_circles(canvas, (center[0], center[1] + new_radius), new_radius, depth - 1)

# Boş bir tuval oluştur
tuval = np.ones((600, 600, 3), dtype="uint8") * 255

# Fraktal daireleri çiz
draw_circles(tuval, (300, 300), 200, 5)

# Tuvali göster
cv2.imshow("Basit Dairesel Fraktal", tuval)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2

# Read video file
cap = cv2.VideoCapture("188595_pixabay.mp4")

# Video kontrolü
if not cap.isOpened():
    print("Dosyayı kontrol edin")
    exit(1)

# Videoyu kare kare oku
while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Video karesini gri tonlara çevir
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Video karesini göster
    cv2.imshow("Frame", gray)

    # Çıkmak için 'q' tuşuna basınız
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Kaynakları serbest bırak
cap.release()
cv2.destroyAllWindows()


# Video çözünürlüğünü al
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Video kaydetme için VideoWriter nesnesi oluştur
out = cv2.VideoWriter('gri_tonlu_video.avi', cv2.VideoWriter_fourcc('M','J','P','G'), 
                      10, (frame_width, frame_height), False)
import cv2

# Haar Cascade dosyasını yükle
face_cascade = cv2.CascadeClassifier("models\haarcascade_frontalface_default.xml")

# Videodan çerçeveleri okuyun
cap = cv2.VideoCapture(0)

# Çerçeveleri işleyin
while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Yüzleri tespit edin
    faces = face_cascade.detectMultiScale(
        frame,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE,
    )

    # Her yüzü bir kutu ile çevreleyin
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Çerçeveyi gösterin
    cv2.imshow("Frame", frame)

    # Çıkış için q tuşuna basın
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Kaynakları serbest bırak
cap.release()
cv2.destroyAllWindows()

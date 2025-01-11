face_cap = cv2.CascadeClassifier("haarcascade_frontalface.xml")
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    col = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    face = face_cap.detectMultiScale(
        col,
        scaleFactor = 1.1,
        minNeighbors = 5,
        minSize = (30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE )
    for (x,y,w,h) in face:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow("Webcam", frame)
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()

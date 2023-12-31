import cv2
import dlib

# Initialize webcam
cap = cv2.VideoCapture(0)

# Initialize face detector and facial landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")  # You need to download this file

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    # If faces are detected, do nothing; else, blur the frame
    if not faces:
        try:
            frame = cv2.GaussianBlur(frame, (21, 21), 65)
        except:
            continue
    else:
        for face in faces:
            landmarks = predictor(gray, face)


    # Display the resulting frame
    cv2.imshow('Frame', frame)

    # Break the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

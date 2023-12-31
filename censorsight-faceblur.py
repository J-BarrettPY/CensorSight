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

    # Check if any faces are detected
    if len(faces) == 0:
        # Apply Gaussian blur to entire frame
        try:
            frame = cv2.GaussianBlur(frame, (99, 99), 15)
        except:
            continue
    else:
        for face in faces:
            # Get the coordinates of the face rectangle
            x1 = face.left()
            y1 = face.top()
            x2 = face.right()
            y2 = face.bottom()

            # Extract the face region from the frame
            face_region = frame[y1:y2, x1:x2]

            try:
                # Apply a Gaussian blur to this face region
                blurred_face = cv2.GaussianBlur(face_region, (99, 99), 15)
            except:
                continue

            # Put the blurred face region back into the frame
            frame[y1:y1+blurred_face.shape[0], x1:x1+blurred_face.shape[1]] = blurred_face

    # Display the resulting frame with the face blurred (or entire frame if no face)
    cv2.imshow('Frame', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture and destroy all windows
cap.release()
cv2.destroyAllWindows()

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

    # Flag to check if rectangle is drawn
    rectangle_drawn = False

    for face in faces:
        landmarks = predictor(gray, face)

        # Identify the extreme points
        min_x = min([landmarks.part(n).x for n in range(36, 48)]) - 30  # Subtract value to extend left side of the rectangle
        max_x = max([landmarks.part(n).x for n in range(36, 48)]) + 30  # Add value to extend right side of the rectangle
        min_y = min([landmarks.part(n).y for n in range(36, 48)]) - 15  # Buffer above topmost eye landmark
        max_y = max([landmarks.part(n).y for n in range(36, 48)]) + 15  # Buffer below bottommost eye landmark

        # Draw a rectangle over the eyes
        try:
            cv2.rectangle(frame, (min_x, min_y), (max_x, max_y), (0, 0, 0), -1)
        except:
            continue

        # Set flag to True as rectangle is drawn
        rectangle_drawn = True

    # Blur the entire frame if no rectangle is drawn
    if not rectangle_drawn:
        try:
            frame = cv2.GaussianBlur(frame, (21, 21), 65)
        except:
            continue

    # Display the resulting frame with rectangles or blurred
    cv2.imshow('Frame', frame)

    # Break the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

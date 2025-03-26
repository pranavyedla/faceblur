import cv2

# Load the Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    # Read frame from webcam
    check, frame = cap.read()
    if not check:
        print("Failed to capture image")
        break
    
    # Flip frame horizontally for a mirror effect
    frame = cv2.flip(frame, 1)
    
    # Convert to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    
    # Blur each detected face
    for (x, y, w, h) in faces:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        frame[y:y+h, x:x+w] = cv2.GaussianBlur(frame[y:y+h, x:x+w], (99, 99), 30)
    
    # Display face count on the frame
    cv2.putText(frame, f'Faces: {len(faces)}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # Show the frame using OpenCV
    cv2.imshow("Blur Faces", frame)

    # Press 't' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('t'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()

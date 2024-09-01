import cv2
import os

# Initialize the camera
cam = cv2.VideoCapture(0)  # Standard parameter to use the default camera
cam.set(3, 640)  # Set the width
cam.set(4, 480)  # Set the height

# Load the face detection model
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Get the user ID
face_id = input('\n Enter user id and press enter: ')

print("\n [INFO] Initializing face capture. Look at the camera and wait ...")

# Initialize the count of captured images
count = 0

# Start capturing the video frame by frame
while True:
    ret, img = cam.read()

    if not ret:
        print("[ERROR] Failed to capture image. Exiting...")
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        count += 1
        # Save the captured image into the dataset folder
        cv2.imwrite("Dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h, x:x+w])
        cv2.imshow('image', img)

    # Press 'ESC' for exiting the video or wait until the count reaches 30
    k = cv2.waitKey(100) & 0xff
    if k == 27:  # 27 is the ESC key
        break
    elif count >= 30:
        break

# Cleanup and close everything
print("\n [INFO] Exiting program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()

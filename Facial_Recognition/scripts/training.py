import cv2
import numpy as np
from PIL import Image
import os

# Path to the dataset
path = 'dataset'

# Initialize the LBPH face recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()
# Load the face detection model
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def getImagesAndLabels(path):
    # Get the paths of all the files in the dataset directory
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faceSamples = []
    ids = []

    # Loop through all the image paths
    for imagePath in imagePaths:
        # Convert the image to grayscale
        PIL_img = Image.open(imagePath).convert('L')
        img_numpy = np.array(PIL_img, 'uint8')

        # Extract the ID from the image path
        id = int(os.path.split(imagePath)[-1].split(".")[1])
        # Detect faces in the image
        faces = detector.detectMultiScale(img_numpy)

        # Loop through all the faces found
        for (x, y, w, h) in faces:
            faceSamples.append(img_numpy[y:y+h, x:x+w])
            ids.append(id)

    return faceSamples, ids


print("\n [INFO] Training faces ... ")

# Get the faces and IDs from the dataset
faces, ids = getImagesAndLabels(path)
# Train the recognizer on the faces and IDs
recognizer.train(faces, np.array(ids))

# Save the trained model
recognizer.write("Trainer/trainer.yml")

print("\n [INFO] {0} faces trained.".format(len(np.unique(ids))))

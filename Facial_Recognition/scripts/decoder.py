# loading training data and training the model 

# for simple purposes the trainig data is filled with my images

from pathlib import Path
import face_recognition
import pickle
import os
from collections import Counter

# Get the directory where the script is located
script_dir = Path(__file__).parent.resolve()

# Ensure the output directory exists
output_dir = script_dir / "output"
output_dir.mkdir(parents=True, exist_ok=True)

# Specify the default encodings path relative to the script location
DEFAULT_ENCODINGS_PATH = output_dir / "encodings.pkl"

# Print the current working directory and the script directory for verification
print("Current Working Directory:", os.getcwd())
print("Script Directory:", script_dir)
print("Encodings Path:", DEFAULT_ENCODINGS_PATH)

# Check if the encodings file exists
if not DEFAULT_ENCODINGS_PATH.exists():
    print(f"Encodings file does not exist: {DEFAULT_ENCODINGS_PATH}")
else:
    print(f"Encodings file found: {DEFAULT_ENCODINGS_PATH}")

# dont need cs already created manually
#Path("train").mkdir(exist_ok=True)
#Path("output").mkdir(exist_ok=True)
#Path("validation").mkdir(exist_ok=True)


""" This function uses a for loop to go through each 
directory within training/, saves the label from each 
directory into name, then uses the load_image_file() 
function from face_recognition to load each image.
As an input it requires a model type and a location to save the encodings
will be generated for each image"""


def encode_known_faces(
        model: str="hog", encodings_location: Path = DEFAULT_ENCODINGS_PATH
) -> None:
    names = []
    encodings =[]
    for filepath in Path("train").glob("*/*"):
        name = filepath.parent.name
        image = face_recognition.load_image_file(filepath)

        # now we want to add all encodings to separte lists 
        face_location = face_recognition.face_locations(image, model=model)
        face_encodings = face_recognition.face_encodings(image, face_location)

        for encoding in face_encodings:
            names.append(name)
            encodings.append(encoding)
            # now we use pickle to save the name-encoding 
            # dictionary
        name_encodings = {"names": names, "encodings": encodings}
        with encodings_location.open(mode="wb") as f:
            pickle.dump(name_encodings, f)


encode_known_faces()

# now we need a funciton to recognize unlabeled faces
def recognize_faces(
    image_location: str,
    model: str = "hog",
    encodings_location: Path = DEFAULT_ENCODINGS_PATH,
) -> None:
    with encodings_location.open(mode="rb") as f:
        loaded_encodings = pickle.load(f)

    input_image = face_recognition.load_image_file(image_location)
    
    input_face_locations = face_recognition.face_locations(
        input_image, model=model
    )
    input_face_encodings = face_recognition.face_encodings(
        input_image, input_face_locations
    )
    for bounding_box, unknown_encoding in zip(
        input_face_locations, input_face_encodings
    ):
        name = _recognize_face(unknown_encoding, loaded_encodings)
        if not name:
            name = "Unknown"
        print(name, bounding_box)


def _recognize_face(unknown_encoding, loaded_encodings):
    boolean_matches = face_recognition.compare_faces(
        loaded_encodings["encodings"], unknown_encoding
    )
    votes = Counter(
        name
        for match, name in zip(boolean_matches, loaded_encodings["names"])
        if match
    )
    if votes:
        return votes.most_common(1)[0][0]
    

recognize_faces("images.jpeg")

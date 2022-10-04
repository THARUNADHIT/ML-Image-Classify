from keras.models import model_from_json
from keras.models import Sequential
import numpy as np
from keras.preprocessing import image
import os

file = open('model.json', 'r')
model = Sequential()
loaded = file.read()
file.close()
model = model_from_json(loaded)
model.load_weights('model.h5')
print("Loaded model from disk")

def classify(img):
    img_name = img
    test_image = image.load_img(img_name, target_size=(64, 64))
    test_image1 = image.img_to_array(test_image)
    test_image2 = np.expand_dims(test_image1, axis=0)
    result = model.predict(test_image2)

    if result[0][0] == 1:
        prediction = "Tony stark"
    else:
        prediction = "Harry potter"
    print(prediction, img_name)

path = 'C:\\Users\\ELCOT\\PycharmProjects\\Image classify\\Dataset\\Test'
files = []
for r, d, f in os.walk(path):
    for file in f:
        if '.jpeg' in file:
            files.append(os.path.join(r, file))

for f in files:
    classify(f)
    print("\n")

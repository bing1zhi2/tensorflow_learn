import numpy as np

from keras.preprocessing import image
from keras.models import load_model


model = load_model('1_exercise.h5')

# predicting images
path = 'E:/dataset/cat_dogs/cats-v-dogs/testing/cats/3.jpg'
img = image.load_img(path, target_size=(150, 150))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)

images = np.vstack([x])
classes = model.predict(images, batch_size=10)
print(classes[0])
if classes[0] > 0.5:
    print(" is a dog")
else:
    print(" is a cat")
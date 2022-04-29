from manual_rps import get_winner, get_computer_choice

import cv2
from keras.models import load_model
import numpy as np
model = load_model('converted_keras/keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
countdown = 10


while countdown > 0: 
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    result = get_winner(np.argmax(model.predict(data)), get_computer_choice())
    cv2.imshow('frame', frame)
    countdown -= 1
    # Press q to close the window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
print(result)            
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()
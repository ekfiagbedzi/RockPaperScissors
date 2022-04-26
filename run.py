import cv2
from keras.models import load_model
import numpy as np
import random
model = load_model('converted_keras/keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
opts = np.array([0, 1, 2, 3])
cpu_opt = random.choice(opts)

while True: 
    ret, frame = cap.read()
    cv2.putText(frame, "Hello World!!!", (200, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame)
    # Press q to close the window
    print(prediction)
    prediction = np.argmax(prediction)

    if cv2.waitKey(120) & 0xFF == ord('q'):
        break
print(prediction)
print(cpu_opt)
if prediction == cpu_opt:
    print("Its a draw game")
elif prediction > cpu_opt:
    print("You won!!!")
else:
    print("You lost")
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()
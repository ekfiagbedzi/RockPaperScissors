import cv2
import time
import random
import numpy as np
from keras.models import load_model
model = load_model('converted_keras/keras_model.h5')
opts = np.array([0, 1, 2, 3])
cpu_opt = random.choice(opts)
font = cv2.FONT_HERSHEY_SIMPLEX


def RockPaperScissorsGame():

    TIMER = int(5)
    OPTIONS = ["ROCK", "PAPER", "SCISSORS", ""]
    a = 0
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)


    n_rounds = 0
    cpu_wins = 0
    user_wins = 0
    while n_rounds < 3:
        ret, img = cap.read()
        cv2.imshow("frame", img)

        k = cv2.waitKey(1)
        cv2.putText(img, "CPU = {}".format(cpu_wins),
        (200, 250), font, 7, (0, 255, 255), 4, cv2.LINE_AA)
        if k == ord("q"):
            prev = time.time()


            for i in OPTIONS:
                ret, frame = cap.read()
                cv2.putText(frame, i,
                (200, 250), font,
                7, (0, 255, 255),
                4, cv2.LINE_AA)

                cv2.imshow("frame", frame)
                cv2.waitKey(125)

                cur = time.time()

                if cur-prev >= 1:
                    prev = cur
                    TIMER = TIMER-1
            else:
                ret, frame = cap.read()
                resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
                image_np = np.array(resized_frame)
                normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
                data[0] = normalized_image
                prediction = model.predict(data)
                cv2.imshow("frame", frame)
                print(prediction)
                prediction = np.argmax(prediction)
                print(cpu_opt)
                if prediction == cpu_opt:
                    print("Its a draw game in this round")
                    cpu_wins += 1
                    user_wins +=1
                elif prediction > cpu_opt:
                    print("You won this round!!!")
                    user_wins += 1

                else:
                    print("You lost this round")
                    cpu_wins += 1


                TIMER = 5
            n_rounds += 1
        elif k == 27:
            break
    if cpu_wins > user_wins:
        print("Sorry, You lost the game")
    elif cpu_wins < user_wins:
        print("Congratulations!!! You won the game")
    else:
        print("Its a Draw")
    cap.release()

    cv2.destroyAllWindows()

RockPaperScissorsGame()
def get_prediction():
    import cv2
    from keras.models import load_model
    import numpy as np
    import random
    import time
    model = load_model('converted_keras/keras_model.h5')
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    OPTIONS_WORDS = ["Nothing", "Rock", "Paper", "Scissors"]
    OPTIONS_NUMBERS = list(range(4))
    OPTIONS_DICT = dict(zip(OPTIONS_WORDS, OPTIONS_NUMBERS))
    cpu_wins = 0
    user_wins = 0
    round = 0
    countdown_timer = 5
    result_message = ""
    while True: 
        ret, frame = cap.read()
        cv2.putText(frame, "Round: {}".format(round), (650, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
        cv2.putText(frame, "CPU = {}".format(cpu_wins), (200, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
        cv2.putText(frame, "Player = {}".format(user_wins), (1000, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
        cv2.putText(frame, "Press A to Reset The Game", (200, 600), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
        cv2.putText(frame, "Press Q to Play", (1000, 600), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
        cv2.putText(frame, result_message, (500, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))

        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        cv2.imshow('frame', frame)
        k = cv2.waitKey(125)
        
        
        # Press q to play
        if k == ord('q'):
            start_time = time.time()
            while countdown_timer >= 0:
                ret, frame = cap.read()
                cv2.putText(frame, "Countdown: {}".format(countdown_timer), (650, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
                cv2.putText(frame, "Round: {}".format(round), (650, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
                cv2.putText(frame, "CPU = {}".format(cpu_wins), (200, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
                cv2.putText(frame, "Player = {}".format(user_wins), (1000, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
                cv2.putText(frame, "Press A to Reset The Game", (200, 600), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
                cv2.putText(frame, "Press Q to Play", (1000, 600), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
                cv2.imshow("frame", frame)
                cv2.waitKey(125)

                current_time = time.time()
                if current_time-start_time >= 1:
                    start_time = current_time
                    countdown_timer -= 1


            else:
                ret, frame = cap.read()
                resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
                image_np = np.array(resized_frame)
                normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
                data[0] = normalized_image
                cpu_choice = random.choice(OPTIONS_NUMBERS)
                user_choice = np.argmax(model.predict(data))
                cv2.imshow('frame', frame)
                countdown_timer = 5
            round += 1
            
            if user_choice > cpu_choice:
                user_wins += 1
                result_message = "You won this round!!!"
                
            
            elif user_choice < cpu_choice:
                cpu_wins += 1
                result_message = "CPU wins this round!!!"
                
                
            else:
                cpu_wins += 0
                user_wins += 0
                result_message = "This round was a draw"

        elif cv2.waitKey(27) == ord('a'):
            cpu_wins = 0
            user_wins = 0
            round = 0

        elif (user_wins >= 3):
                result_message = "Congratulations, You Win The Game!!!"
                
        elif (cpu_wins >= 3):
                result_message = "Sorry, You Lost The Game!!!"
    


        

    # After the loop release the cap object
    cap.release()

    # Destroy all the windows
    cv2.destroyAllWindows()


get_prediction()
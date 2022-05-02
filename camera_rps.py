def get_prediction():
    import cv2
    from keras.models import load_model
    import numpy as np
    import random
    from manual_rps import get_winner
    import time
    model = load_model('converted_keras/keras_model.h5')
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    OPTIONS_WORDS = ["Nothing", "Rock", "Paper", "Scissors"]
    OPTIONS_NUMBERS = list(range(4))
    OPTIONS_DICT = dict(zip(OPTIONS_WORDS, OPTIONS_NUMBERS))
    start_time = time.time()
    cpu_wins = 0
    user_wins = 0
    round = 0
    while (cpu_wins < 3) & (user_wins < 3): 
        ret, frame = cap.read()
        cv2.putText(frame, "Round: {}".format(round), (650, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
        cv2.putText(frame, "Time: {}".format(int(time.time() - start_time)), (650, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
        cv2.putText(frame, "CPU = {}".format(cpu_wins), (200, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
        cv2.putText(frame, "Player = {}".format(user_wins), (1000, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
        cv2.putText(frame, "Press A to Quit", (200, 600), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
        cv2.putText(frame, "Press Q to Play", (1000, 600), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        cpu_choice = random.choice(OPTIONS_NUMBERS)
        user_choice = np.argmax(model.predict(data))
        #result = get_winner(user_choice, cpu_choice)
        cv2.imshow('frame', frame)
        
        
        # Press q to play
        if cv2.waitKey(1) & 0xFF == ord('q'):
            start_time = time.time()
            round += 1
            if user_choice > cpu_choice:
                user_wins += 1
                
            elif user_choice < cpu_choice:
                cpu_wins += 1
                
            else:
                cpu_wins += 0
                user_wins += 0
        elif cv2.waitKey(33) == ord('a'):
            break

    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()


get_prediction()
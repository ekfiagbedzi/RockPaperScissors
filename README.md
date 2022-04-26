# RockPaperScissorsGame

## Rock Paper Scissors Game built with Computer Vision

### Model Description
This model was built using Teachable Machine Learning.
It was trained using 4 different image classes; Rock (566 images), Paper (571 images) Scissiors (560 images) and nothing (544 images) collected with webcam.
The batch size of the training images were 16, epochs were 50 and learning rate = 0.001. 

### How model is used
The model will be used to predict the option the player opted to play using a camera frame.

### Environment setup and libraries installed
I first created a virtual environment using python's `venv`, and installed the following libraries using `pip` containing libraries;
Tensorflow: For Machine Learning
Keras: For Machine Learning
OpenCV-python: For computer vision
Numpy: For numerical computing and image manipulation


The code for the game has been wrapped up in a funciton called RockPaperScissors

### How to Play
To play this game, enter command `python run.py` in the terminal.
This will open your webcam. Press `Q` to start the game. Countdown starts.
Once countdown ends, the current frame at the end of the countdown will be used
to predict the option you chose.
Your choice will be compared to that of that of the CPU and the winner determined
by the classical rules of Rock Paper Scissors.

End



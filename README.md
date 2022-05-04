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


### Manual Game Code
Defined functions; `get_user_choice`, `get_computer_choice` and `get_winner`
![code-snapshot](https://user-images.githubusercontent.com/71975468/166817267-6d7092ec-7da1-47fb-989b-0d7264375ea2.png)

### Webcam Game Code


### How to Play
#### Manual Game
To play the manual version of this game, enter command `python manual_rps.py in the terminal.
This will present a prompt; Press `Q` to start the game. Please enter you choice; one of Rock, Paper or Scisssors:
Once you enter your choice, your choice will be compared to that of that of the CPU and the winner determined
by the classical rules of Rock Paper Scissors.


To play the webcam version of this game, enter command `python camera_rps.py in the terminal.
This will present a prompt. Press `Q` to play the each round. Countdown starts. Your choice will be compared to that of that of the CPU and the winner determined
by the classical rules of Rock Paper Scissors. Once the computer or the player gets to three wins, the game ends and the winner declared
To reset game at any point, press `A`.

End



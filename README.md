# RockPaperScissors

## Rock Paper Scissors Game built with Computer Vision

### Model Description
This model was built using Teachable Machine Learning.
It was trained using 4 different image classes; Rock (566 images), Paper (571 images) Scissiors (560 images) and nothing (544 images) collected with webcam.
The batch size of the training images were 16, epochs were 50 and learning rate = 0.001. 

### How model is used
The model will be used to predict the option the player opted to play using a camera frame.

### Environment setup and libraries installed
I first created a virtual environment using python's `venv`, and installed the following libraries using `pip` containing libraries;
`Tensorflow`: For Machine Learning
`Keras`: For Machine Learning
`OpenCV-python`: For computer vision
`Numpy`: For numerical computing and image manipulation


The code for the game has been wrapped up in a funciton called RockPaperScissors


### Manual Game Code
Defined functions; `get_user_choice`, `get_computer_choice` and `get_winner`
![code-snapshot](https://user-images.githubusercontent.com/71975468/166817267-6d7092ec-7da1-47fb-989b-0d7264375ea2.png)

### Webcam Game Code
Used `cv2.putText` to display various messages such as scores, how to play the game and winners on the webcam display
![code-snapshot](https://user-images.githubusercontent.com/71975468/166819149-d5fa72b6-e4d5-4cb1-90bb-985cd0bcf5ca.png)

Setup and displayed a countdown timer on the webcam
![code-snapshot](https://user-images.githubusercontent.com/71975468/166819378-f1a99098-fbc1-4eab-a8ff-61cd8c3ab830.png)

Made predictions using the frame immediately after countdown ends
![code-snapshot](https://user-images.githubusercontent.com/71975468/166819554-67a8d60c-60cb-4ba6-aa37-3452541aeec8.png)


### How to Play
#### Manual Game
To play the manual version of this game, enter command `python manual_rps.py in the terminal.
This will present a prompt; Press `Q` to start the game. Please enter you choice; one of Rock, Paper or Scisssors:
Once you enter your choice, your choice will be compared to that of that of the CPU and the winner determined
by the classical rules of Rock Paper Scissors.

#### Webcam Game
To play the webcam version of this game, enter command `python camera_rps.py` in the terminal.
This will present a prompt. Press `Q` to play the each round. Countdown starts. Your choice will be compared to that of that of the CPU and the winner determined
by the classical rules of Rock Paper Scissors. Once either the computer or the player gets to three wins, the game ends and the winner declared
To reset game at any point, press `A`.

End



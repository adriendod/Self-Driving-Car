

-- curently rebuilding the car from the ground up with new hardware, the readme is not up to date--

# Self-Driving-Car

This is a project to build a self driving car out of a toy RC Car.
This project uses :
  - a toy rc car from amazon (link)
  - a rasberry pi as the onboard computer
  - a XXXX motor controller to drive the 2 motors (one for driving, one for steering)
  - a pi camera
  
The goal of the project is to have the car drive itself in a circuit made out of blue tape. 
Eventually I plan to integrate object recognition (stop signs, red ligts...) and make the car act accordingly.

## Steps

Here are the steps needed in order to reach the goal:

  - Be able to drive the car from the computer using wifi.
  - Have the rasberry pi send power to the motors to control them ([PWM Config](https://github.com/adriendod/Self-Driving-Car/blob/master/PWM_Config.py))
  - Make the car take pictures and record the steering angle in a csv file to gather training data. ([Car Training](https://github.com/adriendod/Self-Driving-Car/blob/master/car_training.py))
  - Preprocess the data and train a Convolutional Neural Network to predict steering angle. ([CNN Training](https://github.com/adriendod/Self-Driving-Car/blob/master/Self_Driving_Car.ipynb))
  - Implement the trained model in the car. Have the model take pictures and predict a steering angle as fast as possible ([Autonomous Drive](https://github.com/adriendod/Self-Driving-Car/blob/master/autonomous_drive.py)) and model.h5
  
### Driving the car from wifi
It was pretty easy having the car respond to a keypress, but the car would still go forward when I released the key. The best solution I found to this proble is to use Pygame, a library used to develop video games with python. The car control runs in a loop checking many times per second what key is pressed or release and act accordingly. I implemented events in this loop to take pictures and save the final CSV after a key press.


### Take pictures and write the steering angle down
  
  
## Results

The car can take a picture, preprocess the image to feed it to the model, and predict a steering angle in about 300ms. Most of the time is taken by the frame capture and preprocessing. A better technique could be implemented to save time, it will be needed when adding the object recognition.


  

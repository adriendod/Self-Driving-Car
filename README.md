

-- curently rebuilding the car from the ground up with new hardware, the readme is not up to date--

# Self-Driving-Car

This is a project to build a self driving car out of a toy RC Car.
This project uses :
  - a toy rc car from amazon or a bulkier tank frame (anything with 2 DC motors will work)
  - a Jetson Nano as the onboard computer
  - aa Adafruit Featherwing motor controller to drive the 2 motors 
  - a pi camera v2
  
The goal of the project is to have the car drive itself in a circuit made out of blue rope. 
Eventually I plan to integrate object recognition (stop signs, red ligts...) and make the car act accordingly.

## Code

Here are the steps needed in order to reach the goal:

  - Be able to drive the car from the computer using wifi.
  - Have the Jetson Nano send power to the motors to control them ([Motor Class](https://github.com/adriendod/Self-Driving-Car/blob/master/motor.py))
  - Gain access to the camera: ([Camera class](https://github.com/adriendod/Self-Driving-Car/blob/master/camera.py))
  - Make the car take pictures and record the steering angle in a csv file to gather training data. ([Car Training](https://github.com/adriendod/Self-Driving-Car/blob/master/drive.py))
  - Preprocess the data and train a Convolutional Neural Network to predict steering angle. ([CNN Training](https://github.com/adriendod/Self-Driving-Car/blob/master/Self_Driving_car_V2.ipynb))
  - Implement the trained model in the car. Have the model take pictures and predict a steering angle as fast as possible ([Autonomous Drive](https://github.com/adriendod/Self-Driving-Car/blob/master/autonomous_drive.py)) and model.h5

  
  
## Results

The car can take a picture, preprocess the image to feed it to the model, and predict a steering angle in about 0.02s.

[![Alt text](https://img.youtube.com/vi/ijRzcBkdRs4/0.jpg)](https://www.youtube.com/watch?v=ijRzcBkdRs4)



  

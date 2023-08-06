# Raspberry-pi-The-Rod-Tracker-Project
This project was completed as a preparatory course in the Masters of Media Technology at Technical University of Ilmenau,Germany

## Project Overview:

The project involves developing a web interface using Flask to display the results of three tasks on a Raspberry Pi. 

The tasks include motor control, OpenCV control, and sensor control. Python is used to complete the project, while working with libraries like OpenCV, NumPy, and RPi.GPIO, flask, gunicorn, picamera, and others.Three tasks were achieved during the project:

### Motor Control (Task 1):

•	The motor control task aims to control a stepper motor with specific behaviors to earn points.

•	The motor controller.py script contains a MotorController class with methods to start and stop the motor, and set its rotation direction and degrees.

•	The main.py script runs and tests the motor controller, allowing it to rotate randomly.

### OpenCV Control (Task 2):

•	Task 2 involves processing video captured by the Raspberry Pi Camera to detect a red mark and four colors.

•	The opencv controller.py script contains an OpenCVController class to process frames and determine the current color based on the position of the red mark.

•	The main.py script runs and tests the OpenCV controller using a fake camera and provided test frames.

### Distance Sensor Control (Task 3):

•	Task 3 focuses on controlling an ultrasonic distance sensor to measure the distance between the sensor and a board attached to the rod.

•	The sensor controller.py script contains a SensorController class with methods to get the distance and digit from the distance.

•	The main.py script runs and tests the sensor controller, printing distance and digit information.

### Web Interface (All Tasks):

•	The Flask app script (app.py) contains views to control the motor, retrieve motor status, process OpenCV, get distance, and determine the digit based on distance.

•	The main client script (main.js) handles client-side interactions, such as requesting motor and sensor control, updating motor status, and displaying the current color and digit.

•	The index template (index.html) structures the web interface with sections for video streaming, motor control buttons, and monitoring information.

### Testing:

•	Testing the web app locally on the Raspberry Pi via SSH involves pulling the code from the Git repository, making changes, and running the app.py script.

•	Debugging logs will appear on the Raspberry Pi terminal.

### Libraries and Environment:

•	Python is used in Visual Studio.

•	The Flask web framework is employed for developing the web interface.

•	OpenCV is used for image processing tasks.

•	The ultrasonic distance sensor is controlled with GPIO.

•	A fake camera and fake GPIO script are provided for local testing and simulation.

#### Overall, the project demonstrates the integration of hardware (Raspberry Pi, stepper motor, distance sensor, camera) with software (Python, Flask, OpenCV) to create a functional web interface for various tasks and automation.

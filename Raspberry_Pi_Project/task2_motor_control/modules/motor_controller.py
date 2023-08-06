USE_FAKE_GPIO = True  # Change to FALSE if testing in the Raspberry Pi

if USE_FAKE_GPIO:
    from .fake_gpio import GPIO  # For running app
else:
   import RPi.GPIO as GPIO  # For testing in Raspberry Pi


# import ...
import random
import time

class MotorController(object):

    def __init__(self):
        self.working = False

    def start_motor(self):
        self.PIN_STEP = 25  # do not change
        self.PIN_DIR = 8  # do not change
        self.working = True
        # ...
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.PIN_STEP, GPIO.LOW)
        GPIO.setup(self.PIN_DIR, GPIO.OUT)

        direction = random.choice(["clockwise", "counterclockwise"])
        rotation = random.choice([180, 360])
        steps = int(rotation / 0.225)

        if direction == "clockwise":
            GPIO.output(self.PIN_DIR, GPIO.IN)
        else:
            GPIO.output(self.PIN_DIR, GPIO.OUT)


        for i in range(steps):
            GPIO.output(self.PIN_STEP, GPIO.HIGH)
            time.sleep(0.003)
            GPIO.output(self.PIN_STEP, GPIO.LOW)
            time.sleep(0.003)

        print(f"Rotating {rotation} degrees in {direction} direction")

        print('Motor Started')

        self.stop_motor()

    def stop_motor(self):
        GPIO.output(self.PIN_STEP, GPIO.LOW)
        GPIO.output(self.PIN_DIR, GPIO.LOW)
        self.working = False
        print("Motor Stopped")



 # clock_wise=0
       # counter_clock_wise=1
       # rotation=0.225 #motor rotates 0.225 per step
       # total_angle=360 #rotating 360 degree
       # steps=total_angle/rotation #

       # step_1 = int(steps/2)
       # time.sleep(0.003)
       # steps_2 = steps
       # time.sleep(0.003)

       # random_step=[step_1,steps_2]
       # random_movement = random.choice(random_step)



    def is_working(self):
        return self.working


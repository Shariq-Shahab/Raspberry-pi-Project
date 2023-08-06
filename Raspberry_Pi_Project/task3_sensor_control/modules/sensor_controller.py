USE_FAKE_GPIO = True # Chage to FALSE if testing in the Raspberry Pi

if USE_FAKE_GPIO:
    from .fake_gpio import GPIO  # For running app
else:
    import RPi.GPIO as GPIO  # For testing in Raspberry Pi


# import ...
import statistics
import time

class SensorController:

    def __init__(self):
        self.PIN_TRIGGER = 18  # do not change
        self.PIN_ECHO = 24  # do not change
        self.distance = None
        self.color_from_distance = [False, False, False, False]
        print('Sensor controller initiated')

    def track_rod(self):
        # ...
        distances = []
        for i in range(10):
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(self.PIN_TRIGGER, GPIO.OUT)
            GPIO.setup(self.PIN_ECHO, GPIO.IN)

            GPIO.output(self.PIN_TRIGGER, GPIO.LOW)
            time.sleep(0.1)

            GPIO.output(self.PIN_TRIGGER, GPIO.HIGH)
            time.sleep(0.00001)
            GPIO.output(self.PIN_TRIGGER, GPIO.LOW)

            pulse_start_time = time.time()
            pulse_end_time = time.time()
            while GPIO.input(self.PIN_ECHO) == GPIO.LOW:
                pulse_start_time = time.time()
            while GPIO.input(self.PIN_ECHO) == GPIO.HIGH:
                pulse_end_time = time.time()
            pulse_duration = pulse_end_time - pulse_start_time

            measure_distance = round(((pulse_duration * 34300) / 2), 2)
            distances.append(measure_distance)
        self.distance = statistics.median(distances)

        if 4 <= self.distance <= 8:
            self.color_from_distance = [False, False, False, True]
        elif 8.9 <= self.distance <= 13:
            self.color_from_distance = [False, False, True, False]
        elif 13.5 <= self.distance <= 17.8:
            self.color_from_distance = [False, True, False, False]
        elif 18 <= self.distance <= 22:
            self.color_from_distance = [True, False, False, False]
        else:
            self.color_from_distance = [False, False, False, False]

        print('Monitoring')

    def get_distance(self):
        return self.distance

    def get_color_from_distance(self):
        return self.color_from_distance

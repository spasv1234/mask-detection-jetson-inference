import Jetson.GPIO as GPIO
import time

def main():
    print("Starting demo now! Press CTRL+C to exit")
    curr_value = GPIO.HIGH
    try:
        while True:
            time.sleep(1)
            # Toggle the output every second
            print("Outputting {} to pin {}".format(curr_value, output_pin))
            GPIO.output(output_pin, curr_value)
            curr_value ^= GPIO.HIGH
    finally:
        GPIO.cleanup()

def turn_off_led():
    value = GPIO.LOW
    GPIO.output(output_pin, value)

def turn_on_led():
    value = GPIO.HIGH
    GPIO.output(output_pin, value)


# Pin Definitions
output_pin = 18  # BOARD pin 12, BCM pin 18

#Pin Setup
GPIO.setmode(GPIO.BCM) # Board pin-numbering scheme
GPIO.setup(output_pin, GPIO.OUT, initial=GPIO.HIGH)
    


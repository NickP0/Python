from RPLCD.gpio import CharLCD
from RPi import GPIO
import time

#GPIO.cleanup()

GPIO.setmode(GPIO.BOARD)

rs=11
rw=15
e=16

bus_pin_numbs=[37,36,22,18,13,33,32,29]
used_pins=[11,13,15,16,18,22,29,32,33,36,37]
hall_sensor=12

for i in range(len(used_pins)):
    GPIO.setup(used_pins[i], GPIO.OUT)

GPIO.setup(hall_sensor, GPIO.IN)
event = GPIO.add_event_detect(hall_sensor, GPIO.FALLING)

count=0

#this function isn't being used but may be useful in the future
def falling_callback():
    global count
    if GPIO.input(hall_sensor):
         count+=1
    if count > 999:
         count = 0

lcd=CharLCD(cols=16, rows=2, pin_rs=rs, pin_rw=rw, pin_e=e, pins_data=bus_pin_numbs, numbering_mode=GPIO.BOARD, charmap="A00")

lcd.cursor_pos = (0,0)

if __name__ == "__main__":
    while True:
        try:
            event
            if GPIO.event_detected(hall_sensor):
                lcd.clear()
                print("something")
                count += 1
                lcd.write_string(f"Count: {count}")

        except KeyboardInterrupt:
            print("Closing...")
            GPIO.cleanup()


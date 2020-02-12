from gpiozero import PWMLED
import time #import sleep

servoPin = 14
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(servoPIN, GPIO.OUT)

voltage = 0
led = PWMLED(servoPin)


#p = GPIO.PWM(14, 50) # GPIO 14 for PWM with 50HZ
#p.start(voltage) # Initialization
try:
    while True:
        #p.ChangeDutyCycle(voltage)
        led.on()
        led.value = voltage
        voltage += 0.01
        print(led.value)
        time.sleep(1)
        
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
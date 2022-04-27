import multiprocessing
from time import sleep
from gpiozero import Motor, LineSensor
import timeit
from gpiozero import LED
motor1 = Motor(forward=19, backward=26)
motor2 = Motor(forward=13, backward=21)
led = LED(20)
human=0
#speed=0.6
start=0

def move(speed):
    motor1.forward(speed.value)
    motor2.forward(speed.value)

def led_lights(human):
    while True:
        if human.value==0:
            led.off()
        else:
            led.on()
        

def human_detected(speed,human):
    speed.value=1
    while True:
        if human.value==0:
            stop=int(timeit.default_timer())
            time_now=stop-start    #time acts as as traffic lights
            print("human")
            print(human.value)      
            if time_now==0:
                speed.value=0.9
                print("speed=0.9")
            elif time_now==1:
                speed.value=0.8 
                print("speed=0.8")
            elif time_now==2:
                speed.value=0.7 
                print("speed=0.7")
            elif time_now==3:
                speed.value=0.6
                print("speed=0.6")
            elif time_now==4:
                speed.value=0.3  
                print("speed=0.3")
            elif time_now==5:
                speed.value=0.2 
                human.value=1
                print("speed=0.2")
            else:
                speed.value=0.2 
        if human.value==1:
                speed.value=0
                print("human is here")
if __name__ == "__main__":
    start = int(timeit.default_timer())
    human = multiprocessing.Value('i', 0)
    speed = multiprocessing.Value('d', 0)
    
    p1 = multiprocessing.Process(target=human_detected, args=(speed,human))
    p2 = multiprocessing.Process(target=led_lights, args=(human,))
    p1.start()
    p2.start()
    while True:
        #speed=hu0man_detected(speed)
        move(speed)
    

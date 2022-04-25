import multiprocessing
from time import sleep
from gpiozero import Motor, LineSensor
import timeit
motor1 = Motor(forward=19, backward=26)
motor2 = Motor(forward=13, backward=21)
human=0
#speed=0.6
start=0

def move(speed):
    motor1.forward(speed.value)
    motor2.forward(speed.value)
  
def traffic
  
def human_detected(speed):
    speed.value=1
    while True:
        stop=int(timeit.default_timer())
        time_now=stop-start
        print(time_now)
        if time_now==0:
            speed.value=0.9
        if time_now==1:
            speed.value=0.7
        elif time_now==2:
            speed.value=0.5         
        elif time_now==3:
            speed.value=0.3
        elif time_now==4:
            speed.value=0.2 
        else:
            speed.value=0
    
if __name__ == "__main__":
    start = int(timeit.default_timer())
    speed = multiprocessing.Value('d', 0)
    p1 = multiprocessing.Process(target=human_detected, args=(speed,))
    p1.start()
    while True:
        #speed=hu0man_detected(speed)
        move(speed)
    

from djitellopy import tello
import KeyPressModule as kpm
import imageCapture
from time import sleep

kpm.init()
drone = tello.Tello()
drone.connect()
print(drone.get_battery())

def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50

    if kpm.getKey("LEFT"): lr = -speed
    elif kpm.getKey("RIGHT"): lr = speed

    if kpm.getKey("w") : fb = speed
    elif kpm.getKey("s") : fb = -speed

    if kpm.getKey("UP") : ud = speed
    elif kpm.getKey("DOWN") : ud = -speed

    if kpm.getKey("a") : yv = speed
    elif kpm.getKey("d") : yv = -speed

    if kpm.getKey("q") : drone.land()
    if kpm.getKey("e") : drone.takeoff()

    return[lr, fb, ud, yv]


while True:

    vals = getKeyboardInput()
    drone.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    imageCapture.start()
    # makes it stable, nothing happens too fast
    sleep(0.05)
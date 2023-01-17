from djitellopy import tello
from time import sleep

# Creating a tello object
drone = tello.Tello()
drone.connect()

print(drone.get_battery())

# Drone taking off
drone.takeoff()

drone.send_rc_control(0, 50 ,0 ,0)
sleep(2)

# Drone will not move when landing
drone.send_rc_control(0, 0 ,0 ,0)

# Drone landing
drone.land


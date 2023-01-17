import time
import cv2
import numpy as np
from djitellopy import tello

# Dear viewer, commented code are descriptions of the code below or
# is commented out inorder for opencv to be used with the drone (not with the webcame) 

drone = tello.Tello()
drone.connect()
print(drone.get_battery())

drone.streamon()
drone.takeoff()

drone.send_rc_control(0, 0, 25, 0)
time.sleep(2.2)

w, h = 360, 240
fbRange = [6200, 6800]
# proportional, integral, derivative
pid = [0.4, 0.4, 0]
pError = 0

def findFace(img):
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.2, 8)

    # information for center point of face
    myFaceListC = []
    # area of that surface
    myFaceListArea = []

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255,), 2)
        # get our center x and y
        cx = x + w // 2
        cy = y + h // 2

        area = w * h
        cv2.circle(img, (cx, cy), 5, (0, 225, 0), cv2.FILLED)
        myFaceListC.append([cx, cy])
        myFaceListArea.append(area)

    if len(myFaceListArea) != 0:
        i = myFaceListArea.index(max(myFaceListArea))
        return img, [myFaceListC[i], myFaceListArea[i]]

    else:
        return img, [[0, 0], 0]


def trackFace(info, w, pid, pError):
    # we need to create a range when the move will move
    area = info[1]
    x, y = info[0]
    fb = 0

    error = x - w//2
    speed = pid[0]*error + pid[1] * (error-pError)
    # new speed
    speed = int(np.clip(speed, -100, 100))


    # Drone won't move (green zone)
    if area > fbRange[0] and area < fbRange[1]:
        fb = 0
    # Too close (move backwards)
    elif area > fbRange[1]:
        fb = -20
    # Too far (move forwards)
    elif area < fbRange[0] and area != 0:
        fb = 20

    if x == 0:
        speed = 0
        error = 0

    print(speed, fb)

    # me.send_rc_control(0, fb, 0, speed)
    return error

# Standard code for running code with open cv
cap = cv2.VideoCapture(0)
while True:
    _, img = cap.read()
    # img = drone.get_frame_read().frame
    img, info = findFace(img)
    pError = trackFace(info, w, pid, pError)
    # Center values will be used to rotate
    # Area values will be used to go front and backwards
    # print("Center: ", info[0], "Area:", info[1])
    cv2.imshow("Output", img)
    # when we press q. it will land
    if cv2.waitkey(1) & 0xFF == ord('q'):
        drone.land()
        break


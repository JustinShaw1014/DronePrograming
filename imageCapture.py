from djitellopy import tello

import cv2

drone = tello.Tello()
drone.connect()
print(drone.get_battery())

drone.streamon()

# Creating a loop to capture multiple images
while True:
    img = drone.get_frame_read().frame
    # We are resizeing the frame to process faster
    img = cv2.resize(img, (360,240))
    # Creating a window to display this result
    cv2.imshow("Image", img)
    # We must give it a delay of 1 millisecond as the frame will close before we could see it
    cv2.waitKey(1)
import pygame

def init():
    pygame.init()
    win = pygame.display.set_mode((400, 400))

# A function to get the keyboard input
def getKey(keyName):
    ans = False

    # if the key is pressed
    for event in pygame.event.get(): pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame, 'K_{}'.format(keyName))
    if keyInput[myKey]:
        ans = True
    pygame.display.update()
    return ans

# If any other file than KeyPressedModule is run, the code below will not run
# Testing for pygame inputs
def main():
    if getKey("LEFT"):
        print("Left key pressed")
    if getKey("RIGHT"):
        print("Right key pressed")
    

# if I am running this file as the main file, run this block of code
# else None
if __name__ == '__main__':
    init()
    while True:
        main()
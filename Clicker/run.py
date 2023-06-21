
# Import the pygame module
import pygame
# Import random for random numbers
import random
# Import time to get the current current time
import time


            
# Import pygame.locals for easier access to key coordinates
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)


# Initialize pygame
pygame.init()
pygame.font.init()



#
# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Variable to keep the main loop running
running = True

# Fill the screen with grey
screen.fill((50, 50, 50))

count = 0

# Main loop
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            #pos = pygame.mouse.get_pos()
            if count == 0:
                start_time = time.time()
            count += 1
            print(count)

        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False

    if count > 10:
        elapsed_time = time.time() - start_time
        print("It took " + str(elapsed_time) + "seconds")
        running = False   

    
    if count % 2 == 0:
        # Fill the screen with white
        screen.fill((255, 255, 255))
    else:
        screen.fill((255, 0, 0))

    
    # Update the display
    pygame.display.flip()

 


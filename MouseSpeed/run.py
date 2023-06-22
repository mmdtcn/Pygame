'''
Game to present the user with boxes to click on.
Paul Talaga - June 2021
'''

# Import the pygame module
import pygame
# Import random for random numbers
import random
# Import time to get the current time
import time

# Initialize pygame
pygame.init()

# Having to click the same box position twice doesn't make sense, so
# this function returns true if every element does not have the same value next to it.
# Useful when trying to randomize a list of positions.
def allowable(list):
    last = list[0]
    for i in range(1,len(list)):
        if last == list[i]:
            return False
        last = list[i]
    return True

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

# Game step counter
count = -1
# There are 4 box positions and we present the user with each position twice
positions = [1,2,3,4] * 2
# Shuffle the positions, but make sure no box position is duplicated.
random.shuffle(positions)
while not allowable(positions):
    random.shuffle(positions)
#print(positions)

# Keep track of missed clicks.
bad_click = 0

# To hold the position of the box rectangle for click detection
rect = None

# Main loop
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == pygame.KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            # The first click starts the timer and shows the first box
            if count == -1:
                start_time = time.time()
                count = 0
            # Was the click in the last box displayed?
            elif rect.collidepoint(pos) :
                print("hit")
                count += 1  # TODO - this works but the last box won't show.
            else:
                # Clicked the mouse but didn't hit the box!
                bad_click += 1
            # Box size
            box = pygame.Surface( (100, 100))
            # Box color
            box.fill((255, 0, 255))
            # Brute-force way of position the box on the screen
            if positions[count] == 1:
                rect = box.get_rect(
                    center = (SCREEN_WIDTH/3, SCREEN_HEIGHT/3)
                )
            elif positions[count] == 2:
                rect = box.get_rect(
                    center = (2 * SCREEN_WIDTH/3,  SCREEN_HEIGHT/3)
                )
            elif positions[count] == 3:
                rect = box.get_rect(
                    center = (SCREEN_WIDTH/3, 2 * SCREEN_HEIGHT/3)
                )
            else:
                rect = box.get_rect(
                    center = (2 * SCREEN_WIDTH/3, 2 * SCREEN_HEIGHT/3)
                )
            # Refill the screen with grey so the old position disappears
            screen.fill((50, 50, 50))
            # Put the box on the screen at a location.
            screen.blit(box, rect)
            print(count)


        # Did the user click the window close button? If so, stop the loop.
        elif event.type == pygame.QUIT:
            running = False

    # Is the game over?
    if count >= len(positions) -1:
        elapsed_time = time.time() - start_time
        print("It took " + str(elapsed_time) + "seconds")
        print(f"and {bad_click} bad clicks.")
        running = False   

    
    # Update the display
    pygame.display.flip()

 


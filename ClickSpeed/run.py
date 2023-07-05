'''
Game to see the reaction time of the user.
Click on the screen when RED is displayed
Paul Talaga - June 2021
'''

# Import the pygame module
import pygame
# Import random for random numbers
import random
# Import time to get the current time
import time


from update_score import updateScore


def shuffle_colors(c):
    random.shuffle(c)
    while c[0] == (255,0,0):
        random.shuffle(c)

# Get the user's name
name = input("What is your name?")

# Initialize pygame
pygame.init()

colors = [ (255,255,0), (0, 255, 100), (200, 200, 200), (100, 255,100), (255,0,0)]

shuffle_colors(colors)

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

times = []
num_incorrect = 0

# Create a custom event for switching the colors
CHANGECOLOR = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGECOLOR, 1500)

# Variable to keep the main loop running
running = True

# Current color index
i = 0

# Main loop
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == pygame.KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and colors[i] == (255,0,0):
            # Did they click when it was red?
            elapsed_time = time.time() - start_time
            #print(f"Reaction time {elapsed_time:0.3}")
            # Send score to scoreboard
            updateScore(name, elapsed_time)
            # So they can't memorize when red is
            shuffle_colors(colors)
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("It wasn't red!!!!!")
            num_incorrect += 1
            print(f"That's {num_incorrect} wrong clicks!")
        elif event.type == CHANGECOLOR:
            i = i + 1
            if i >= len(colors):
                i = 0
            # Fill the screen with that color
            screen.fill( colors[i] )

            # If red went up, save the time
            start_time = time.time()

            # Update the display
            pygame.display.flip()
        # Did the user click the window close button? If so, stop the loop.
        elif event.type == pygame.QUIT:
            running = False
 

        

 


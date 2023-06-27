
# Import the pygame module
import pygame
# Import random for random numbers
import random

# Convert mp3 to ogg - https://stackoverflow.com/questions/62543965/pygame-audio-error-unrecognized-audio-format
# pip install pydub
# AudioSegment.from_mp3("mymp3.mp3").export('myogg.ogg', format='ogg')

# Define a Player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Flake(pygame.sprite.Sprite):
    def __init__(self):
        super(Flake, self).__init__()
        #self.surf = pygame.Surface((75, 25))  # For development before images added
        self.surf = pygame.image.load("flake-small.png").convert_alpha()
        #self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(
            center=(SCREEN_WIDTH/2 , 
                    SCREEN_HEIGHT/2 )
        )
        self.xspeed = random.random() * 5 - 2 #random.randint(-5,5)
        self.yspeed = random.random() * 5 - 2 #random.randint(-5,5)
        if self.xspeed == 0 or self.yspeed == 0:
            self.kill()
        self.accel = 1.01
        self.rotate = random.randint(0,20)
        self.surf = pygame.transform.rotate(self.surf, self.rotate)
        for i in range(random.randint(0,10)):
            self.update()

    def update(self):
        self.rect.move_ip(int(self.xspeed), int(self.yspeed))
        
        self.xspeed *= self.accel
        self.yspeed *= self.accel
        if self.rect.left < 0 or self.rect.left > SCREEN_WIDTH or self.rect.bottom < 0 or self.rect.bottom > SCREEN_HEIGHT:
            self.kill()

        



# Initialize pygame
pygame.init()
pygame.font.init()


# Setup the clock for a decent framerate
clock = pygame.time.Clock()


#
# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# Create a custom event for adding a new snowflake
TIMER_UPDATE = pygame.USEREVENT + 1
pygame.time.set_timer(TIMER_UPDATE, 500)
time = 0


# Create groups to hold flakes
flakes = pygame.sprite.Group()


# Variable to keep the main loop running
running = True

# Fill the screen with grey
screen.fill((50, 50, 50))



# Main loop
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == pygame.KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == pygame.K_ESCAPE:
                running = False

        # Did the user click the window close button? If so, stop the loop.
        elif event.type == pygame.QUIT:
            running = False
        # Add a new flake?
        elif event.type == TIMER_UPDATE:
            flake = Flake()
            flakes.add(flake)

    # Move objects
    flakes.update()

    # Fill the screen with white
    screen.fill((255, 255, 255))

    # Draw all sprites
    for entity in flakes:
        screen.blit(entity.surf, entity.rect)

    # Update the display
    pygame.display.flip()

    # Ensure program maintains a rate of 30 frames per second
    clock.tick(30)


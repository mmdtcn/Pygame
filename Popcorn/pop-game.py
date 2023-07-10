
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
            center=(random.randint(0,SCREEN_WIDTH) , 
                    SCREEN_HEIGHT/4 )
        )
        self.xspeed = random.random() * 10 - 5.0 #random.randint(-5,5)
        self.yspeed = random.random() * 10 - 5.0 #random.randint(-5,5)
        self.gravity = 0
        self.unpopped = True


    def update(self):
        self.rect.move_ip(int(self.xspeed), int(self.yspeed + self.gravity))
        self.gravity += 0.1
        if self.rect.left < 0 or self.rect.left > SCREEN_WIDTH or self.rect.bottom < 0 or self.rect.bottom > SCREEN_HEIGHT:
            self.kill()
        # Remove snowflakes that don't move
        if self.xspeed == 0 and self.yspeed == 0 and random.randint(0,100) < 5:
            self.kill()


# Initialize pygame
pygame.init()
pygame.font.init()

splash = pygame.mixer.Sound('splash.ogg')

# Master score
score = 0

font = pygame.font.Font('freesansbold.ttf', 32)

# Game over text
over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score():
    score_font = font.render(f"Score: {score} Time remaining {time_left:0.1f}", True, (255,255,255))
    screen.blit(score_font, (10, 10))

def final_score():
    score_font = font.render(f"Final Score: {score}  r to Reset", True, (255,255,255))
    screen.blit(score_font, (200, 400))

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
pygame.time.set_timer(TIMER_UPDATE, 100)
time_left = 15


# Create groups to hold flakes
flakes = pygame.sprite.Group()


# Variable to keep the main loop running
running = True


# Main loop
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == pygame.KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == pygame.K_ESCAPE:
                running = False
            # r for reset was typed
            elif event.key == pygame.K_r:  
                score = 0
                time_left = 15
        # Did the user click the window close button? If so, stop the loop.
        elif event.type == pygame.QUIT:
            running = False
        # Add a new flake?
        elif time_left > 0 and event.type == TIMER_UPDATE:
            flakes.add( Flake() )
            time_left -= 0.1
        elif time_left > 0 and event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            # See what flakes (if any) were clicked on
            for f in flakes:
                if f.unpopped and f.rect.collidepoint(pos):
                    f.unpopped = False
                    score += 1
                    splash.play()
                    f.surf = pygame.image.load("raindrop.png").convert_alpha()

            
    # Move objects
    if time_left > 0:
        flakes.update()

    # Fill the screen
    screen.fill((255, 200, 200))

    # Draw all sprites
    for entity in flakes:
        screen.blit(entity.surf, entity.rect)

    if time_left > 0:
        show_score()
    else:
        final_score()


    # Update the display
    pygame.display.flip()

    # Ensure program maintains a rate of 30 frames per second
    clock.tick(30)


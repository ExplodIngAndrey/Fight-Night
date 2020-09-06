import pygame
from pygame import mixer

# Initialize Pygame
pygame.init()

# Create the Screen
screen = pygame.display.set_mode((800, 600))

# ID Sounds
coinSound = mixer.Sound('Coin.wav')
fallingSound = mixer.Sound('Falling.wav')
jumpSound = mixer.Sound('Jump.wav')
menuSelectSound = mixer.Sound('MenuSelect.wav')
pauseSound = mixer.Sound('Pause.wav')
unpauseSound = mixer.Sound('Unpause.wav')

# Title and Icon
pygame.display.set_caption('Street Fighter')
icon = pygame.image.load('Logo.png')
pygame.display.set_icon(icon)

# Game Loop
running = True
while running:
    screen.blit(background, (0, 0))
    # Check for Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()  # Updates Screen

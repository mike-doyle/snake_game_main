import pygame, sys

pygame.init()
screen = pygame.display.set_mode((600,800))

while True: 
    
    # Draw the elements of the game
    # Running this code alone will create an instance
    # that is possible to be closed by clicking "X"

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

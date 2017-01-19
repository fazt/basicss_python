import pygame
pygame.init()

window = pygame.display.set_mode((500, 400))
while True:
    pygame.draw.rect(window, (255,0,0),(0, 0, 50, 30))
    pygame.display.update()

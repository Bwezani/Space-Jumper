import pygame
from sys import exit
print('YOU ARE A LONG WAY FROM HOME, TIME TO FIND YOUR WAY BACK...')

pygame.init()
screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption('Space Jumper!')

while  True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    #some stuff
    pygame.display.update()
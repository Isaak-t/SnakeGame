import pygame
import random
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
green = (0,255,0)
blue = (0,0,255)

board_width = 500
board_height = 500

pygame.init()
board = pygame.display.set_mode((board_width,board_height))
pygame.draw.rect(board,green,pygame.Rect(10,10,10,10))
pygame.display.set_caption("snake snake snake")

apples = 10
snake_speed = 20

run = True
while run == True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            pygame.display.flip()
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

            if event.key == pygame.K_x:
              ran_x = random.randomint(0, 500)
              ran_y = random.randomint(0, 500)
              pygame.draw.rect(board, white, pygame.Rect(ran_x, ran_y, apples, apples))

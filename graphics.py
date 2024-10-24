import pygame
import random

screen = None
screen_color = "black"
grid_color = (33,33,33)
snake_color = "green"
portal_color = "blue"
food_color = "red"
obstacle_color = (200,200,200)


def display(x, y):
    global screen
    screen = pygame.display.set_mode((x, y))
    screen.fill(screen_color)


def drawGrid(width, height, block_size: int):
    for x in range(0, width):
        for y in range(0, height):
            rect = pygame.Rect(x*block_size, y*block_size, block_size, block_size)
            pygame.draw.rect(screen, grid_color, rect, 1)


def drawSnake(snake: list, block_size: int):
    for i in range(len(snake)):
        rect = pygame.Rect(snake[i][0]*block_size, snake[i][1]*block_size, block_size, block_size)
        pygame.draw.rect(screen, snake_color, rect)


def drawFood(pos: tuple, block_size):
    rect = pygame.Rect(pos[0]*block_size, pos[1]*block_size, block_size, block_size)
    pygame.draw.rect(screen, food_color, rect, 0, 20)


def drawPortal(pos: tuple, block_size):
    rect = pygame.Rect(pos[0]*block_size, pos[1]*block_size, block_size, block_size)
    pygame.draw.rect(screen, portal_color, rect, 10, 20)


def drawObstacles(obstacle: list, block_size):
    for i in range(len(obstacle)):
        rect = pygame.Rect(obstacle[i][0]*block_size, obstacle[i][1]*block_size, block_size, block_size)
        pygame.draw.rect(screen, obstacle_color, rect)



def clear_screen():
    screen.fill("black")
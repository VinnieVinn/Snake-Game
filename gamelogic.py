import pygame
import random

def isCollidingWithSelf(snake):
    head = snake[0]
    for i in range(1, len(snake)-1):
        if head == snake[i]:
            return True
    else:
        return False


def isCollidingWithWall(snake, grid_width, grid_height):
    head = snake[0]
    if head[0] > grid_width-1: return True
    if head[1] > grid_height-1: return True
    if head[0] < 0: return True
    if head[1] < 0: return True
    return False

def randomizeFoodPos(snake, grid_width, grid_height):
    global food_pos
    while True:
        pos = pygame.Vector2(random.randint(0, grid_width-1), random.randint(0, grid_height-1))
        
        for i in snake:
            if pos == i:
                break
        else: 
            return pos

def hasEaten(snake, food_pos):
    return snake[0] == food_pos

def addListHead(list: list, item):
    list.insert(0, item)

def removeTail(snake):
    return snake.pop(len(snake)-1)
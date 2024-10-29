import pygame
import random

def isCollidingWithSelf(snake):
    head = snake[0]
    for i in range(1, len(snake)): # Kanske ska vara -1 här?? Vet inte, fattar mig inte på range()...
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


def isCollidingWithObstacle(snake, obstacles):
    head = snake[0]
    for i in range(len(obstacles)):
        if head == obstacles[i]:
            return True
    else:
        return False


def randomizeFoodPos(grid_width, grid_height, ignore_list = []):
    global food_pos
    while True:
        #pos = pygame.Vector2(random.randint(0, grid_width-1), random.randint(0, grid_height-1))
        pos = (random.randint(0, grid_width-1), random.randint(0, grid_height-1))
        
        for i in ignore_list:
            if pos == i:
                break
        else:
            return pos


def randomizeObstaclePos(obstacleTypes, grid_width, grid_height, ignore_list = []):
    type = random.randint(0, len(obstacleTypes)-1)
    obstacle = []
    posOffset = randomizeFoodPos(grid_width, grid_height, ignore_list)
    
    for i in range(len(obstacleTypes[type])): 
        pos = (obstacleTypes[type][i][0] + posOffset[0], obstacleTypes[type][i][1] + posOffset[1])
        obstacle.append(pos)

    return obstacle

def addListHead(list: list, item):
    list.insert(0, item)


def removeTail(snake):
    return snake.pop(len(snake)-1)
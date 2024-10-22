import pygame

screen = None
screen_color = "black"


grid_color = (33,33,33)
block_size = 70

def display(x, y, color):
    global screen
    global screen_color
    screen = pygame.display.set_mode((x, y))
    screen.fill(color)

def drawGrid(width, height, block_size: int, color):
    for x in range(0, width):
        for y in range(0, height):
            rect = pygame.Rect(x*block_size, y*block_size, block_size, block_size)
            pygame.draw.rect(screen, color, rect, 1)


def drawSnake(snake: list, block_size: int, color):
    for i in range(len(snake)):
        rect = pygame.Rect(snake[i][0]*block_size, snake[i][1]*block_size, block_size, block_size)
        pygame.draw.rect(screen, color, rect)


def drawFood(pos: tuple, block_size, color):
    rect = pygame.Rect(pos[0]*block_size, pos[1]*block_size, block_size, block_size)
    pygame.draw.rect(screen, color, rect)

def clear_screen():
    screen.fill("black")
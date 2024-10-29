import pygame
import random
import text


def display(x, y):
    global screen
    screen = pygame.display.set_mode((x, y))
    screen.fill(screen_color)


def drawGrid(width, height, block_size: int):
    for x in range(0, width):
        for y in range(0, height):
            rect = pygame.Rect(x*block_size, y*block_size, block_size, block_size)
            pygame.draw.rect(screen, randomize_color(grid_first_color, grid_last_color), rect, 1)


def drawSnake(snake: list, block_size: int, player):
    snake_color_iteration = tuple(map(lambda a, b : (a - b)/len(snake), snake_first_color[player], snake_last_color[player]))
    new_snake_color = snake_first_color[player]

    for i in range(len(snake)):
        rect = pygame.Rect(snake[i][0]*block_size, snake[i][1]*block_size, block_size, block_size)
        
        new_snake_color = (new_snake_color[0]-snake_color_iteration[0], new_snake_color[1]-snake_color_iteration[1], new_snake_color[2]-snake_color_iteration[2])
        pygame.draw.rect(screen, new_snake_color, rect)


def drawFood(pos: tuple, block_size):
    rect = pygame.Rect(pos[0]*block_size, pos[1]*block_size, block_size, block_size)
    pygame.draw.rect(screen, food_color, rect, 0, 20)


def drawPortal(pos: tuple, block_size):
    rect = pygame.Rect(pos[0]*block_size, pos[1]*block_size, block_size, block_size)
    pygame.draw.rect(screen, randomize_color(portal_first_color, portal_last_color), rect, 10, 20)


def drawObstacles(obstacle: list, block_size):
    for i in range(len(obstacle)):
        rect = pygame.Rect(obstacle[i][0]*block_size, obstacle[i][1]*block_size, block_size, block_size)
        pygame.draw.rect(screen, obstacle_color, rect)


def draw_end_screen(scoreText: text.Text, underText: text.Text):
    margin = 10
    
    scoreText.set_font_size(screen.get_width() / 20)
    underText.set_font_size(screen.get_width() / 30)

    scoreText.rect.center = (screen.get_width() / 2, screen.get_height() / 2)
    underText.rect.center = (screen.get_width() / 2, screen.get_height() / 2 + scoreText.get_height() + margin)

    scoreText.draw(screen)
    underText.draw(screen)


def clear_screen():
    screen.fill("black")


def randomize_color(colorLimit1, colorLimit2):
    r = random.randint(colorLimit1[0], colorLimit2[0])
    g = random.randint(colorLimit1[1], colorLimit2[1])
    b = random.randint(colorLimit1[2], colorLimit2[2])
    rgb = (r,g,b)
    return rgb



screen = None
screen_color = "black"

grid_first_color = (0,0,0)
grid_last_color = (33,33,33)

snake_first_color = [(0,255,0), (255,0,0)]
snake_last_color = [(0,150,0), (150,0,0)]

portal_first_color = (0,0,150)
portal_last_color = (0,200,255)

food_color = "red"

obstacle_color = (200,200,200)
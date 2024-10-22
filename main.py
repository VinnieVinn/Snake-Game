import pygame
import random
import graphics

def randomizeFoodPos():
    while True:
        pos = pygame.Vector2(random.randint(0, grid_width-1), random.randint(0, grid_height-1))
        
        for i in snake:
            if pos == i:
                break
        else: 
            return pos


def addListHead(list: list, item):
    snake.insert(0, item)


def isCollidingWithSelf():
    head = snake[0]
    for i in range(1, len(snake)-1):
        if head == snake[i]:
            return True
    else:
        return False


def isCollidingWithWall():
    head = snake[0]
    if head[0] > grid_width-1: return True
    if head[1] > grid_height-1: return True
    if head[0] < 0: return True
    if head[1] < 0: return True
    return False

pygame.init()

grid_width = 15
grid_height = 10
grid_color = (33,33,33)
block_size = 70

empty_color = "black"
graphics.display(grid_width*block_size, grid_height*block_size, empty_color)
clock = pygame.time.Clock()
running = True
dt = 0
getFrames = 0
gameSpeed = 8 # Frames
fpsLimit = 120

snake = [(0, 0), (1, 0), (2, 0), (2, 1)]
snake_start_pos = (0, 0)
snake_color = "green"
snake_dir = pygame.Vector2(0, 1)
UP = (0, -1)
DOWN = (0, 1)
RIGHT = (1, 0)
LEFT = (-1, 0)

food_color = "red"
food_pos = randomizeFoodPos()

timer = 0
score = 0

while running:
    pygame.display.set_caption(f"Score: {score}            fps: {int(clock.get_fps())}")
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    # fill the screen with a color to wipe away anything from last frame
    graphics.clear_screen()
    
    if isCollidingWithSelf():
        exit()
    if isCollidingWithWall():
        exit()




    graphics.drawGrid(grid_width, grid_height, block_size, grid_color)
    graphics.drawSnake(snake, block_size, snake_color)
    graphics.drawFood(food_pos, block_size, food_color)


    # Randomizes food pos
    keys = pygame.key.get_pressed()

    
    if keys[pygame.K_w]:
        snake_dir = UP
    if keys[pygame.K_s]:
        snake_dir = DOWN
    if keys[pygame.K_d]:
        snake_dir = RIGHT
    if keys[pygame.K_a]:
        snake_dir = LEFT



    if timer*gameSpeed / fpsLimit >= 1:
        """if isCollidingWithWall():

            if snake_dir == UP: d
                print(snake[0][1])
                addListHead(snake, (snake[0][0], grid_height-1))"""
        addListHead(snake, snake[0]+snake_dir)
        
        if snake[0] == food_pos:
            score += 1
            snake.append(snake[len(snake)-1])
            print(snake)
            food_pos = randomizeFoodPos()
        else:
            snake.pop(len(snake)-1)

        timer = 0
    else:
        timer += 1

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(fpsLimit) / 1000
    getFrames += 1

pygame.quit()
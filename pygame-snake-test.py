import pygame
import random



def generate_grid(width: int, height: int):
    return list([[0]*height]*width)


def drawGrid(grid: list, block_size: int, color):
    for x in range(0, len(grid)):
        for y in range(0, len(grid[0])):
            rect = pygame.Rect(x*block_size, y*block_size, block_size, block_size)
            pygame.draw.rect(screen, color, rect, 1)


def drawSnake(snake: list, block_size: int, color):
    for i in range(len(snake)):
        rect = pygame.Rect(snake[i][0]*block_size, snake[i][1]*block_size, block_size, block_size)
        pygame.draw.rect(screen, color, rect)


def drawFood(pos: tuple, block_size, color):
    rect = pygame.Rect(pos[0]*block_size, pos[1]*block_size, block_size, block_size)
    pygame.draw.rect(screen, color, rect)


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


# pygame setup
pygame.init()

grid_width = 15
grid_height = 10
grid_color = (33,33,33)
block_size = 70
grid = generate_grid(grid_width, grid_height)

screen = pygame.display.set_mode((grid_width*block_size, grid_height*block_size))
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

empty_color = "black"
screen.fill(empty_color)

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
    screen.fill("black")
    
    if isCollidingWithSelf():
        exit()
    if isCollidingWithWall():
        exit()




    drawGrid(grid, block_size, grid_color)
    drawSnake(snake, block_size, snake_color)
    drawFood(food_pos, block_size, food_color)


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
import pygame
import random
import graphics # type: ignore
import gamelogic # type: ignore

pygame.init()

grid_width = 15
grid_height = 10
block_size = 70

graphics.display(grid_width*block_size, grid_height*block_size)
clock = pygame.time.Clock()
running = True
dt = 0
getFrames = 0
gameSpeed = 8 # Frames
fpsLimit = 120

snake = [(0, 0), (1, 0), (2, 0), (2, 1)]
snake_start_pos = (0, 0)
snake_dir = pygame.Vector2(0, 1)
UP = (0, -1)
DOWN = (0, 1)
RIGHT = (1, 0)
LEFT = (-1, 0)

food_pos = gamelogic.randomizeFoodPos(snake, grid_width, grid_height)

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
    
    if gamelogic.isCollidingWithSelf(snake):
        exit()
    if gamelogic.isCollidingWithWall(snake, grid_width, grid_height):
        exit()




    graphics.drawGrid(grid_width, grid_height, block_size)
    graphics.drawSnake(snake, block_size)
    graphics.drawFood(food_pos, block_size)


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
        gamelogic.addListHead(snake, snake[0]+snake_dir)
        if gamelogic.hasEaten(snake, food_pos):
            food_pos = gamelogic.randomizeFoodPos(snake, grid_width, grid_height)
            score += 1
        else:
            gamelogic.removeTail(snake)
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
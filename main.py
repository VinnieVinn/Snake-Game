import pygame
import random
import graphics # type: ignore
import gamelogic # type: ignore
import main_menu  # type: ignore


grid_width = 15
grid_height = 10
block_size = 70

graphics.display(grid_width*block_size, grid_height*block_size)
clock = pygame.time.Clock()
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
last_direction = DOWN
input_buffer = []

food_pos = gamelogic.randomizeFoodPos(grid_width, grid_height, snake)
portal_1 = gamelogic.randomizeFoodPos(grid_width, grid_height, snake + [food_pos])
portal_2 = gamelogic.randomizeFoodPos(grid_width, grid_height, snake + [food_pos, portal_1])

timer = 0
score = 0

def new_input(direction):
    if direction == last_direction or direction in input_buffer:
        return
    if direction[0] + snake_dir[0] == 0 and direction[1] + snake_dir[1] == 0:
        return
    if len(input_buffer) < 2:
        input_buffer.append(direction)
    else:
        input_buffer[1] = direction

running = main_menu.startGame
while running:
    pygame.display.set_caption(f"Score: {score}            fps: {int(clock.get_fps())}")
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    # fill the screen with a color to wipe away anything from last frame
    graphics.clear_screen()




    graphics.drawGrid(grid_width, grid_height, block_size)
    graphics.drawPortal(portal_1, block_size)
    graphics.drawPortal(portal_2, block_size)
    graphics.drawSnake(snake, block_size)
    graphics.drawFood(food_pos, block_size)


    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_w]:
        new_input(UP)
    if keys[pygame.K_s]:
        new_input(DOWN)
    if keys[pygame.K_d]:
        new_input(RIGHT)
    if keys[pygame.K_a]:
        new_input(LEFT)

    if timer*gameSpeed / fpsLimit >= 1:
        if len(input_buffer) != 0:
            snake_dir = input_buffer.pop(0)
            last_direction = snake_dir
            
        
        gamelogic.addListHead(snake, snake[0]+snake_dir)
        
        if snake[0] == portal_1:
            snake[0] = portal_2
        elif snake[0] == portal_2:
            snake[0] = portal_1

        if snake[-1] == portal_1 or snake[-1] == portal_2:
            portal_1 = gamelogic.randomizeFoodPos(grid_width, grid_height, snake + [food_pos, portal_2])
            portal_2 = gamelogic.randomizeFoodPos(grid_width, grid_height, snake + [food_pos, portal_1])

        if snake[0] == food_pos:
            food_pos = gamelogic.randomizeFoodPos(grid_width, grid_height, snake)
            score += 1
        else:
            gamelogic.removeTail(snake)
        timer = 0
    else:
        timer += 1


    if gamelogic.isCollidingWithSelf(snake):
        running = False
    if gamelogic.isCollidingWithWall(snake, grid_width, grid_height):
        running = False

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(fpsLimit) / 1000
    getFrames += 1

print(score)
pygame.quit()
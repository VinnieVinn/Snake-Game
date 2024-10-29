import pygame
import random
import graphics # type: ignore
import gamelogic # type: ignore
import main_menu  # type: ignore
import text
import filehandler
pygame.init()

grid_width = main_menu.gridWidth
grid_height = main_menu.gridHeight
block_size = 50
obstacleAmount = main_menu.obstacles

graphics.display(grid_width*block_size, grid_height*block_size)
clock = pygame.time.Clock()
dt = 0
getFrames = 0
gameSpeed = main_menu.gameSpeed # Frames
fpsLimit = 120

snake = [[0, 0], [1, 0], [2, 0], [2, 1]]
snake_start_pos = (0, 0)
snake_dir = pygame.Vector2(0, 1)
UP = (0, -1)
DOWN = (0, 1)
RIGHT = (1, 0)
LEFT = (-1, 0)
last_direction = DOWN
input_buffer = []

obstacleTypes = [[(0, 0), (0, 1), (0, 2)], 
            [(0, 0), (0, 1), (1, 1)],
            [(0, 0), (1, 0), (2, 0)]]
obstacles = []

for i in range(obstacleAmount):
    obstacles += gamelogic.randomizeObstaclePos(obstacleTypes, grid_width, grid_height, snake + obstacles)


food_pos = gamelogic.randomPos(grid_width, grid_height, snake + obstacles)
portal_1 = pygame.Vector2(gamelogic.randomPos(grid_width, grid_height, snake + obstacles + [food_pos]))
portal_2 = pygame.Vector2(gamelogic.randomPos(grid_width, grid_height, snake + obstacles + [food_pos, portal_1]))


timer = 0
score = 0
highscore = filehandler.get_best()

end = False

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
    pygame.display.set_caption(f"Score: {score}            Highscore: {highscore if int(highscore) > score else score}            fps: {int(clock.get_fps())}")
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()  

    keys = pygame.key.get_pressed()

    if end: 
        scoreText = text.Text(0, 0, f"Du fick {score} poäng!", "freesansbold.ttf", 0, True, "white", "black")
        underText = text.Text(0, 0, "Bla Bla tryck mellanslag.", "freesansbold.ttf", 0, True, (200,200,200), "black")
        graphics.draw_end_screen(scoreText, underText)

        if keys[pygame.K_SPACE]:
            running = False
    else:
        # fill the screen with a color to wipe away anything from last frame
        graphics.clear_screen()

        graphics.drawGrid(grid_width, grid_height, block_size)
        graphics.drawObstacles(obstacles, block_size)
        graphics.drawPortal(portal_1, block_size)
        graphics.drawPortal(portal_2, block_size)
        graphics.drawSnake(snake, block_size)
        graphics.drawFood(food_pos, block_size)


        if keys[pygame.K_w]:
            new_input(UP)
        if keys[pygame.K_s]:
            new_input(DOWN)
        if keys[pygame.K_d]:
            new_input(RIGHT)
        if keys[pygame.K_a]:
            new_input(LEFT)

        if timer*gameSpeed >= fpsLimit:
            if len(input_buffer) != 0:
                snake_dir = input_buffer.pop(0)
                last_direction = snake_dir


            gamelogic.addListHead(snake, snake[0]+snake_dir)

            if gamelogic.isCollidingWithSelf(snake):
                end = True                
            if gamelogic.isCollidingWithObstacle(snake, obstacles):
                end = True

            if gamelogic.isCollidingWithWall(snake, grid_width, grid_height):
                if snake_dir == UP: 
                    snake[0][1] = grid_height-1
                elif snake_dir == DOWN: 
                    snake[0][1] = 0
                elif snake_dir == RIGHT:
                    snake[0][0] = 0
                elif snake_dir == LEFT:
                    snake[0][0] = grid_width-1
        

            if snake[0] == portal_1:
                snake[0] = portal_2
            elif snake[0] == portal_2:
                snake[0] = portal_1

            if snake[-1] == portal_1 or snake[-1] == portal_2:
                portal_1 = pygame.Vector2(gamelogic.randomPos(grid_width, grid_height, snake + obstacles + [food_pos, portal_2]))
                portal_2 = pygame.Vector2(gamelogic.randomPos(grid_width, grid_height, snake + obstacles + [food_pos, portal_1]))

            if snake[0] == food_pos:
                food_pos = gamelogic.randomPos(grid_width, grid_height, snake + obstacles)
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

print(score)
filehandler.add_score(score)
pygame.quit()
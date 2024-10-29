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

snakes = [[(0, 0), (1, 0), (2, 0), (2, 1)]]

UP = (0, -1)
DOWN = (0, 1)
RIGHT = (1, 0)
LEFT = (-1, 0)

last_direction = [DOWN, DOWN]
input_buffer = [[]]

snake_dirs = [(0, 1)]
if main_menu.players == 2:
    snakes.append([(grid_width - 1, 0), (grid_width - 2, 0), (grid_width - 3, 0), (grid_width - 3, 1)])
    snake_dirs.append((0, 1))
    input_buffer.append([])

obstacleTypes = [[(0, 0), (0, 1), (0, 2)], 
            [(0, 0), (0, 1), (1, 1)],
            [(0, 0), (1, 0), (2, 0)],
            [(0, 0), (0, 1), (0, 2)],
            [(0, 0), (1, 0), (0, 1), (1, 1)],
            [(1, 0), (1, 1), (1, 2), (0, 2)]]
obstacles = []
spawn_ignore_list = snakes[0].copy()
if main_menu.players == 2:
    spawn_ignore_list += snakes[1]
for i in range(obstacleAmount):
    obstacles += gamelogic.randomizeObstaclePos(obstacleTypes, grid_width, grid_height, spawn_ignore_list)
spawn_ignore_list += obstacles

food_pos = gamelogic.randomPos(grid_width, grid_height, spawn_ignore_list)
spawn_ignore_list.append(food_pos)

portal_1 = gamelogic.randomPos(grid_width, grid_height, spawn_ignore_list)
spawn_ignore_list.append(portal_1)

portal_2 = gamelogic.randomPos(grid_width, grid_height, spawn_ignore_list)


timer = 0
score = 0
highscore = filehandler.get_best()

end = False

def new_input(direction, player = 0):
    if direction == last_direction[player] or direction in input_buffer[player]:
        return
    if gamelogic.sumTuples(direction, snake_dirs[player]) == (0, 0):
        return
    if len(input_buffer[player]) < 2:
        input_buffer[player].append(direction)
    else:
        input_buffer[player][1] = direction

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
        scoreText = text.Text(0, 0, f"Ni fick {score} poäng!", "freesansbold.ttf", 0, True, "white", "black")
        underText = text.Text(0, 0, "Tryck på mellanslag för att avsluta", "freesansbold.ttf", 0, True, (200,200,200), "black")
        graphics.draw_end_screen(scoreText, underText)

        if keys[pygame.K_SPACE]:
            running = False
    else:
        graphics.drawFood(food_pos, block_size) # NECESSARY!
        graphics.drawObstacles(obstacles, block_size) # NECESSARY!
        for p in range(0, main_menu.players):
            graphics.drawSnake(snakes[p], block_size, p)


        if keys[pygame.K_w]:
            new_input(UP)
        if keys[pygame.K_s]:
            new_input(DOWN)
        if keys[pygame.K_d]:
            new_input(RIGHT)
        if keys[pygame.K_a]:
            new_input(LEFT)

        if main_menu.players == 2:
            if keys[pygame.K_UP]:
                new_input(UP, 1)
            if keys[pygame.K_DOWN]:
                new_input(DOWN, 1)
            if keys[pygame.K_RIGHT]:
                new_input(RIGHT, 1)
            if keys[pygame.K_LEFT]:
                new_input(LEFT, 1)

        if timer*gameSpeed >= fpsLimit:
            graphics.clear_screen() # NECESSARY!

            graphics.drawGrid(grid_width, grid_height, block_size)
            graphics.drawObstacles(obstacles, block_size)
            graphics.drawPortal(portal_1, block_size)
            graphics.drawPortal(portal_2, block_size)
            for p in range(0, main_menu.players):
                graphics.drawSnake(snakes[p], block_size, p)
            graphics.drawFood(food_pos, block_size)

            for player in range(0, main_menu.players):
                if len(input_buffer[player]) != 0:
                    snake_dirs[player] = input_buffer[player].pop(0)
                    last_direction[player] = snake_dirs[player]

                snake = snakes[player]
                snake_dir = snake_dirs[player]

                gamelogic.addListHead(snake, gamelogic.sumTuples(snake[0], snake_dir))

                if gamelogic.isCollidingWithSnake(snakes, player):
                    end = True                
                if gamelogic.isCollidingWithObstacle(snake, obstacles):
                    end = True

                if gamelogic.isCollidingWithWall(snake, grid_width, grid_height):
                    if snake_dir == UP: 
                        snake[0] = (snake[0][0], grid_height-1)
                    elif snake_dir == DOWN: 
                        snake[0] = (snake[0][0], 0)
                    elif snake_dir == RIGHT:
                        snake[0] = (0, snake[0][1])
                    elif snake_dir == LEFT:
                        snake[0] = (grid_width - 1, snake[0][1])
            

                if snake[0] == portal_1:
                    snake[0] = portal_2
                elif snake[0] == portal_2:
                    snake[0] = portal_1
                combined = snakes[0] + snakes[1] if main_menu.players == 2 else snakes[0]
                if snake[-1] == portal_1 or snake[-1] == portal_2:
                    portal_1 = gamelogic.randomPos(grid_width, grid_height, combined + obstacles + [food_pos, portal_2])
                    portal_2 = gamelogic.randomPos(grid_width, grid_height, combined + obstacles + [food_pos, portal_1])

                if snake[0] == food_pos:
                    food_pos = gamelogic.randomPos(grid_width, grid_height, combined + obstacles + [portal_1, portal_2])
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
import pygame
import button
import text
import os

def load_img(location):
    img = pygame.image.load(directory + location).convert_alpha()
    return button.Button(0, 0, img, button_scale)

def flip_img_x(img):
    img.flip_img_x()
    return img

def flip_img_y(img):
    return pygame.transform.flip(img, False, True).convert_alpha()

def load_text(prompt: str, font: str, fontSize: int, antialias: bool, color, bgColor):
    return text.Text(0, 0, prompt, font, fontSize, antialias, color, bgColor)

pygame.init()



screen_width = 800
screen_height = 800
button_scale = 3 # x times
margin = (16, 16) # pixels (x, y)
backgroundColor = "black"
directory = os.path.dirname(os.path.realpath(__file__))

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Main Menu')


players = 1
gridWidth = 10
gridHeight = 10
obstacles = 0
gameSpeed = 6

options = [{"Start":load_img("\\sprites\\start.png")}, 
           {"PlayersText":load_text("Spelare:", "freesansbold.ttf", 32, True, "green", "black")},
           {
               "PlayersLeftArrow":load_img("\\sprites\\arrow.png"), 
               "PlayersValue":load_text(f"{players}", "freesansbold.ttf", 47, True, "black", "#ffffff00"), 
               "PlayersRightArrow": flip_img_x(load_img("\\sprites\\arrow.png"))
               },
           {"WidthText":load_text("Spelplan bredd:", "freesansbold.ttf", 32, True, "green", "black")},
           {
               "WidthLeftArrow":load_img("\\sprites\\arrow.png"), 
               "WidthValue":load_text(f"{gridWidth}", "freesansbold.ttf", 47, True, "black", "#ffffff00"), 
               "WidthRightArrow": flip_img_x(load_img("\\sprites\\arrow.png"))
               },
           {
               "HeightText":load_text("Spelplan höjd:", "freesansbold.ttf", 32, True, "green", "black")},
           {
               "HeightLeftArrow":load_img("\\sprites\\arrow.png"), 
               "HeightValue":load_text(f"{gridHeight}", "freesansbold.ttf", 47, True, "black", "#ffffff00"), 
               "HeightRightArrow": flip_img_x(load_img("\\sprites\\arrow.png"))
               },
           {"ObstaclesText":load_text("Hinder:", "freesansbold.ttf", 32, True, "green", "black")},
           {
               "ObstaclesLeftArrow":load_img("\\sprites\\arrow.png"), 
               "ObstaclesValue":load_text(f"{obstacles}", "freesansbold.ttf", 47, True, "black", "#ffffff00"), 
               "ObstaclesRightArrow": flip_img_x(load_img("\\sprites\\arrow.png"))
               },
           {"GameSpeedText":load_text("Hastighet:", "freesansbold.ttf", 32, True, "green", "black")},
           {
               "GameSpeedLeftArrow":load_img("\\sprites\\arrow.png"), 
               "GameSpeedValue":load_text(f"{gameSpeed}", "freesansbold.ttf", 47, True, "black", "#ffffff00"), 
               "GameSpeedRightArrow": flip_img_x(load_img("\\sprites\\arrow.png"))
               },
           {"Exit":load_img("\\sprites\\exit.png")}, 
           ]

i = 0
itemVerticalOffset = margin[1]
for dict in options:
    imgSize = None
    textSize = None
    itemHorizontalOffset = margin[0]

    for pair in dict.items():
        pair[1].set_x(itemHorizontalOffset)
        pair[1].set_y(itemVerticalOffset)

        if isinstance(pair[1], button.Button): # IMG
            imgSize = (pair[1].get_width(), pair[1].get_height())
            options[i].update({pair[0]:pair[1]})
            itemHorizontalOffset += imgSize[0] * button_scale + margin[0]

        elif isinstance(pair[1], text.Text): # TEXT 
            textSize = (pair[1].get_width(), pair[1].get_height())
            options[i].update({pair[0]:pair[1]})

            pair[1].set_x(itemHorizontalOffset)
            pair[1].set_y(itemVerticalOffset)
            itemHorizontalOffset += textSize[0] + margin[0]
        
    if dict != {}: 
        if imgSize != None:
            itemVerticalOffset += imgSize[1] * button_scale + margin[1]
        elif textSize != None: 
            itemVerticalOffset += textSize[1] + margin[1]
    i += 1


startGame = False

running = True
while running: 

    #event handler
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            programRunning = False
            exit()
    
    # Graphics
    screen.fill(backgroundColor)


    # Render loop
    for dict in options:
        for item in dict.values():          
            if isinstance(item, button.Button): # IMG
                item.draw(screen)
            elif isinstance(item, text.Text): # TEXT 
                item.draw(screen)
    

    

    if options[0].get("Start").pressed():
        startGame = True
        running = False
    if options[-1].get("Exit").pressed():
        running = False

    if options[2].get("PlayersLeftArrow").pressed():
        players = 1
        options[2]["PlayersValue"].set_prompt(str(players))
    elif options[2].get("PlayersRightArrow").pressed():
        players = 2
        options[2]["PlayersValue"].set_prompt(str(players))

    elif options[4].get("WidthLeftArrow").pressed():
        gridWidth -= 1
        if gridWidth < 1: gridWidth = 1
        options[4]["WidthValue"].set_prompt(str(gridWidth))
    elif options[4].get("WidthRightArrow").pressed():
        gridWidth += 1
        options[4]["WidthValue"].set_prompt(str(gridWidth))

    elif options[6].get("HeightLeftArrow").pressed():
        gridHeight -= 1
        if gridHeight < 1: gridHeight = 1
        options[6]["HeightValue"].set_prompt(str(gridHeight))
    elif options[6].get("HeightRightArrow").pressed():
        gridHeight += 1
        options[6]["HeightValue"].set_prompt(str(gridHeight))

    elif options[8].get("ObstaclesLeftArrow").pressed():
        obstacles -= 1
        if obstacles < 0: obstacles = 0
        options[8]["ObstaclesValue"].set_prompt(str(obstacles))
    elif options[8].get("ObstaclesRightArrow").pressed():
        obstacles += 1
        options[8]["ObstaclesValue"].set_prompt(str(obstacles))

    elif options[10].get("GameSpeedLeftArrow").pressed():
        gameSpeed -= 1
        if gameSpeed < 1: gameSpeed = 1
        options[10]["GameSpeedValue"].set_prompt(str(gameSpeed))
    elif options[10].get("GameSpeedRightArrow").pressed():
        gameSpeed += 1
        options[10]["GameSpeedValue"].set_prompt(str(gameSpeed))

        

    pygame.display.update()

pygame.quit()
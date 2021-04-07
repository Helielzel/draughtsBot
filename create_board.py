import itertools
import pygame as pg


def create_board(gameBoard):
    circles = list()
    # circles[0] = [color, type, x, y] --> draw_pawns(circles)

    for key in gameBoard:
        to_push = []
        to_pushcoord = ""
        splitted_key = []

        if gameBoard[key][1] == "":
            continue
        if gameBoard[key][2] == "p1":
            to_push.append("WHITE")
        else:
            to_push.append("BLACK")
        #done with color.
        if gameBoard[key][1] == "p":
            to_push.append("pawn")
        else:
            to_push.append("queen")
        #done with type

        splitted_key.append(key[0])
        to_pushcoord += key[1]
        try:
            to_pushcoord += key[2]
        except:
            pass
        splitted_key.append(to_pushcoord)

        #now key is splitted like that : "a10" -> a, 10

        alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
        num = ["10", "9", "8", "7", "6", "5", "4", "3", "2", "1"]

        to_push.append((10 + alpha.index(splitted_key[0]) * 20) * 1.4)
        to_push.append((10 + num.index(splitted_key[1]) * 20) * 1.4)
        
        circles.append(to_push)

    window(circles)

def window(pawn_coord):
    pg.init()

    BLACK = pg.Color('black')
    WHITE = pg.Color('white')
    BLUE = pg.Color(114, 164, 212)

    screen = pg.display.set_mode((280, 280))
    #clock = pg.time.Clock()

    colors = itertools.cycle((BLUE, WHITE))
    tile_size = 28
    width, height = 10*tile_size, 10*tile_size
    background = pg.Surface((width, height))

    for y in range(0, height, tile_size):
        for x in range(0, width, tile_size):
            rect = (x, y, tile_size, tile_size)
            pg.draw.rect(background, next(colors), rect)
        next(colors)

    screen.blit(background, (0, 0))

    #pawn_coord = [color, type, x, y]
    for line in pawn_coord:
        if len(line) != 4:
            continue
        pg.draw.circle(background, line[0], (line[2], line[3]), 9)

    screen.fill((60, 70, 90))
    screen.blit(background, (0, 0))
    pg.image.save(screen, "img/coucou.png")
    
    """
    game_exit = False
    while not game_exit:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_exit = True

        screen.fill((60, 70, 90))
        screen.blit(background, (100, 100))

        pg.display.flip()
        clock.tick(30)
    """
    pg.quit()
    return
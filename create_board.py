import itertools
import pygame as pg

def window(pawn_coord):
    pg.init()

    BLACK = pg.Color('black')
    WHITE = pg.Color('white')
    GREY = pg.Color('grey')

    screen = pg.display.set_mode((400, 400))
    clock = pg.time.Clock()

    colors = itertools.cycle((BLACK, WHITE))
    tile_size = 20
    width, height = 10*tile_size, 10*tile_size
    background = pg.Surface((width, height))

    for y in range(0, height, tile_size):
        for x in range(0, width, tile_size):
            rect = (x, y, tile_size, tile_size)
            pg.draw.rect(background, next(colors), rect)
        next(colors)

    screen.blit(background, (100, 100))

    #pawn_coord = [color, type, x, y]
    for line in pawn_coord:
        if len(line) != 4:
            continue
        pg.draw.circle(background, line[0], (line[2], line[3]), 8)
    
    #pg.draw.circle(background, GREY, (10, 50), 8) #a9 -> 10 50
    #pg.draw.circle(background, GREY, (50, 10), 8) #c10 -> 50 10 
    #pg.draw.circle(background, GREY, (30, 10), 8) #b10 -> 30 10
    #pg.draw.circle(background, GREY, (70, 10), 8)
    #pg.draw.circle(background, GREY, (70, 10), 8)
    

    #pg.image.save(screen, "coucou.png")

    game_exit = False
    while not game_exit:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_exit = True

        screen.fill((60, 70, 90))
        screen.blit(background, (100, 100))

        pg.display.flip()
        clock.tick(30)

    pg.quit()
    return
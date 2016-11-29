import pygame as pg
import sys
from random import randint
from Pipe import Pipe
from Bird import Bird


def detect_colision(pipes, bird):
    if bird.rect.colliderect(pipes.pipe_down) == 1 or bird.rect.colliderect(pipes.pipe_up) == 1:
        return True
    elif bird.rect.y < 0 or bird.rect.y > 440:
        return True
    return False

def main():
    pg.init()
    counter = 0

    pg.font.init()
    font = pg.font.SysFont('Arial',40)

    screen = pg.display.set_mode((400,450))
    clock = pg.time.Clock()
    pipes = [Pipe(30)]
    player = Bird()
    while True:
        clock.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
                player.jump()
        screen.fill((0,0,0))
        if pipes[0].pipe_down.x < 170 and len(pipes) < 2:
            pipes.append(Pipe(randint(50,300)))
        if pipes[0].pipe_down.x < -30:
            del pipes[0]
            counter += 1
       # pg.draw.rect(screen, (255, 255, 255), pg.Rect(10,10,10,10))
        for p in pipes:
            p.draw(screen)
            p.update()

        if detect_colision(pipes[0], player):
            main()
        player.update()
        player.draw(screen)
        screen.blit(font.render(str(counter), -1, (255, 0, 0)), (200, 50))
        pg.display.flip()

if __name__ == '__main__':
    main()
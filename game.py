import pygame as pg
import sys
from ga import GeneticAlgorithm
from random import randint
from Pipe import Pipe
from Bird import Bird
import time


def detect_colision(pipes, bird):
    if bird.rect.colliderect(pipes.pipe_down) == 1 or bird.rect.colliderect(pipes.pipe_up) == 1:
        return True
    elif bird.rect.y < 0 or bird.rect.y > 440:
        return True
    return False

firstStart = True
gen = GeneticAlgorithm()


def main(firstStart=False, generation=1):
    counter = 0
    if firstStart:
        population = gen.population
    else:
        population = gen.evolve()

    fitness = 0
    deadcounter = 0

    #for p in population:
        #print(p.net.weights)

    pg.font.init()
    font = pg.font.SysFont('Arial',25)

    screen = pg.display.set_mode((400,450))
    clock = pg.time.Clock()
    pipes = [Pipe(87)]

    pg.init()

    #print(len(population))
    #print(population)
    while True:
        clock.tick(60)

        #if ai = none
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                pg.quit()
                sys.exit()

        fitness += 1
        screen.fill((0,0,0))
        if pipes[0].pipe_down.x < 170 and len(pipes) < 2:
            pipes.append(Pipe(randint(50,300)))
        if pipes[0].pipe_down.x < 70:
            del pipes[0]

            counter += 1
       # pg.draw.rect(screen, (255, 255, 255), pg.Rect(10,10,10,10))
        for p in pipes:
            p.draw(screen)
            p.update()

        for player in population:
            if not player.dead:
                if detect_colision(pipes[0], player):
                    player.dead = True
                    player.fitness += 1000 * counter
                    deadcounter += 1
                if deadcounter >= len(population):
                    #print('gen')
                    main(generation=generation+1)


                player.update(pipes[0])
                player.fitness += 1
                player.draw(screen)

        screen.blit(font.render('Birds left:{}'.format(str(100-deadcounter)), -1, (255, 0, 0)), (10, 150))
        screen.blit(font.render('Progress:{}'.format(str(counter)), -1, (255, 255, 0)), (10, 50))
        screen.blit(font.render('Fitness:{}'.format(fitness), -1, (0, 0, 255)), (10, 250))
        screen.blit(font.render('Generation:{}'.format(generation), -1, (0, 255, 0)), (10, 350))



        pg.display.flip()

if __name__ == '__main__':
    main(firstStart=True)
import pygame as pg

class Pipe:
    def __init__(self,x):
        self.pipe_up = pg.Rect((400,0),(30,x))
        self.pipe_down = pg.Rect((400,x+100),(30,350-x))

    def update(self):
        self.pipe_up.move_ip(-1,0)
        self.pipe_down.move_ip(-1,0)

    def draw(self, screen):
        pg.draw.rect(screen,(255,255,255),self.pipe_up)
        pg.draw.rect(screen,(255,255,255),self.pipe_down)
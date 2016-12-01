import pygame as pg
import nn
import numpy as np
from random import randint

class Bird:
    def __init__(self, weights=None, ai=None):
        self.x = 60
        self.y = randint(10,430)
        self.speed = 2
        self.ai = ai
        self.rect = pg.Rect(self.x,self.y,20,20)
        self.dead = False
        if not weights:
            self.net = nn.Network()
        else: self.net = nn.Network(weights)
        self.fitness = 0

    def update(self, pipe):
        out = self.net.feedforward([np.abs(self.rect.x - pipe.pipe_up.x), np.abs(self.rect.y - pipe.pipe_down.y)])
        if out > 0.5:
            self.jump()
        self.move()

    def move(self):
        # checking if jumped recently if so decrease velocity until its default again
        if self.speed < 2:
            self.speed += 2
        self.rect.move_ip(0, self.speed)

    def jump(self):
        self.speed = -10
        self.fitness -= 3

    def draw(self, screen):
        pg.draw.rect(screen, (100,100,100), self.rect)



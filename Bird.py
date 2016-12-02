import pygame as pg
import nn
import numpy as np
import constants as cn
from random import randint

class Bird:
    def __init__(self, weights=None, ai=None):
        self.x = 60
        self.y = randint(10,cn.HEIGHT-10)
        self.speed = 4
        self.ai = ai
        self.rect = pg.Rect(self.x,self.y,cn.B_WIDTH, cn.B_HEIGHT)
        self.dead = False
        if not weights:
            self.net = nn.Network()
        else: self.net = nn.Network(weights)
        self.fitness = 0

    def update(self, pipe):
        self.image = pg.image.load('assets/0.png')
        out = self.net.feedforward([(self.rect.x - pipe.pipe_up.x), (self.rect.y - pipe.pipe_down.y)])
        if out > 0.5:
            self.jump()
        self.move()

    def move(self):
        # checking if jumped recently if so decrease velocity until its default again
        if self.speed < 4:
            self.speed += 1
            self.image = pg.image.load('assets/1.png')
        else: self.image = pg.image.load('assets/0.png')
        self.rect.move_ip(0,self.speed)

    def jump(self):
        self.speed = -12
        self.fitness -= 3

    def draw(self, screen):
        screen.blit(self.image.convert_alpha(),self.rect)




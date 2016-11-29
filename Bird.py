import pygame as pg

class Bird:
    def __init__(self):
        self.x = 60
        self.y = 200
        self.speed = 2
        self.rect = pg.Rect(self.x,self.y,20,20)

    def update(self):
        if self.speed < 2:
            self.speed += 2
        self.rect.move_ip(0,self.speed)

    def jump(self):
        self.speed = -15

    def draw(self, screen):
        pg.draw.rect(screen, (100,100,100), self.rect)



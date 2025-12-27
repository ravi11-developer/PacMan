import pygame
from pygame.locals import *
from vector import Vector2
from constants import *
from entity import Entity
from modes import modeController
class Ghost(Entity):
    def __init__(self, node,pacman=None):
        Entity.__init__(self,node)
        self.name=GHOST
        self.points=200
        self.goal=Vector2()
        self.directionMethod=self.goalDiretion
        self.pacman=pacman
        self.mode=modeController(self)

    def update(self, dt):
        self.mode.update(dt)
        if self.mode.current is SCATTER:
            self.scatter()
        elif self.mode.current is CHASE:
            self.chase()
        Entity.update(self, dt)

    def scatter(self):
        self.goal = Vector2()

    def chase(self):
        self.goal = self.pacman.position


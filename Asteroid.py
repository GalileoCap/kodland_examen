import pygame
from pygame import Vector2
import numpy as np
import random

from Object import NPolygon

class Asteroid(NPolygon):
  def __init__(self):
    seed = random.random()

    # TODO: Get dimensions
    # TODO: Normal distribution to the center for directions
    side = random.randint(0, 3)
    if side == 0: # From the left
      pos = Vector2(-25, random.random() * 720) 
      target = Vector2(25, random.random() * 720)
    elif side == 1: # From the right
      pos = Vector2(1280 + 25, random.random() * 720)
      target = Vector2(-25, random.random() * 720)
    elif side == 2: # From the top
      pos = Vector2(random.random() * 1280, -25)
      target = Vector2(random.random() * 1280, 720 + 25)
    elif side == 3: # From the bottom
      pos = Vector2(random.random() * 1280, 720 + 25)
      target = Vector2(random.random() * 1280, -25)

    self.direction = (target - pos).normalize()
    self.movSpeed = seed * 10
    self.rotSpeed = 2*np.pi / (seed * 10)
    sides = random.randint(5, 16)

    super().__init__(pos, 'white', 25, sides)

  def tick(self, ctx):
    self._move(ctx)
    super().tick(ctx)

  def _move(self, ctx):
    self.rotate(self.rotSpeed * ctx.dt)
    self.pos += self.direction * self.movSpeed

import pygame
from pygame import Vector2
import numpy as np

from Object import Object, EquilateralTriangle

class Player(EquilateralTriangle):
  def __init__(self, pos):
    self.movSpeed = 250

    super().__init__(pos, 'white', 25, fromPos = False)
    self.rotate(np.pi) # Start looking up

  def tick(self, ctx):
    self._move(ctx)
    super().tick(ctx)

  def _move(self, ctx):
    keys = pygame.key.get_pressed()
    movSpeed = int(keys[pygame.K_w]) - int(keys[pygame.K_s])
    rotSpeed = int(keys[pygame.K_d]) - int(keys[pygame.K_a])

    deltaRot = np.pi * rotSpeed * ctx.dt
    self.rotate(deltaRot)

    deltaPos = (Vector2(0, movSpeed) * self.movSpeed * ctx.dt).rotate_rad(self.rotation)
    self.pos += deltaPos

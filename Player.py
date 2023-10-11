import pygame
from pygame import Vector2
import numpy as np

from Object import Object, EquilateralTriangle
from Control import Label

class Player(EquilateralTriangle):
  def __init__(self, pos):
    self.movSpeed = 250

    super().__init__(pos, 'white', 25, fromPos = False)
    self.rotate(np.pi) # Start looking up

    self.scoreboard = Label(Vector2(0, 0), 0, 0, '0', 'purple', 'white')
    self.score = 0

  def tick(self, ctx):
    self._move(ctx)
    self._score(ctx)
    super().tick(ctx)

  def draw(self, ctx):
    super().draw(ctx)
    self.scoreboard.draw(ctx)

  def _move(self, ctx):
    keys = pygame.key.get_pressed()
    movSpeed = int(keys[pygame.K_w]) - int(keys[pygame.K_s])
    rotSpeed = int(keys[pygame.K_d]) - int(keys[pygame.K_a])

    deltaRot = np.pi * rotSpeed * ctx.dt
    self.rotate(deltaRot)

    deltaPos = (Vector2(0, movSpeed) * self.movSpeed * ctx.dt).rotate_rad(self.rotation)
    self.pos += deltaPos

  def _score(self, ctx):
    self.score += ctx.dt
    self.scoreboard.text = f'Puntaje: {int(self.score)}'

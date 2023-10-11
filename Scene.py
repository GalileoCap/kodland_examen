import pygame
from pygame import Vector2

from Object import Object
from Player import Player
from Asteroid import Asteroid
from Button import Button

class Scene(Object):
  def __init__(self):
    self.objs = []

  def tick(self, ctx):
    self._tickObjs(ctx)
    super().tick(ctx)

  def draw(self, ctx):
    self._drawObjs(ctx)
    super().draw(ctx)

  def _tickObjs(self, ctx):
    for obj in self.objs:
      obj.tick(ctx)

  def _drawObjs(self, ctx):
    for obj in self.objs:
      obj.draw(ctx)

class MenuScene(Scene):
  def __init__(self):
    super().__init__()
    self.objs += [Button(Vector2(0, 0), 200, 50, 'Jugar', 'green', 'white', lambda ctx: print('Jugar'))]

class GameScene(Scene):
  def __init__(self):
    self.player = Player(Vector2(1280/2, 720/2)) # TODO: Get screen size at creation
    self.asteroids = []
    self.asteroidTimer = 1
    self.currAsteroidTimer = 0
    super().__init__()

  def tick(self, ctx):
    super().tick(ctx)
    self._spawnAsteroids(ctx)
    self._tickAll(ctx)
    self._checkColission(ctx)

  def draw(self, ctx):
    ctx.screen.fill('purple') # Fondo negro
    self._drawAll(ctx)
    super().draw(ctx)

  def _tickAll(self, ctx):
    self.player.tick(ctx)
    for a in self.asteroids:
      a.tick(ctx)

  def _drawAll(self, ctx):
    self.player.draw(ctx)
    for a in self.asteroids:
      a.draw(ctx)

  def _spawnAsteroids(self, ctx):
    self.currAsteroidTimer += ctx.dt
    if self.currAsteroidTimer >= self.asteroidTimer:
      self.asteroids.append(Asteroid())
      self.currAsteroidTimer = 0

  def _checkColission(self, ctx):
    if any((a.intersects(self.player) for a in self.asteroids)):
      ctx.setPaused(True)

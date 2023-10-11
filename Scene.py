import pygame
from pygame import Vector2

from Object import Object
from Player import Player

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

class MainScene(Scene):
  def __init__(self):
    self.objs = [
      Player(Vector2(1280/2, 720/2)), # TODO: Get screen size at creation
    ]

  def draw(self, ctx):
    ctx.screen.fill('purple') # Fondo negro
    super().draw(ctx)

import pygame
from pygame import Vector2
import numpy as np

class Object:
  def __init__(self, pos):
    self.pos = pos

  def tick(self, ctx):
    self.draw(ctx)

  def draw(self, ctx):
    pass

class Polygon(Object):
  def __init__(self, pos, color, points):
    super().__init__(pos)
    self.color = color
    self.points = points

  def draw(self, ctx):
    points = [point + self.pos for point in self.points]
    pygame.draw.polygon(ctx.screen, self.color, points)

  def rotate(self, rad):
    for point in self.points:
      point.rotate_ip_rad(rad)

class Rectangle(Polygon):
  def __init__(self, pos, color, base, height):
    points = [Vector2(-base/2, -height/2), Vector2(base/2, -height/2), Vector2(base/2, height/2), Vector2(-base/2, height/2)]
    super().__init__(pos, color, points)

class Square(Rectangle):
  def __init__(self, pos, color, side):
    super().__init__(pos, color, side, side)

class Player(Square):
  def __init__(self, pos):
    super().__init__(pos, 'white', 25)

  def tick(self, ctx):
    self.rotate(2*np.pi/2 * ctx.dt)
    super().tick(ctx)

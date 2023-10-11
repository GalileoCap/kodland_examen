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
    self.rotation = 0

  def draw(self, ctx):
    points = [point + self.pos for point in self.points]
    pygame.draw.polygon(ctx.screen, self.color, points)

  def rotate(self, rad):
    self.rotation += rad
    for point in self.points:
      point.rotate_ip_rad(rad)

class Rectangle(Polygon):
  def __init__(self, pos, color, base, height, *, fromPos):
    self.base = base
    self.height = height

    points = [Vector2(0, 0), Vector2(base, 0), Vector2(base, height), Vector2(0, height)]
    if not fromPos:
      centroid = (points[0] + points[1] + points[2] + points[3]) / 3
      points = [point - centroid for point in points]

    super().__init__(pos, color, points)

class Square(Rectangle):
  def __init__(self, pos, color, side, *, fromPos):
    self.side = side
    super().__init__(pos, color, side, side, fromPos = fromPos)

class Triangle(Polygon):
  def __init__(self, pos, color, base, height, *, fromPos):
    points = [Vector2(0, 0), Vector2(base, 0), Vector2(base/2, height)]
    if not fromPos:
      centroid = (points[0] + points[1] + points[2]) / 3
      points = [point - centroid for point in points]
    super().__init__(pos, color, points)

class EquilateralTriangle(Triangle):
  def __init__(self, pos, color, side, *, fromPos):
    height = np.sqrt(side**2 - (side/2)**2)
    super().__init__(pos, color, side, height, fromPos = fromPos)

import pygame
from pygame import Vector2

from Object import Rectangle

class Label(Rectangle):
  def __init__(self, pos, base, height, text, bgColor, fgColor, *, fromPos = True):
    super().__init__(pos, bgColor, base, height, fromPos = fromPos)
    self.text = text
    self.fgColor = fgColor

  def draw(self, ctx):
    super().draw(ctx)
    self._drawText(ctx)

  def _drawText(self, ctx):
    text = ctx.font.render(self.text, True, self.fgColor)
    rect = self.pos # TODO: Central en el botón
    ctx.screen.blit(text, rect)

class Button(Label):
  def __init__(self, pos, base, height, text, bgColor, fgColor, onClick, *, fromPos = True):
    super().__init__(pos, base, height, text, bgColor, fgColor, fromPos = fromPos)
    self.onClick = onClick

  def tick(self, ctx):
    self._checkClick(ctx)
    super().tick(ctx)

  def _checkClick(self, ctx):
    if self.wasJustClicked(ctx):
      self.onClick(ctx)

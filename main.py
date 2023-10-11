import pygame
from pygame import Vector2

from Context import Context
from Scene import MenuScene

if __name__ == '__main__':
  pygame.init()
  ctx = Context(MenuScene(), Vector2(1280, 720), pygame.font.SysFont('Corbel', 35))
  ctx.play()

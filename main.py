from pygame import Vector2

from Context import Context
from Scene import MainScene

if __name__ == '__main__':
  ctx = Context(MainScene(), Vector2(1280, 720))
  ctx.play()

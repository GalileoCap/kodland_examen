import pygame
from pygame import Vector2

from Object import Object
from Player import Player
from Asteroid import Asteroid
from Control import Label, Button

import utils

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
    self.scores = [
      Label(Vector2(1280/2 - 3*35/2, 720/2 - 1*35), 150, 35, 'FGC - 1000', 'black', 'white'),
      Label(Vector2(1280/2 - 3*35/2, 720/2 - 0*35), 150, 35, 'FGC - 1000', 'black', 'white'),
      Label(Vector2(1280/2 - 3*35/2, 720/2 - -1*35), 150, 35, 'FGC - 1000', 'black', 'white')
    ]
    self.objs += [
      Label(Vector2(1280/2 - 4*35/2, 720/2 - 6*35), 150, 35, 'ASTEROIDS', 'gray', 'white'),
      Button(Vector2(1280/2 - 2*35/2, 720/2 - 5*35), 75, 35, 'Jugar', 'green', 'white', lambda ctx: ctx.setChangeScene(GameScene())),

      Label(Vector2(1280/2 - 3*35/2, 720/2 - 2*35), 150, 35, 'Puntajes', 'black', 'white'),
      *self.scores,

      Button(Vector2(1280/2 - 3*35/2, 720/2 + 3*35), 75, 35, 'Configurar', 'black', 'gray', lambda ctx: ctx.setChangeScene(ConfigScene())),
      Button(Vector2(1280/2 - 35/2, 720/2 + 5*35), 75, 35, 'Salir', 'black', 'gray', lambda ctx: ctx.quit()),
    ]

  def tick(self, ctx):
    for i in range(len(self.scores)):
      self.scores[i].text = utils.fmtScore(ctx.maxScores[i])
    super().tick(ctx)

class ConfigScene(Scene):
  def __init__(self):
    super().__init__()
    self.objs += [
      Label(Vector2(1280/2 - 4*35/2, 720/2 - 6*35), 150, 35, 'ASTEROIDS', 'gray', 'white'),
      Button(Vector2(1280/2 - 3*35/2, 720/2 - 5*35), 75, 35, 'Configurar', 'black', 'white', lambda ctx: ctx.setChangeScene(GameScene())),

      Button(Vector2(1280/2 - 5*35/2, 720/2 - 2*35), 150, 35, 'Cambiar Nombre', 'black', 'white', lambda ctx: ctx.setChangeScene(NameScene())),
      # Label(Vector2(1280/2 - 4*35/2, 720/2 - 2*35), 150, 35, 'TODO: Teclas', 'black', 'white'),

      Button(Vector2(1280/2 - 35/2, 720/2 + 3*35), 75, 35, 'Atrás', 'black', 'gray', lambda ctx: ctx.setChangeScene(MenuScene())),
    ]

class NameScene(Scene):
  def __init__(self):
    super().__init__()
    self.playerName = ''
    self.letters = [
      Label(Vector2(1280/2 - 2*35/2, 720/2), 15, 25, ' ', 'gray', 'white'),
      Label(Vector2(1280/2 - 0*35/2, 720/2), 15, 25, ' ', 'gray', 'white'),
      Label(Vector2(1280/2 - -2*35/2, 720/2), 15, 25, ' ', 'gray', 'white'),
    ]
    self.objs += [
      Label(Vector2(1280/2 - 4*35/2, 720/2 - 6*35), 150, 35, 'ASTEROIDS', 'gray', 'white'),
      Button(Vector2(1280/2 - 3*35/2, 720/2 - 5*35), 75, 35, 'Configurar', 'black', 'white', lambda ctx: ctx.setChangeScene(GameScene())),

      Label(Vector2(1280/2 - 5*35/2, 720/2 - 3*35), 150, 35, 'Tipeá tu nombre (tres letras)', 'black', 'white'),
      Label(Vector2(1280/2 - 5*35/2, 720/2 - 2*35), 150, 35, 'y presioná enter para elegirlo', 'black', 'white'),

      *self.letters,

      Button(Vector2(1280/2 - 35/2, 720/2 + 3*35), 75, 35, 'Atrás', 'black', 'gray', lambda ctx: ctx.setChangeScene(ConfigScene())),
    ]

  def tick(self, ctx):
    super().tick(ctx)
    self._inputName(ctx)

  def draw(self, ctx):
    super().draw(ctx)
    for i in range(len(self.letters)):
      self.letters[i].text = self.playerName[i] if i < len(self.playerName) else ' '

  def _inputName(self, ctx):
    for event in ctx.events:
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_BACKSPACE:
          self.playerName = self.playerName[:-1]
        elif event.key == pygame.K_RETURN and len(self.playerName) == 3:
          ctx.setPlayerName(self.playerName)
        elif len(self.playerName) < 3:
          self.playerName += event.unicode

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
      ctx.saveScore(int(self.player.score))
      ctx.setChangeScene(MenuScene())

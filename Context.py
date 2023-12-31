import pygame
from pygame import Vector2

class Context:
  def __init__(self, startingScene, resolution, font):
    self.resolution = resolution
    self.font = font
    self.scene = startingScene
    self.paused = False
    self._newScene = None

    self.playerName = 'FGC'
    self.maxScores = [('FGC', 60 * 60), ('FGC', 60), ('FGC', 1)]

  def play(self):
    self._start()
    self._gameLoop()
    self._quit()

  def setPlayerName(self, name):
    self.playerName = name

  def saveScore(self, newScore):
    foo = (self.playerName, newScore)
    a, b, c = self.maxScores
    if a[1] < newScore:
      c = b
      b = a
      a = foo
    elif b[1] < newScore:
      c = b
      b = foo
    elif c[1] < newScore:
      c = foo
    self.maxScores = [a, b, c]

  def setChangeScene(self, newScene):
    self._newScene = newScene

  def setPaused(self, pause):
    self.paused = pause

  def quit(self):
    self.running = False

  def _start(self):
    self.screen = pygame.display.set_mode(self.resolution)
    self.clock = pygame.time.Clock()

  def _quit(self):
    pygame.quit()

  def _gameLoop(self):
    self.dt = 0
    self.running = True
    while self.running:
      self._changeScene()
      self._pollEvents()
      if not self.paused:
        self.scene.tick(self)

      self.screen.fill('black') # Limpio la pantalla
      self.scene.draw(self)
      pygame.display.flip() # Dibujo lo nuevo

      self.dt = self.clock.tick(60) / 1000 # Avanzo un tick, limitando el frame rate a 60fps

  def _pollEvents(self):
    self.wasMouseJustReleased = False
    self.wasMouseJustPressed = False

    self.events = pygame.event.get()
    for event in self.events:
      if event.type == pygame.QUIT:
        self.quit()
      elif event.type == pygame.MOUSEBUTTONUP:
        self.wasMouseJustReleased = True
        self.isMousePressed = False
      elif event.type == pygame.MOUSEBUTTONDOWN:
        self.wasMouseJustPressed = True
        self.isMousePressed = True
      elif event.type == pygame.KEYDOWN:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
          self.setPaused(not self.paused)

  def _changeScene(self):
    if self._newScene is not None:
      self.scene = self._newScene
      self._newScene = None

import pygame
from pygame import Vector2

class Context:
  def __init__(self, startingScene, resolution, font):
    self.resolution = resolution
    self.font = font
    self.scene = startingScene
    self.paused = False

  def play(self):
    self._start()
    self._gameLoop()
    self._quit()

  def setPaused(self, pause):
    self.paused = pause

  def _start(self):
    self.screen = pygame.display.set_mode(self.resolution)
    self.clock = pygame.time.Clock()

  def _quit(self):
    pygame.quit()

  def _gameLoop(self):
    self.dt = 0
    self.running = True
    while self.running:
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
        self.running = False
      elif event.type == pygame.MOUSEBUTTONUP:
        self.wasMouseJustReleased = True
        self.isMousePressed = False
      elif event.type == pygame.MOUSEBUTTONDOWN:
        self.wasMouseJustPressed = True
        self.isMousePressed = True

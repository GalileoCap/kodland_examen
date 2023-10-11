import pygame
from pygame import Vector2

class Context:
  def __init__(self, startingScene, resolution):
    self.resolution = resolution
    self.scene = startingScene

  def play(self):
    self._start()
    self._gameLoop()
    self._quit()

  def _start(self):
    pygame.init()
    self.screen = pygame.display.set_mode(self.resolution)
    self.clock = pygame.time.Clock()

  def _quit(self):
    pygame.quit()

  def _gameLoop(self):
    self.dt = 0
    self.running = True
    while self.running:
      self._pollEvents()

      self.screen.fill('black') # Limpio la pantalla
      self.scene.tick(self)
      pygame.display.flip() # Dibujo lo nuevo

      self.dt = self.clock.tick(60) / 1000 # Avanzo un tick, limitando el frame rate a 60fps

  def _pollEvents(self):
    self.events = pygame.event.get()
    for event in self.events:
      if event.type == pygame.QUIT:
        self.running = False
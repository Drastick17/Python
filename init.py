import pygame as pg
import sys

from Vistas.Views import Views

#BACKGROUND = pg.image.load("starry_night.jpg").convert()
class Main():
  def __init__(self, width, height,):
    self.width = width;
    self.height = height;
    self.screen = pg.display.set_mode((self.width,self.height))
    self.surface = pg.Surface((self.width, self.height))
    #instances
    self.views = Views(self)
    
  def Run(self):
    pg.init()
    pg.display.set_caption("Tres En Raya")
    self.views.StartView() 
      #!!pg.draw.rect(self.surface,(255,255,255),(0, 0, 250, 50), 0)
      #!!self.screen.blit(self.surface,(0,0))


if __name__ == '__main__':
  game = Main(300, 300)
  game.Run()
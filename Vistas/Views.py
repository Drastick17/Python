from pydoc import cli
import pygame as pg
import numpy as np
import sys

from Compontes.Button import Button 
from Compontes.Board import Board

class Views():
  def __init__(self, window):
    self.screen = window.screen
    self.marks = []
    self.Board = Board(self, self.marks)
    self.GameOver = False
  
  def GameView(self):
    click = False
    self.screen.fill((0,255,255))
    #Define game variables
    player = 1
    #Define Board Marks
    

    #Fill Board
    for x in range(3):
      row = [0]*3
      self.marks.append(row)


   
    while True:
      for event in pg.event.get():
        self.Board.DrawLines()
        #Handle events
        if event.type == pg.QUIT:
          pg.quit()
          sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN and click==False:
          click = True   
        #Quit click = true
        if(event.type == pg.MOUSEBUTTONUP and click):
          click = False
          pos = pg.mouse.get_pos()
          cellX = pos[0]
          cellY = pos[1]
          if(self.marks[cellX // 100][cellY // 100] == 0):
            #get Position of clicked cell
            self.marks[cellX // 100][cellY // 100] = player
            #Draw mark
            self.Board.DrawMarks()
            #Switch player
            player *= -1
          print(self.marks,self.marks)
          if(len(self.Board.winner) > 0 ):
            self.GameOver = True
            print(self.GameOver)
            
    
          
      pg.display.update()
  
  def StartView(self):
    PLAY_BUTTON = Button(self)
    PLAY_BUTTON.draw("Play",100,125,46)
    while True:
      for event in pg.event.get():
        PLAY_BUTTON.isClicked(pg.mouse)
        if event.type == pg.QUIT:
          pg.quit()
          sys.exit()
        if(PLAY_BUTTON.clicked):
          self.GameView()
      
      pg.display.update()
      
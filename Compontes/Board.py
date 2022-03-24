from calendar import c
from pygame import draw
class Board():

  def __init__(self, window, marks):
    self.screen = window.screen
    self.marks = marks
    self.red = (255,0,0)
    self.green = (0,255, 0)
    self.winner = {}

  def DrawLines(self):
    lineColor = (255,255,255)
    for i in range(1,3):
        draw.line(self.screen,lineColor,(0,100*i),(300,100*i),10)
        draw.line(self.screen,lineColor,(100*i,0),(100*i,300),10)
  
  def DrawMarks(self):
    posX = 0
    for x in self.marks:
      posY = 0;
      for y in x:
        if(y == 1):
          draw.line(self.screen, self.red, (posX * 100 + 15, posY * 100 + 15), (posX * 100 + 85, posY * 100 + 85), 10)
          draw.line(self.screen, self.red, (posX * 100 + 85, posY * 100 + 15), (posX * 100 + 15, posY * 100 + 85), 10)
        if(y == -1):
          draw.circle(self.screen, self.green, (posX * 100 + 50, posY * 100 + 50), 38, 10)
        posY += 1
      posX += 1	  
    
  def CheckWinner(self):
    for x in self.marks:
      if(sum(x) == 3):
        self.winner['winner'] = "player1"
      if(sum(x) == 3):
        self.winner['winner'] = "player2"
      


      

      
      

      
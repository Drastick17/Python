from pygame import draw
class Board():
  lineColor = (74,163,146)
  def __init__(self, window, marks, gameOver, turno ):
    self.screen = window.screen
    self.turno = turno
    self.marks = marks
    self.gameOver = gameOver
    self.red = (84,84,84)
    self.green = (242,235,211)


  def DrawLines(self):
    for i in range(1,3):
        draw.line(self.screen,self.lineColor,(10,100*i),(290,100*i),8)
        draw.line(self.screen,self.lineColor,(100*i,10),(100*i,290),8)
  
  def DrawMarks(self):
    posX = 0
    for x in self.marks:
      posY = 0;
      for y in x:
        if(y == 1):
          draw.line(self.screen, self.red, (posX * 100 + 15, posY * 100 + 15), (posX * 100 + 85, posY * 100 + 85), 10)
          draw.line(self.screen, self.red, (posX * 100 + 85, posY * 100 + 15), (posX * 100 + 15, posY * 100 + 85), 10)
        if(y == -1):
          draw.circle(self.screen, self.green, (posX * 100 + 50, posY * 100 + 50), 40, 8)
        posY += 1
      posX += 1	  
    
  def CheckWinner(self):
    posY = 0
    count = 0
    for row in self.marks:
      if(sum(row) == 3):
        self.gameOver= True
        break;
      if(self.marks[0][posY] + self.marks[1][posY]+self.marks[2][posY] == 3):
        self.gameOver= True
        break;
      posY+=1

    if (self.marks[0][0] + self.marks[1][1] + self.marks [2][2] == 3) or (self.marks[2][0] + self.marks[1][1] + self.marks [0][2] == 3):
      self.gameOver= True
          
    if (self.marks[0][0] + self.marks[1][1] + self.marks[2][2] == -3) or (self.marks[2][0] + self.marks[1][1] + self.marks[0][2] == -3):
      self.gameOver= True
    
      
      


      

      
      

      
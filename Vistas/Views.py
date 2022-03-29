import pygame as pg
import sys

from Compontes.Button import Button 
from Compontes.Board import Board

class Views():
  bgcolor = (88,191,173)
  def __init__(self, window):
    self.screen = window.screen
  
  def GameView(self):
    self.marks = []
    self.gameOver = False
    self.winner= None
    self.turno = 0;
    click = False
    
    self.Board = Board(self, self.marks, self.gameOver, self.turno)
    self.screen.fill(self.bgcolor)
    #Define game variables
    self.player = 1
    #si turno = 1 (X) player = 1 
    #si turno = 2 (O) player = -1

    #Fill Board
    for x in range(3):
      row = [0]*3
      self.marks.append(row)
      #[[1,0,0]]
      #[[0,-1,0]]
      #[[0,0,0]]

    while True:
      for event in pg.event.get():
        self.Board.DrawLines()
        self.drawTurno()
        print(self.marks)
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
          cellX = pos[0] # x
          cellY = pos[1] # y
          if(self.marks[cellX // 100][cellY // 100] == 0):
            #get Position of clicked cell
            self.marks[cellX // 100][cellY // 100] = self.player
            #Draw mark
            self.Board.DrawMarks()
            #Switch player
            self.player *= -1
            self.turno += 1
            self.Board.CheckWinner()
            
          
          
          if(self.Board.gameOver):
            self.TryAgayn()
          if(self.Board.gameOver == False and self.turno == 9):
            self.Empate()
       
      pg.display.update()
  
  def drawTurno(self):
    self.text = ""
    if(self.turno%2 == 0):
     self.text="X"
    else:
      self.text="O"
    pg.display.set_caption(f"Turno de {self.text}")

  def Empate(self):
    TRY_AGAIN = Button(self)
    TRY_AGAIN.draw("Try Again",80,140,42,(242,235,211),(54,54,54))
    SALIR = Button(self)
    SALIR.draw("QUIT", 80, 190, 42,(242,235,211),(54,54,54))

    empateText = "Empate"
    font = pg.font.SysFont('None', 35)
    renderText = font.render(empateText,True,(35,35,35))
    pg.draw.rect(self.screen,(255,255,255),(0,45,300, renderText.get_height()+10))
    self.screen.blit(renderText,(int(300 / 2) - int(renderText.get_width() / 2),50)) 

    while True:
      for event in pg.event.get():
        TRY_AGAIN.isClicked(pg.mouse)
        SALIR.isClicked(pg.mouse)
        if event.type == pg.QUIT:
          pg.quit()
          sys.exit()
        
        if(TRY_AGAIN.clicked):
          self.GameView()
        if(SALIR.clicked):
          pg.quit()
          sys.exit()


      pg.display.update()  
    
  def TryAgayn(self):
    TRY_AGAIN = Button(self)
    TRY_AGAIN.draw("Try Again",80,140,42,(242,235,211),(54,54,54))
    SALIR = Button(self)
    SALIR.draw("QUIT", 80, 190, 42,(242,235,211),(54,54,54))
    winnerText = f"El ganador es {self.text}"
    font = pg.font.SysFont('None', 35)
    renderText = font.render(winnerText,True,(35,35,35))
    pg.draw.rect(self.screen,(255,255,255),(0,45,300, renderText.get_height()+10))
    self.screen.blit(renderText,(int(300 / 2) - int(renderText.get_width() / 2),50)) 

    while True:
      for event in pg.event.get():
        TRY_AGAIN.isClicked(pg.mouse)
        SALIR.isClicked(pg.mouse)
        if event.type == pg.QUIT:
          pg.quit()
          sys.exit()
        
        if(TRY_AGAIN.clicked):
          self.GameView()
        if(SALIR.clicked):
          pg.quit()
          sys.exit()

      pg.display.update()

  def StartView(self):
    background = pg.image.load("/Users/dannysolano/Desktop/PROYECTS_APPS/curso_de_Python/Juego/media/background.webp")
    self.screen.blit(background,(0,0))
    font = pg.font.SysFont('None', 40)
    renderText = font.render("TRES EN RAYA",True,(90,90,90),)
    pg.draw.rect(self.screen,(255,255,255),(0,45,300, renderText.get_height()+10))
    self.screen.blit(renderText,(int(300 / 2) - int(renderText.get_width() / 2),50)) 
    PLAY_BUTTON = Button(self)
    PLAY_BUTTON.draw("Play",110,125,46,(54,54,54),(255,255,255))
    while True:
      for event in pg.event.get():
        PLAY_BUTTON.isClicked(pg.mouse)
        if event.type == pg.QUIT:
          pg.quit()
          sys.exit()
        if(PLAY_BUTTON.clicked):
          self.GameView()
      
      pg.display.update()
      
from pygame import draw, Rect, font


class Button():
  def __init__(self, window):
     self.screen = window.screen
     self.clicked = False

  def draw(self,text, x, y, size, color = (0,0,0), bg = (255,0,255)):
    self.x = x
    self.y = y
    self.text = text
    self.size = size
    self.color = color
    self.bg = bg
    self.font = font.SysFont('None', size)

    self.renderText()
    self.width = self.textImg.get_width()+10
    self.height = self.textImg.get_height()+10
    self.btnRect = Rect(self.x, self.y,self.width , self.height)
    draw.rect(self.screen, self.bg, self.btnRect,0,5)
    self.screen.blit(self.textImg,(self.x + int(self.width / 2) - int(self.textImg.get_width() / 2), (self.y + int(self.height / 2) - int(self.textImg.get_height()) / 2) ))
    
  

  def isClicked(self, mouse):
    mousePos = mouse.get_pos()

    if self.btnRect.collidepoint(mousePos):
      if(mouse.get_pressed()[0]):
        self.clicked = True
      elif mouse.get_pressed()[0] == False and self.clicked:
        self.clicked = False
      else:
        pass

  def renderText(self):
    self.textImg = self.font.render(self.text,True,self.color)

  
    
    

 
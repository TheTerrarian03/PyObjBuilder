import pygame
import constants as consts
import functions as fcs


class WxH:
    # (4, 5) Or 4, 5
    def __init__(self, *args):
        if (len(args) == 1):
            if (isinstance(args[0], tuple)) or (isinstance(args[0], list)):
                if (len(args[0]) == 2):
                    self.x = args[0][0]
                    self.y = args[0][1]
        
        elif (len(args) == 2):
            if(isinstance(args[0], int) and isinstance(args[1], int)):
                self.x = args[0]
                self.y = args[1]
        
        else:
            self.x = 0
            self.y = 0
    
    def get(self) -> tuple[int, int]:
        return (self.x, self.y)

class Window:
    def __init__(self, sizeWxH, title="New Window"):
        self.sizeWxH = sizeWxH
        self.screen = pygame.display.set_mode(sizeWxH, pygame.RESIZABLE)
        pygame.display.set_caption(title)
        self.frames = []
        
    def getWxH(self) -> tuple[int, int]:
        return (0, 0)
    
    def getWidth(self) -> int:
        return pygame.display.get_surface().get_size()[0]

    def getHeight(self):
        pass
        
    def addFrame(self, frame):
        self.frames.append(frame)
    
    def update(self):
        pygame.draw.rect(self.screen, consts.COLORS.DARKMODE.BG, (0, 0, self.sizeWxH[0], self.sizeWxH[1]))
        
        for frame in self.frames:
            pygame.draw.rect(self.screen, consts.COLORS.DARKMODE.HIGHLIGHT, (frame.pos[0], frame.pos[1], frame.size[0], frame.size[1]), 3)
        
    def updateSurface(self):
        pygame.display.update()

class Border:
    def __init__(self, direction: str, position: int):
        self.direction = direction
        self.position = position
        self.rectPos = None
        
    def update(self):
        pass
    
    def updateMouseCursor(self):
        if self.direction == "x":
            pass

class Frame:
    def __init__(self, sizeWxH, posXY, doesSnap=True, name="Frame"):
        self.size = sizeWxH
        self.pos = posXY
        self.snap = doesSnap
        self.name = name
    
    def processMouseCursor(self):
        # block for changing the cursor for moving and resizing the frame
        mousePos = pygame.mouse.get_pos()
        isNear = fcs.getApproxMousePos(self.size, self.pos, mousePos, error=5)
        print(isNear)
        if (isNear in ["T", "B"]):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZENS)
        elif (isNear in ["L", "R"]):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZEWE)
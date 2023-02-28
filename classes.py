import pygame
import constants as consts
import functions as fcs


class Window:
    def __init__(self, sizeWxH, title="New Window"):
        self.sizeWxH = sizeWxH
        self.screen = pygame.display.set_mode(sizeWxH)
        pygame.display.set_caption(title)
        self.frames = []
        
    def addFrame(self, frame):
        self.frames.append(frame)
    
    def update(self):
        pygame.draw.rect(self.screen, consts.COLORS.DARKMODE.BG, (0, 0, self.sizeWxH[0], self.sizeWxH[1]))
        
        for frame in self.frames:
            pygame.draw.rect(self.screen, consts.COLORS.DARKMODE.HIGHLIGHT, (frame.pos[0], frame.pos[1], frame.size[0], frame.size[1]), 3)
        
    def updateSurface(self):
        pygame.display.update()

class Frame:
    def __init__(self, sizeWxH, posXY, doesSnap=True, name="Frame"):
        self.size = sizeWxH
        self.pos = posXY
        self.snap = doesSnap
        self.name = name
    
    def checkMouse(self):
        mousePos = pygame.mouse.get_pos()
        isNear = fcs.getApproxMousePos(self.size, self.pos, mousePos, error=5)
        print(isNear)
        if (isNear in ["T", "B"]):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZENS)
        elif (isNear in ["L", "R"]):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZEWE)
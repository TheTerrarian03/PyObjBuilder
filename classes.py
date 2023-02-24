import pygame
import constants as consts


class Window:
    def __init__(self, sizeWxH, title="New Window"):
        self.sizeWxH = sizeWxH
        self.screen = pygame.display.set_mode(sizeWxH)
        pygame.display.set_caption(title)
    
    def update(self):
        pygame.draw.rect(self.screen, consts.COLORS.DARKMODE.BG, (0, 0, self.sizeWxH[0], self.sizeWxH[1]))
        
    def updateSurface(self):
        pygame.display.flip()
    
    def processInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
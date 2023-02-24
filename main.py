import pygame
import classes as cls
import functions as fcs


running = True

clock = pygame.time.Clock()
window = cls.Window((400, 300), "Py Obj Builder")

while running:
    window.update()
    
    window.updateSurface()
    clock.tick(60)
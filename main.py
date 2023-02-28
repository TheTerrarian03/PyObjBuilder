import pygame
import classes as cls
import functions as fcs


def main():
    pygame.init()
    running = True

    clock = pygame.time.Clock()
    window = cls.Window((400, 300), "Py Obj Builder")
    frame1 = cls.Frame((50, 50), (25, 25), name="AAAAA")
    
    window.addFrame(frame1)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        window.update()
        
        window.updateSurface()
        frame1.checkMouse()
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()
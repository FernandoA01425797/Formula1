from pygame import *
import sys


init()
screen = display.set_mode((800,600))
fondo = image.load("Logo de F1.png")
fondo = transform.scale(fondo, (800,600))

while True:
    
    for e in event.get():
        if e.type == QUIT: sys.exit()
    screen.blit(fondo, (0,0))
    draw.rect(screen, (225,0,0), (290,400,180,88), 0)
    draw.rect(screen, (225,225,225), (290,400,180,88), 1)
    draw.rect(screen, (225,225,225), (290,400,180,88), 1)
    display.flip()

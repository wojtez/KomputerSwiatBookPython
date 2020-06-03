import pygame
import random
import os

pygame.init()
szer_okna = 600
wys_okna = 600
screen = pygame.display.set_mode((szer_okna, wys_okna))

class Biedronka():
    def __init__(self):
        #nadawanie przypadkowych wartości ruchu po osi x i y
        self.x = random.randint(250, 500)
        self.y = random.randint(250, 500)
        #nadawanie przypadkowych wartości prędkości po osi x i y
        self.vx = random.randint(-4, 4)
        self.vx = random.randint(-4, 4)
        self.grafika = pygame.image.load(os.path.join('biedronka.png'))
        self.wielkosc = 20

    def rysuj(self):
        # wstawiamy obiekt na ekanie aplikacji
        screen.blit(self.grafika, (self.x, self.y))
        
    def ruch(self):
        #wprawiamy obiekt w ruch, po osiach x, y
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        # odbijamy obiekt od ścian programu
        if self.x <= 0 or self.x >= szer_okna - self.wielkosc:
            self.vx = self.vx * -1
        if self.vy <= 0 or self.y >= szer_okna - self.wielkosc:
            self.vy = self.vy * -1
            
    #def kolizja(self):
        # zdezenie biedronki z naszym obiektem
     
        
        


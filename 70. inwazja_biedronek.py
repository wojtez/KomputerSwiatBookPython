# Program inwazja biedronek mający na celu zaznajomienie z modułem pygame

import pygame, random, os

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
        self.vy = random.randint(-4, 4)
        self.grafika = pygame.image.load(os.path.join('source/biedronka.png'))
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
            
    def kolizja(self, player):
        # zdezenie biedronki z naszym obiektem
        #wyznaczenie srodka biedronki
        x_srodek = self.x + self.wielkosc/2
        y_srodek = self.y + self.wielkosc/2
        #warunek jeżeli będzie zderzenie
        if player.collidepoint(x_srodek, y_srodek):
            czcionka = pygame.font.SysFont("Gorgia", 20)
            napis = czcionka.render("KONIEC GRY", 1, (123, 213, 231))
            screen.blit(napis, (100, 130))
            #zmienna o charakterze globalnym pozwalajaca na zatrzymanie gry 
            #z poziomu metody
            global gramy
            gramy = False
            
# tworzymy biedronki 1 zaleznosci od ilosci tutaj 10
przeciwnicy = []
for i in range(10):
    przeciwnicy.append(Biedronka())



#tworzymy system punktowy
punkty = 0
#zmienna globalna
gramy = True
#wstawiamy wspolrzedne poczatkowe gracza oraz predkosc poruszania
x_gracz = 300
y_gracz = 300
v = 20
#tworzymy gracza
gracz = pygame.Rect(x_gracz, y_gracz, 20, 20)
#pętla główna gry
while True:
    #sprawdzanie przy każym evencie programu
    for event in pygame.event.get():
        #sprawdza czy nie zostal klikniety x zeby wyjsc z programu
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        #sprawdza ruch gracza gora/dol, prawo/lewo
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_UP:
                if y_gracz - v > 0:
                    y_gracz = y_gracz - v    
            if event.type == pygame.K_DOWN:
                if y_gracz + v < wys_okna - 20:
                    y_gracz = y_gracz + v    
            if event.type == pygame.K_RIGHT:
                if x_gracz + v < szer_okna - 20:
                    x_gracz = x_gracz + v    
            if event.type == pygame.K_LEFT:
                if x_gracz - v > 0:
                    x_gracz = y_gracz - v
            #twrzenie gracza ponownie z nowymi współrzędnymi
            gracz = pygame.Rect(x_gracz, y_gracz, 20, 20)    
    
    #wprowadzamy biedronki w ruch    
    if gramy == True:
        punkty = punkty + 1
        screen.fill((50, 50, 100))
        #kazda z listy 10ciu biedronek wprowadzamy w ruch
        for biedroneczka in przeciwnicy:
            biedroneczka.ruch()
            biedroneczka.rysuj()
            biedroneczka.kolizja(gracz)
        #wstawiamy informacje o punktach
        czcionka = pygame.font.SysFont("Georgia", 20)
        napis = czcionka.render(str(punkty), 1, (123, 213, 231))
        screen.blit(napis, (30, 30))
        #wstawamy reprezentacje gracza
        pygame.draw.rect(screen, (0, 30, 0), gracz, 0)
        #uaktualniamy obraz
        pygame.display.update()
        #zwalniamy ruch biedronek
        pygame.time.wait(10)
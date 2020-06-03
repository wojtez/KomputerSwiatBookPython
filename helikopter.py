# Gra helikopter mająca za zadanie unianie zdeżenia ze ścianami jaskini
# oraz liczenie pónktów 

import pygame , os, random, math

# inicjalizacja pakietu
pygame.init()

# wymiary okna i jego wywołanie
szer = 600
wys = 600
screen = pygame.display.set_mode((szer, wys))

# procedura wstawania napisu


def napisz(tekst, x, y, rozmiar):
    # przypisanie odpowiedniej czcionki
    cz = pygame.font.SysFont("Courier New", rozmiar)
    # renderowanie napisu(tekst, czy jest czy nie, kolor RGB)
    rend = cz.render(tekst, 1, (255, 100, 100))
    # opcjonalnie można użyć poniższych wzorów do wyśrodkowania napisu
    # x = (szer - rend.get_rect().width)/2
    # y = (wys - rend.get_rect().height)/2
    screen.blit(rend, (x, y))


copokazuje = "menu"


class Przeszkoda():
    """ towrzenie przeszkód """

    def __init__(self, x, szerokosc):
        self.x = x
        self.szerokosc = szerokosc
        self.y_gora = 0
        self.wys_gora = random.randint(150, 250)
        self.odstep = 300
        self.y_dol = self.wys_gora + self.odstep
        self.wys_dol = wys - self.y_dol
        self.kolor = (160, 140, 190)
        self.ksztalt_gora = pygame.Rect(
            self.x, self.y_gora, self.szerokosc, self.wys_gora)
        self.ksztalt_dol = pygame.Rect(
            self.x, self.y_dol, self.szerokosc, self.wys_dol)
    # rysowanie przeszkód

    def rysuj(self):
        pygame.draw.rect(screen, self.kolor, self.ksztalt_gora, 0)
        pygame.draw.rect(screen, self.kolor, self.ksztalt_dol, 0)
    # wprawianie przeszkod w ruch

    def ruch(self, v):
        self.x = self.x - v
        self.ksztalt_gora = pygame.Rect(
            self.x, self.y_gora, self.szerokosc, self.wys_gora)
        self.ksztalt_dol = pygame.Rect(
            self.x, self.y_dol, self.szerokosc, self.wys_dol)
    # dodanie kolizji

    def kolizja(self, player):
        if self.ksztalt_gora.colliderect(player) or self.ksztalt_dol.colliderect(player):
            return True
        else:
            return False


class Helikopter():
    """ Tworzenie Helikoptera"""

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.szerokosc = 30
        self.wysokosc = 55
        self.ksztalt = pygame.Rect(
            self.x, self.y, self.szerokosc, self.wysokosc)
        self.grafika = pygame.image.load(os.path.join('helicopterSmall.png'))
    # rysujemy helikopter

    def rysuj(self):
        screen.blit(self.grafika, (self.x, self.y))
    # wprawiamy helikopter w ruch

    def ruch(self, v):
        self.y = self.y + v
        self.ksztalt = pygame.Rect(
            self.x, self.y, self.szerokosc, self.wysokosc)


# tworzenie obiektu przeszkody
przeszkody = []
# 21 poniewaz tylko 20 prostokatow moze sie zmiescic w oknie programu
for i in range(21):
    # podajemy szerokosc/20 poniewaz na ekranie jest tylko 20 prostokatow
    przeszkody.append(Przeszkoda(i*szer/20, szer/20))

# tworzenie obiektu helikoptera
gracz = Helikopter(250, 275)

# tworzenie zmiennej kierunku w ktorym bedzie sie poruszac helikopter
dy = 0

# *******************   pętla główna gry   **********************

while True:
    for event in pygame.event.get():
        # warunek zamknięcia okna programu przyciskiem x
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        # warunek wywołania ruchu obiektu helikopter
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                dy = -1
            if event.key == pygame.K_DOWN:
                dy = 1
            # warunek przejścia z menu do gry
            if event.key == pygame.K_SPACE:
                if copokazuje != "rozgrywka":
                    gracz = Helikopter(250, 275)
                    dy = 0
                    copokazuje = "rozgrywka"
                    punkty = 0
    # oczyszczanie okna gry
    screen.fill((0, 0, 0))
    # dodanie dodatkowego ekranu w zależnosci od wyswietlanej treści
    if copokazuje == "menu":
        napisz("Hit SPACE to start playing.", 80, 150, 25)
        # wczytanie grafiki
        grafika = pygame.image.load(os.path.join('logo2.png'))
        screen.blit(grafika, (80, 30))
    elif copokazuje == "rozgrywka":
        for p in przeszkody:
            # wprawiamy preszkode w ruch i przezsuwamy o 1 piksel
            p.ruch(1)
            p.rysuj()
            # wywolanie metody kolizja i zakonczenie jezeli wartosc True
            if p.kolizja(gracz.ksztalt):
                copokazuje = "koniec"
        # nadpisywanie kolejnych przeszkod w miejsce tych ktore sie przesunely
        for p in przeszkody:
            if p.x <= -p.szerokosc:
                # usuwamy przeszkode
                przeszkody.remove(p)
                # dodajemy nową przeszkode
                przeszkody.append((Przeszkoda(szer, szer/20)))
                # dodajemy punkt za kazdym razem jak przesuwa się przeszkoda
                punkty = punkty + math.fabs(dy)
        # wywołanie metod dla gracza
        gracz.rysuj()
        gracz.ruch(dy)
        napisz(str(punkty), 50, 50, 20)
    elif copokazuje == "koniec":
        grafika = pygame.image.load(os.path.join('logo2.png'))
        screen.blit(grafika, (80, 30))
        napisz("YOU HAVE LOST... !!!", 50, 290, 20)
        napisz("Hit SPACE to start playing.", 50, 350, 20)
        napisz("Your Score: " + str(punkty), 50, 320, 20)

    pygame.display.update()

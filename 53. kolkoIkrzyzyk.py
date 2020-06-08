# Program wykorzystjący moduł turtle do tworzenia popularnej gry kółko i krzyżyk

from turtle import *
import math

# definiujemy bok kwadratu
bok = 80
pole = [[False, False, False], [False, False, False], [False, False, False]]


# rysowanie pola do gry za pomocą kwadratu
def kwadrat():
    for i in range(4):
        fd(bok)
        left(90)

# rysowanie pól do gry w tabeli 3x3
def plansza():
    # rysowanie kwadratow w wierszach
    for i in range(3):
        # rysowanie 3 wadratow w kazdym wierszu
        for j in range(3):
            # zawieszenie rysowania po istniejącej linii
            pd()
            # wywołanie procedury
            kwadrat()
            # wznowienie rysowania po pustej linii
            pu()
            fd(bok)
        # przesuwamy kursor do drugiej linii
        bk(3*bok)
        left(90)
        fd(bok)
        right(90)

# tworzenie krzyżyka
def krzyzyk(a, b):  # a = kolumna, b = wiersz
    pu()
    # przesmieszczanie żółwia
    setx(a * bok + bok/2)
    sety(b * bok + bok/2)
    pd()
    left(45)
    for i in range(4):
        fd(bok/4)
        bk(bok/4)
        left(90)
    right(45)
    pu()

# tworzenie kolka
def kolko(a, b):
    pu()
    setx(a * bok + bok/2)
    # wyliczamy ze wzoru na promień kola (2*pi*r)
    # zakladamy ze kolo powstanie z 36 linii
    # każda po 3 kroki żółwia i przesunieta o 10 stopni
    # co daje nam 108 (36*6) i finalnie do wzoru wstawiamy 54/pi
    sety(b * bok + bok/2 - 54/math.pi)
    # opcjonalnie można wykorzstać wbudowaną funkcję
    # sety(circle(50))
    pd()
    for i in range(36):
        fd(3)
        left(10)


czyj_ruch = "x"

# sprawdzanie czyj ruch jest nastepny
def postaw(a, b):
    global czyj_ruch
    global pole
    #dodanie tablicy pozwala zablokowac wstawianie x lub o w to samo miejsce
    if pole [a] [b] == False:
        pole [a] [b] = True
        if czyj_ruch == "x":
            krzyzyk(a, b)
            czyj_ruch = "0"
        elif czyj_ruch == "0":
            kolko(a, b)
            czyj_ruch = "x"

# uruchomienie rysowania planszy
plansza()
postaw(1, 2)
postaw(0, 1)
postaw(1, 2)
postaw(1, 2)
postaw(1, 2)
postaw(1, 2)
postaw(1, 2)
postaw(1, 2)
postaw(1, 2)
postaw(0, 2)
postaw(1, 0)
postaw(2, 2)



input("Push enter button to finnish game.")

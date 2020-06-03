from turtle import *
import math


#definiujemy bok kwadratu
bok = 80

#rysowanie pola do gry za pomocą kwadratu
def kwadrat():
    for i in range (4):
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

#tworzenie krzyżyka
def krzyzyk(a, b):  # a = kolumna, b = wiersz
    pu()
    #przesmieszczanie żółwia
    setx(a * bok + bok/2)
    sety(b * bok + bok/2)
    pd()
    left(45)
    for i in range (4):
        fd(bok/4)
        bk(bok/4)
        left(90)
    right(45)
    pu()
        
#tworzenie kolka
def kolko(a, b):
    pu()
    setx(a * bok + bok/2)
    #wyliczamy ze wzoru na promień kola (2*pi*r)
        # zakladamy ze kolo powstanie z 36 linii 
        # każda po 3 kroki żółwia i przesunieta o 10 stopni
        # co daje nam 108 (36*6) i finalnie do wzoru wstawiamy 54/pi
    sety(b * bok + bok/2 - 54/math.pi)
    #opcjonalnie można wykorzstać wbudowaną funkcję
    #sety(circle(50))
    pd()
    for i in range(36):
        fd(3)
        left(10)
    
plansza()

kolko(1, 1)
krzyzyk(0, 2)
kolko(1, 2)
krzyzyk(1, 0)
kolko(2, 1)
krzyzyk(0, 1)
kolko(0, 0)
krzyzyk(2, 2)
kolko(2, 0)

input("Push enter button to finnish game.")
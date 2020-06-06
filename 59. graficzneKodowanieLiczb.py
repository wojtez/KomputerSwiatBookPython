from turtle import *

bok = 80
# definicja rysowania kwadratu
def kwadrat(kolor):
    begin_fill()
    fillcolor(kolor)
    for i in range (4):
        fd(bok)
        left(90)
    end_fill()

#definicja rysowania słupka
def slupek(k1, k2, k3):
    #rysowanie kwadratu w kolorze k1
    pd()
    kwadrat(k1)
    pu()
    #ustawianie żółwia w odp. pozycji i kierunku
    left(90)
    fd(bok)
    right(90)
    #rysowanie kwadratu w kolorze k1
    pd()
    kwadrat(k2)
    pu()
    #ustawianie żółwia w odp. pozycji i kierunku
    left(90)
    fd(bok)
    right(90)
    #rysowanie kwadratu w kolorze k1
    pd()
    kwadrat(k3)
    pu()
    #ustawianie żółwia w odp. pozycji i kierunku
    left(90)
    fd(bok)
    right(90)

#procedura sumowania liczby - procedura bo zwraca zmienną
def sumuj(liczba):
    if liczba > 99 and liczba < 1000:
        #reszta z dzielenia liczby przez 10 daje nam ostatnią liczbę
        jednosci = liczba%10
        liczba = (liczba - liczba%10) / 10
        dziesiatki = liczba%10
        liczba = (liczba - liczba%10) / 10
        setki = liczba
    return jednosci + dziesiatki + setki
   
#porcedura kodowania jednego slupka
def koduj_slupek(liczba):
    if sumuj(liczba) >= 1 and sumuj(liczba) <= 5:
        slupek("blue", "blue", "green")
    if sumuj(liczba) >= 6 and sumuj(liczba) <= 10:
        slupek("blue", "green", "green")
    if sumuj(liczba) >= 11 and sumuj(liczba) <= 15:
        slupek("green", "green", "green")
    if sumuj(liczba) >= 16 and sumuj(liczba) <= 20:
        slupek("green", "green", "blue")
    if sumuj(liczba) >= 21 and sumuj(liczba) <= 25:
        slupek("green", "blue", "blue")
    if sumuj(liczba) >= 26 and sumuj(liczba) <= 27:
        slupek("blue", "blue", "blue")       
        
#rsowanie calego rysunku 3x3
def zakoduj(a, b, c):
    #rysowanie 1-go slupka
    koduj_slupek(a)
    fd(bok)
    #przechodzenie do pozycji rysowania 2-go slupka
    right(90)
    fd(bok*3)
    left(90)
    #rysowanie 2-go słupka
    koduj_slupek(b)
    fd(bok)
    #przechodzenie do pozycji rysowania 3-go slupka
    right(90)
    fd(bok*3)
    left(90)
    #rysowanie 3-go słupka
    koduj_slupek(c)
    
        
#testowanie programu
zakoduj(888, 111, 110)
input()
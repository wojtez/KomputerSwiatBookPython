# Gra losowa mająca za zadanie poprawny wybór jednego z przycików losowo wybieranego przez komputer

from tkinter import *
import random 


okno_gry = Tk()
okno_gry.title("Wybierz przycisk")
okno_gry.geometry("300x350")
przyciski = []
etykieta = str


def wstaw_przyciski():
    ile_przyciskow = 8
    dobry = random.randint(0, ile_przyciskow-1)
    for i in range(ile_przyciskow):
        if i == dobry:
            przyciski.append(Button(okno_gry, text = "kliknij mnie", command = trafiony))
        else:
            przyciski.append(Button(okno_gry, text = "kliknij mnie", command = pudlo))
    
    for i in przyciski:
        i.pack(fill=BOTH, expand=YES)

def trafiony():
    for i in przyciski:
        i.destroy()
    etykieta = Label(okno_gry, text="Trafiles dobry przycisk")
    etykieta.pack(fill=BOTH, expand=YES)
    okno_gry.after(5000, restart)

def restart():
    etykieta.destroy()
    wstaw_przyciski()

def pudlo():
    for i in przyciski:
        i.destroy()
    etykieta = Label(okno_gry, text="Trafiles zly przycisk")
    etykieta.pack(fill=BOTH, expand=YES)
    okno_gry.after(5000, restart)


wstaw_przyciski()    

import json, os
from random import sample

class Carte:

    def __init__(self, c, n):
        self.couleur = c
        self.numero = n

    def __repr__(self):
        return f"{self.couleur} {self.numero}"


class Table:

    def __init__(self, c):
        self.carte = c

    def __repr__(self):
        return self.carte


class Main:

    def __init__(self, lc: list[Carte]):
        self.main = lc

    def __repr__(self):
        return self.main

class Jeu:

    def __init__(self, m: Main, t: Table):
        self.table = t
        self.main = m

    def cartes_posables(self) -> list[Carte]:
        rendu = []
        for c in self.main.main:
            if c.numero == self.table.carte.numero or c.couleur == self.table.carte.couleur:
                rendu.append(c)
        return rendu

j = Jeu(Main([
    Carte(5, "rouge"),
    Carte(6, "bleu"),
    Carte(6, "noir"),
    Carte(3, "noir"),
]) ,Table(Carte(6, "rouge")))
print(j.cartes_posables())

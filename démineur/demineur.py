#!/usr/bin/env python
# coding: utf-8

# In[3]:


from random import randrange
from tkinter import *
from affichage import *

def voisins(n, l, i, j):
    return [(a,b) for (a, b) in [(i, j+1),(i, j-1), (i-1, j), (i+1,j), (i+1, j+1), (i+1, j-1), (i-1, j+1), (i-1, j-1)] if a in range(n) and b in range(l)]

def ListeNulle(n, l):
    L=[]
    for i in range(n):
        L.append([0])
        for j in range(l):
            L[i].append(0)
    return L

def afficher(L):
    for i in L:
        for y in i:
            print(y, end = " ")
        print()
        
def placerChiffres(i, y): #creer la liste des chiffres
    global chiffres
    n = len(chiffres)
    l = len(chiffres[0])
    for k in range(len(voisins(n, l, i, y))):
        chiffres[voisins(n, l, i, y)[k][0]][voisins(n, l, i, y)[k][1]] += 1
    return chiffres
        
def placerMines(n, l, d): #creer la liste de mine
    global compteurMine, mines, chiffres
    compteurMine = 0
    chiffres = ListeNulle(n, l)
    mines = ListeNulle(n, l)
    while compteurMine < d:
        x = randrange(0,n)
        y = randrange(0,l)
        if mines[x][y]==0:
            mines[x][y] = 1
            compteurMine+=1
            chiffres = placerChiffres(x,y)
    return mines, chiffres

#on initialise
mines = ListeNulle(9, 9) #liste des mines -- 1 = mine
chiffres = ListeNulle(9, 9) #liste des chiffres
cases = ListeNulle(9, 9) #cases decouverte ou non -- 1 = decouverte
drapeau = ListeNulle(9, 9) #drapeau placé ou non -- 1 = drapeau -- 2 = point d'interrogation
d = 12 #nb mines
compteurMine = 0 #compteur
t = 30 #taille des cases
canClick = True # droit ou non de cliquer
difficulte = 1
placerMines(9, 9, 10)


# In[ ]:





# In[ ]:





# In[ ]:





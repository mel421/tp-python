#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import *
from demineur import *

def creer(n, l): #constuit le plateau
    global canClick, lbl, btn, cnv, btn1, btn2, btn3
    cnv.delete(ALL)
    for i in range(n):
        for y in range(l):
            cnv.create_image(y*t + t//2 + 2 , i*t + t//2 + 2, image = caseLogo)
    canClick = True
    btn.pack(side = "bottom")
    btn1.pack(side = "left")
    btn2.pack(side = "left")
    btn3.pack(side = "left")
    lbl.pack(side = "bottom")
    chronoLbl.pack(side = "right")
    
def changerDifficulte1():
    global mines, compteurMine, chiffres, cases, drapeau, difficulte
    difficulte = 1
    cnv.delete(ALL)
    mines = ListeNulle(9,9)
    cases = ListeNulle(9,9)
    drapeau = ListeNulle(9,9)
    mines, chiffres = placerMines(9,9, 10)
    creer(9,9)
    compteurMine = 10
    cnv["height"] = 270
    cnv["width"] = 270
    lbl["text"] = "10"

def changerDifficulte2():
    global mines, compteurMine, chiffres, cases, drapeau, difficulte
    difficulte = 2
    mines = ListeNulle(16,16)
    cases = ListeNulle(16,16)
    drapeau = ListeNulle(16,16)
    mines, chiffres = placerMines(16,16, 40)
    creer(16,16)
    compteurMine = 40
    cnv["height"] = 480
    cnv["width"] = 480 
    lbl["text"] = "40"

def changerDifficulte3():
    global mines, compteurMine, chiffres, cases, drapeau, difficulte
    difficulte = 3
    mines = ListeNulle(16,30)
    cases = ListeNulle(16,30)
    drapeau = ListeNulle(16,30)
    mines, chiffres = placerMines(16,30, 99)
    creer(16,30)
    compteurMine = 99
    cnv["height"] = 480
    cnv["width"] = 900
    lbl["text"] = "99"
    
def decouvrir(x, y, n, l): #fait le degagement
    for k in range(len(voisins(n, l, x, y))):
        a = voisins(n, l, x, y)[k-1][1]
        b = voisins(n, l, x, y)[k-1][0]
        if(cases[b][a] == 0 and mines[b][a] == 0):
            if(chiffres[b][a] == 1):
                cnv.create_image(a*t + t//2 + 2, b*t + t//2 + 2, image = unLogo)
            elif(chiffres[b][a] == 2):
                cnv.create_image(a*t + t//2 + 2, b*t + t//2 + 2, image = deuxLogo)
            elif(chiffres[b][a] == 3):
                cnv.create_image(a*t + t//2 + 2, b*t + t//2 + 2, image = troisLogo)
            elif(chiffres[b][a] == 4):
                cnv.create_image(a*t + t//2 + 2, b*t + t//2 + 2, image = quatreLogo)
            elif(chiffres[b][a] == 5):
                cnv.create_image(a*t + t//2 + 2, b*t + t//2 + 2, image = cinqLogo)
            elif(chiffres[b][a] == 6):
                cnv.create_image(a*t + t//2 + 2, b*t + t//2 + 2, image = sixLogo)
            elif(chiffres[b][a] == 7):
                cnv.create_image(a*t + t//2 + 2, b*t + t//2 + 2, image = septLogo)
            elif(chiffres[b][a] == 8):
                cnv.create_image(a*t + t//2 + 2, b*t + t//2 + 2, image = huitLogo)
            cases[b][a] = 1
            if(chiffres[b][a] == 0):
                cnv.create_image(a*t + t//2 + 2, b*t + t//2 + 2, image = zeroLogo)
                decouvrir(b, a, n, l)
                
def lose():
    n = len(chiffres)
    l = len(chiffres[0])
    for x in range(len(mines)):
        for y in range(len(mines[0])):
            if(mines[x][y] == 1):
                cnv.create_rectangle(y*t, x*t, y*t+t, x*t+t, fill = "red")
                cnv.create_image(y*t + t//2 + 1, x*t + t//2 + 1, image = mineLogo)
            else:
                if(chiffres[x][y] == 1):
                    cnv.create_image(y*t + t//2 + 2, x*t + t//2 + 2, image = unLogo)
                elif(chiffres[x][y] == 2):
                    cnv.create_image(y*t + t//2 + 2, x*t + t//2 + 2, image = deuxLogo)
                elif(chiffres[x][y] == 3):
                    cnv.create_image(y*t + t//2 + 2, x*t + t//2 + 2, image = troisLogo)
                elif(chiffres[x][y] == 4):
                    cnv.create_image(y*t + t//2 + 2, x*t + t//2 + 2, image = quatreLogo)
                elif(chiffres[x][y] == 5):
                    cnv.create_image(y*t + t//2 + 2, x*t + t//2 + 2, image = cinqLogo)
                elif(chiffres[x][y] == 6):
                    cnv.create_image(y*t + t//2 + 2, x*t + t//2 + 2, image = sixLogo)
                elif(chiffres[x][y] == 7):
                    cnv.create_image(y*t + t//2 + 2, x*t + t//2 + 2, image = septLogo)
                elif(chiffres[x][y] == 8):
            	    cnv.create_image(y*t + t//2 + 2, x*t + t//2 + 2, image = huitLogo)
                cases[x][y] = 1
                if(chiffres[x][y] == 0):
                    cnv.create_image(y*t + t//2 + 2, x*t + t//2 + 2, image = zeroLogo)
    cnv.create_text(len(chiffres[0])*t//2, len(chiffres)*t//2, text = "PERDU", font = "Ubuntu 50 bold")
    
def win():
    for i in range(len(chiffres)):
        for j in range(len(chiffres[0])):
            if(cases[i][j] == 0 and mines[i][j] == 0):
                return False
    return True

def clic1(event):
    global canClick, chiffres, mines, cases
    y = event.x // 30
    x = event.y // 30
    if(canClick == True):    
        if(mines[x][y] == 0):
            if(chiffres[x][y] == 1):
                cnv.create_image(y*t + t//2 + 2, x*t + t//2 + 2, image = unLogo)
            elif(chiffres[x][y] == 2):
                cnv.create_image(y*t + t//2 + 2, x*t + t//2 + 2, image = deuxLogo)
            elif(chiffres[x][y] == 3):
                cnv.create_image(y*t + t//2 + 2, x*t + t//2 + 2, image = troisLogo)
            elif(chiffres[x][y] == 4):
                cnv.create_image(y*t + t//2 + 2, x*t + t//2 + 2, image = quatreLogo)
            elif(chiffres[x][y] == 5):
                cnv.create_image(y*t + t//2 + 2, x*t + t//2 + 2, image = cinqLogo)
            elif(chiffres[x][y] == 6):
                cnv.create_image(y*t + t//2 + 2, x*t + t//2 + 2, image = sixLogo)
            elif(chiffres[x][y] == 7):
                cnv.create_image(y*t + t//2 + 2, x*t + t//2 + 2, image = septLogo)
            elif(chiffres[x][y] == 8):
                cnv.create_image(y*t + t//2 + 2, x*t + t//2 + 2, image = huitLogo)
            cases[x][y] = 1
            if(chiffres[x][y] == 0):
                cnv.create_image(y*t + t//2 + 2, x*t + t//2 + 2, image = zeroLogo)
                decouvrir(x, y, len(chiffres), len(chiffres[0]))
            if(win() == True):
                canClick = False
                cnv.create_text(len(chiffres)*t//2, len(chiffres[0])*t//2, text = "GAGNÉ", font = "Ubuntu 50 bold")

        else:
            canClick = False
            lose()
        
def clic2(event):
    global compteurMine
    y = event.x // 30
    x = event.y // 30
    if(cases[x][y] == 0 and canClick == True):
        if(drapeau[x][y] == 0 and compteurMine > 0):
            drapeau[x][y]=1
            compteurMine -= 1
            lbl["text"] = str(compteurMine)
            cnv.create_image(y*t + t//2 + 2 , x*t + t//2 + 2, image = drapeauLogo)
        elif(drapeau[x][y] == 1):
            drapeau[x][y]=2
            cnv.create_image(y*t + t//2 + 2 , x*t + t//2 + 2, image = pointLogo)
            compteurMine += 1
            lbl["text"] = str(compteurMine)
        else:    
            drapeau[x][y]=0
            cnv.create_image(y*t + t//2 + 2 , x*t + t//2 + 2, image = caseLogo)

def redemarrer():
    if difficulte == 1:
        changerDifficulte1()
    if difficulte == 2:
        changerDifficulte2()
    if difficulte == 3:
        changerDifficulte3()

def chrono(timer):
    while(canClick == True):
        timer += 1
        chronoLbl["text"] = str(timer)
        cnv.after(1000, chrono, timer)
    

jeu = Tk()

t = 30
drapeauLogo = PhotoImage(file = "drapeau.png")
mineLogo = PhotoImage(file = "mine.png")
caseLogo = PhotoImage(file = "case.png")
pointLogo = PhotoImage(file = "point.png")
zeroLogo = PhotoImage(file = "0.png")
unLogo = PhotoImage(file = "1.png")
deuxLogo = PhotoImage(file = "2.png")
troisLogo = PhotoImage(file = "3.png")
quatreLogo = PhotoImage(file = "4.png")
cinqLogo = PhotoImage(file = "5.png")
sixLogo = PhotoImage(file = "6.png")
septLogo = PhotoImage(file = "7.png")
huitLogo = PhotoImage(file = "8.png")
cnv = Canvas(jeu, width = 270 , height = 270)
cnv.pack(side = "bottom")
btn = Button(jeu, text="Redemarrer", fg="white", bg="red", command = redemarrer, height = 2, width= 8)
btn1 = Button(jeu, text="1", fg="black", bg="red", command = changerDifficulte1, height = 2, width= 2)
btn2 = Button(jeu, text="2", fg="blue", bg="red", command = changerDifficulte2, height = 2, width= 2)
btn3 = Button(jeu, text="3", fg="yellow", bg="red", command = changerDifficulte3, height = 2, width= 2)
lbl = Label(jeu,text="10",  font='Arial 25 bold', bg='white', width=5)
chronoLbl = Label(jeu,text="0",  font='Arial 25 bold', bg='white', width=5)

cnv.bind("<Button-1>", clic1) #clic gauche
cnv.bind("<Button-3>", clic2) #clic droit : drapeau
creer(9, 9)

jeu.mainloop()
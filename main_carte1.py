from appJar import gui
from deck import Deck
from tkinter import *
from card import Carte
from test_card import random_card_Nbr

#app = gui()


mywindow = Tk()

app = gui()

def test(win):
    if mywindow.destroy:
        app.showSubWindow(win)

app.setTitle("Karta kbir yakel sghir")
app.setIcon(r"C:\Users\AMJAD\Desktop\new\src\favicon.ico")
app.setSize("600x350")
app.addLabelOptionBox("couleur", ["\u2660", "\u2665", "\u2666", "\u2663"], 0, 0)
app.addLabelOptionBox("valeur", [str(i) for i in range(1, 14)], 0, 2)

def on_click(button):
    couleur = app.getOptionBox("couleur")
    valeur = app.getOptionBox("valeur")
    if couleur == "\u2660":
        app.setImage("Carte_image", Carte(int(valeur), Carte.PIQUE).image())
    elif couleur == "\u2665":
        app.setImage("Carte_image", Carte(int(valeur), Carte.COEUR).image())
    elif couleur == "\u2666":
        app.setImage("Carte_image", Carte(int(valeur), Carte.CARREAU).image())
    elif couleur == "\u2663":
        app.setImage("Carte_image", Carte(int(valeur), Carte.TREFLE).image())

#app.addButton("affiche carte", on_click, 1, 1)
app.addImage("Carte_image", "src/empty.gif", 0, 1)

user1 = Deck()
user2 = Deck()

import random

def press(button):  # sourcery skip: last-if-guard
    if button == "Take card from player 2":
        if  user2.L[-1][0] < user1.L[-1][0]:
            user1.L.insert(0, user1.L[-1])
            user1.supprime()
            #print(user1.L)
            user1.L.insert(0, user2.L[-1])
            user2.supprime()
            user1.voir()
            user1.nombre()
            #random.choice(user1.L)
            #print(user1.L)
            app.setLabel("nombre cards player 1",str(len(user1.L)))
            app.setLabel("nombre cards player 2",str(len(user2.L)))
            #print("User 1 =>>",len(user1.L))
            #print("User 2 =>>",len(user2.L))
    elif button == "take card from player 1":
        if  user1.L[-1][0] < user2.L[-1][0]:
            user2.L.insert(0, user2.L[-1])
            user2.supprime()
            user2.L.insert(0, user1.L[-1])
            user1.supprime()
            user2.voir()
            user2.nombre()
                            #random.choice(user2.L)
                            #print(user2.L)
                            #print("User 1 =>>",len(user1.L))
                            #print("User 2 =>>",len(user2.L))
            app.setLabel("nombre cards player 1",str(len(user1.L)))
            app.setLabel("nombre cards player 2",str(len(user2.L)))

app.addButton("take card from player 1", press, 1, 2, 1)
app.addButton("Take card from player 2", press, 1, 0, 1)



def compare_():
    if user1.L[-1][0] < user2.L[-1][0]:
        print("")
        

        
        

def button_user1_affichage():
    app.setImage("carte image user2","resources/Playing_card_" + str(user1.L[-1][1]) + "_" + str(user1.L[-1][0]) + ".gif")
    return 1

app.addButton("afficher la carte a user1", button_user1_affichage, 2, 0)
app.addImage("carte image user1", "src/Aluette_card_deck_-_Grimaud_-_1858-1890_-_Back_side.gif", 0,2)    

def button_user2_affichage():
    app.setImage("carte image user1","resources/Playing_card_" + str(user2.L[-1][1]) + "_" + str(user2.L[-1][0]) + ".gif")
    return [user2.L[-1][1], user2.L[-1][0]]


app.addButton("afficher la carte a user2", button_user2_affichage, 2, 2)
app.addImage("carte image user2", "src/Aluette_card_deck_-_Grimaud_-_1858-1890_-_Back_side.gif", 0, 0)




from list_ import list_from_1_13_card

def distribute():
    if list_from_1_13_card() in user1.L and list_from_1_13_card() in user2.L:
        return

    new_user1_L = []
    new_user2_L = []
    for i in range(53):
        if i%2==0 and len(user1.L) < 26:
            user1.L.append(random_card_Nbr())
        elif len(user2.L) < 26:
            user2.L.append(random_card_Nbr())


    print("User 1 =>>",user1.L)
    print("User 2 =>>",user2.L)
    print("card total: =>> Player 1", len(user1.L))
    print("card total: =>> Player 2: ", len(user2.L))
    app.setLabel("nombre cards player 1",str(len(user1.L)))
    app.setLabel("nombre cards player 2",str(len(user2.L)))

app.addLabel("nombre cards player 1", str(len(user1.L)), 4, 0, 2)
app.addLabel("nombre cards player 2", str(len(user2.L)), 4, 2, 2)
app.addButton("distribuer les cartes", distribute, 2, 1)
app.go()





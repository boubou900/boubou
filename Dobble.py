from random import *
def groupelettre(l_en_commun):#fonction qui creer aleatoirement un premier groupe de lettres et fait le second en fonction du premier en ayant comme arguments une lettre en commun ou non
    groupe1=[]#groupe de lettre a gauche de l'ecran
    for i in range (8):
         une_lettre_aletoire=randint(0,25)
         une_lettre_aletoire=une_lettre_aletoire+65
         une_lettre_aletoire=chr(une_lettre_aletoire)#utilisation code cesar pour passer d'un nombre aleatoire a une lettre
         groupe1.append(une_lettre_aletoire)
    groupe2=[]#groupe de lettre a droite de l'ecran
    
    if (l_en_commun==False):#creation du second groupe de lettre en ne mettant pas de lettre en commun
        while (len(groupe2)!=8):
            une_lettre_aletoire=randint(0,25)
            une_lettre_aletoire=une_lettre_aletoire+65
            une_lettre_aletoire=chr(une_lettre_aletoire)
            if (une_lettre_aletoire not in groupe1):#test de si la lettre aleatoire est deja present dans le groupe 1
                groupe2.append(une_lettre_aletoire)
            
    elif (l_en_commun==True):#creation du second groupe de lettre en mettant au minimum une lettre en commun
        for i in range (8):#creation aleatoire second groupe de lettre
            une_lettre_aletoire=randint(0,25)
            une_lettre_aletoire=une_lettre_aletoire+65
            une_lettre_aletoire=chr(une_lettre_aletoire)
            groupe2.append(une_lettre_aletoire)
        n_lettre_g1=randint(0,7)#choisi un nombre aleatoire entre 0 et 7(pour le numero de lettre du groupe 1)
        n_lettre_g2=randint(0,7)#choisi un nombre aleatoire entre 0 et 7((pour le numero de lettre du groupe 2)
        groupe2[n_lettre_g2]=groupe1[n_lettre_g1]#modifie la lettre numeroté du nombre aleatoire du groupe de 2 pour la remplacer avec celle de la lettre numeroté du nombre aleatoire du groupe de 1
        
        
    return groupe1,groupe2
    
def affichage(groupe1,groupe2):#fonction qui affiche les deux groupes de lettres 
    affichageg1=groupe1
    affichageg2=groupe2
    print("  ",affichageg1[0],affichageg1[1],"                       ",affichageg2[0],affichageg2[1],"\n",affichageg1[7],"  ",affichageg1[2],"                    ",affichageg2[7],"  ",affichageg2[2],"\n",affichageg1[6],"  ",affichageg1[3],"                    ",affichageg2[6],"  ",affichageg2[3],"\n"," ",affichageg1[5],affichageg1[4],"                       ",affichageg2[5],affichageg2[4])

def tour(nom_joueur1,points_joueur1,nom_joueur2,points_joueur2):
    l_en_commun=randint(0,1)
    if (l_en_commun==0):
        l_en_commun=True
    else:
        l_en_commun=False
    b=groupelettre(l_en_commun)
    affichage(b[0],b[1])
    lettre_tape=input("Tapez!")
    #comptage des points en fonction de si les joueurs ont raison ou non

    if lettre_tape== "":
        print("Veuillez appuyer sur les bonnes touches.")
    elif lettre_tape[0]== "q" and l_en_commun==False:           #lejoueur 1 pense qu'il n' y a pas de lettre en commun : il a raison → +1pt
        points_joueur1=points_joueur1+1
        print(nom_joueur1,"gagne un point.")
    elif lettre_tape[0]== "q" and l_en_commun==True:          #lejoueur 1 pense qu'il n' y a pas de lettre en commun : il a tord → -5pts
        points_joueur1=points_joueur1-5
        print(nom_joueur1,"perd 5 points.")
        if points_joueur1<0:
            points_joueur1=0
    elif lettre_tape[0]== "l" and l_en_commun==False:         #lejoueur 2 pense qu'il n' y a pas de lettre en commun : il a raison → +1pt
        points_joueur2=points_joueur2+1
        print(nom_joueur2,"gagne un point.")
    elif lettre_tape[0]== "l" and l_en_commun==True:          #lejoueur 2 pense qu'il n' y a pas de lettre en commun : il  a tord → -5pts
        points_joueur2=points_joueur2-5
        print(nom_joueur2,"perd 5 points.")
        if points_joueur2<0:
            points_joueur2=0
    elif lettre_tape[0]== "s" and l_en_commun==True:            #lejoueur 1 pense qu'il  y a une lettre en commun : il a raison → +1pt
        points_joueur1=points_joueur1+1
        print(nom_joueur1,"gagne un point.")
    elif lettre_tape[0]== "s" and l_en_commun==False:         #lejoueur 1 pense qu'il  y a une lettre en commun : il a tord → -5pts
        points_joueur1=points_joueur1-5
        print(nom_joueur1,"perd 5 points.")
        if points_joueur1<0:
            points_joueur1=0
    elif lettre_tape[0]== "m" and l_en_commun==True:            #lejoueur 2 pense qu'il  y a une lettre en commun : il a raison → +1pt
        points_joueur2=points_joueur2+1
        print(nom_joueur2,"gagne un point.")
    elif lettre_tape[0]== "m" and l_en_commun==False:         #lejoueur 2 pense qu'il  y a une lettre en commun : il a tord → -5pts
        points_joueur2=points_joueur2-5
        print(nom_joueur2,"perd 5 points.")
        if points_joueur2<0:
            points_joueur2=0
    else:
        print("Veuillez appuyer sur les bonnes touches.")
    print(nom_joueur1,"a",points_joueur1,"points et",nom_joueur2,"a",points_joueur2,"points.")
    rappel=print("\nRappel touche:\n\nPour ",nom_joueur1,":\nQ pour pas de lettre en commun\nS pour lettre en commun.\n\nPour ",nom_joueur2,":\nL pour pas de lettre en commun\nM pour lettre en commun.\n\n")
    pause=input("Appuyez sur entrée lorsque vous etes pret.")
    
    return points_joueur1,points_joueur2         #la fonction retoune les points des deux joueurs 

        
def jeu ():
    nom_joueur1=input(" Quel est le nom du premier joueur ? ")#variables associées aux noms des deux joueurs
    print("Pour ",nom_joueur1,", si vous considèrez qu’il n’y a pas de lettre en commun tapez Q et si vous considèrez qu’il y a une ou plusieurs lettre en commun tapez S.")#instructions pour le joueur 1
    nom_joueur2=input(" Quel est le nom du deuxième joueur ? ")
    print("Pour ",nom_joueur2,", si vous considèrez qu’il n’y a pas de lettre en commun tapez L et si vous considèrez qu’il y a une ou plusieurs lettre en commun tapez M.appuyez sur espace lorsque vous êtes prêt")#instructions pour le joueur 2
    pret=input()
    points_joueur1=0        #initialisation des variables
    points_joueur2=0
    while (points_joueur1!=10)and(points_joueur2!=10):
        points_joueur1,points_joueur2=tour(nom_joueur1,points_joueur1,nom_joueur2,points_joueur2) #variables associées aux points des joueurs donnés par la fonction tour qui ici est appelé
        
    if (points_joueur1==1):
        print("GG,",nom_joueur1,"a gagné et ",nom_joueur2," a perdu!")
    else:
        print("GG,",nom_joueur2,"a gagné et ",nom_joueur1," a perdu!")
    
        
partie=jeu()
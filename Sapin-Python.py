#Vidéo de ce premier test avec Python disponible ici : https://www.youtube.com/watch?v=PchoV66BFqs
print ("Salut les Noobs !\n")
#On demande la taille que veux l'utilisateur
taille_du_sapin=input("Indiquez une hauteur de 4 à 20\n")
#On initialise les variables
taille_du_sapin=int(taille_du_sapin)-1
etage_du_sapin=0
nombre_d_etoiles=1
#On dit que le maximum d'étoiles qu'on aura en dernière ligne est = à la taille que l'utilisateur a mis x 2 - 1 | Exemple 5 x 2 = 10; 10 - 1 = 9
max_etoiles=int(taille_du_sapin)*2-1
#Tant qu'on a pas affiché le nombre de lignes qu'a demandé l'utilisateur, on affiche des boules et des étoiles au sapin
while (etage_du_sapin <= int(taille_du_sapin)):
    boule_ou_etoile=1
    #On affiche un nombre d'espace = au nombre_etoiles puis on affiche toujours une * en premier
    print(" "*max_etoiles+"*", end="")
    #Tant qu'il nous reste à afficher des éléments sur la ligne (si le nombre de boules est < ou = à l'étage que nous écrivons...
    while boule_ou_etoile <= etage_du_sapin * 2:
        #...on écrit une "*" si le nombre est pair
        if boule_ou_etoile%2==0:
            print("*", end="")
        #... ou on écrit un "o" si le nombre est impair   
        else:
            print("o", end="")
        #On dit qu'on a ajouté une boule ou une étoile    
        boule_ou_etoile = boule_ou_etoile+1
    #On fait un retour à la ligne    
    print("\n",end="")
    #On dit qu'on a ajouté une ligne au sapin
    etage_du_sapin = etage_du_sapin + 1
    #On dit qu'il nous faudra retirer un espace à la ligne suivante
    max_etoiles = max_etoiles - 1
#Si la taille du sapin saisie par l'utilisateur est < ou = à 5 alors on affiche des espaces (2x la taille saisie par l'utilisateur - 2 |Exemple : 5x2-2 = 8 espaces) puis on ajoute le pied du sapin
if int(taille_du_sapin) <= 5:
    print (" "*(int(taille_du_sapin)*2-2), end="")
    print("|||")
#Si la taille du sapin saisie par l'utilisateur est > à 5 et < ou = à 8 alors on affiche des espaces (2x la taille saisie par l'utilisateur - 3 |Exemple : 8x2-3 = 15 espaces) puis on ajoute le pied du sapin    
if int(taille_du_sapin) >5 and int(taille_du_sapin) <=8:
    print (" "*(int(taille_du_sapin)*2-3), end="")
    print("|||||")
#Si la taille du sapin saisie par l'utilisateur est > à 8 alors on affiche des espaces (2x la taille saisie par l'utilisateur - 4 |Exemple : 10x2-3 = 18 espaces) puis on ajoute le pied du sapin        
if int(taille_du_sapin) >8:
    print (" "*(int(taille_du_sapin)*2-4), end="")
    print("|||||||")
#On souhaite bonne fêtes parce qu'on est poli (abonnez-vous, faites-pas vos chiens...) - https://www.youtube.com/c/SalutlesNoobs   
print ("Bonnes fêtes !")

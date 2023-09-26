
ListeEntrees = ["1- Salade de chef\t\t 12 euros\n","2- Salade niçoise\t\t 10 euros\n" ,"3- Salade grecque\t\t 9 euros\n","4- Salade italienne\t\t 11 euros\n"]
ListePrixEntree =[12,10,9,11]
ListePlats = ["1- Friture de poissons\t\t 25 euros\n","2- Bavette de veau \t\t 19 euros\n","3- Saumon à la plancha\t\t 22 euros\n","4- Boeuf bourguinois\t\t 16 euros\n"]
ListePrixPlats = [25,19,22,16]
ListeDesserts= ["1- Créme brulée\t\t 7 euros\n","2- Tiramissu\t\t 8 euros\n","3- Glace aux choix\t 9 euros\n","4- Panacota\t\t 6 euros\n"]
ListePrixDesserts = [7,8,9,6]

print("-----Bienvenue au restaurant PyFood-----\n")

print ("Voila ce qu'on propose comme entrée :\n")

print(ListeEntrees[0])
print(ListeEntrees[1])
print(ListeEntrees[2])
print(ListeEntrees[3])


ListeEntrees= 0
while ListeEntrees== 0:
    ListeEntrees_str = input("Quel est votre entrée ? : ")
    try:
        ListeEntrees= int(ListeEntrees_str) # si le cast fonctionne je passe à la suite :(else) et je saute except
    except: # si le cast ne fonctionne pas je lève une exception
        print("Vous n'avez pas saisi une valeur numérique")
    else:
        if ListeEntrees== 0: # si la valeur saisie est = zéro
            print("Vous avez saisi zéro")
        elif ListeEntrees< 0: # si la valeur saisie est négative
            print("Vous avez saisi une valeur négative")
            ListeEntrees= 0   #je réaffecte 0 à entrée pour revenir à la condition initiale
        elif ListeEntrees> 4:
            print("Nous n'avons pas cette  entrée !")
            ListeEntrees= 0
        else: # si la valeur saisi est correcte (différente de zéro, n'est pas négative et une valeur numérique)
            print("Vous avez choisi {}.".format(ListeEntrees))







            #c est amir tien une aide fait avec des tuples


            #exemple 

            entree = (

            ("Salade de chef",12),
            ("Salade niçoise",10),
            ("Salade grecque",9),
            ("Salade italienne",11)
            )


            #voila apres tu fait le reste est tu modifie ton code 
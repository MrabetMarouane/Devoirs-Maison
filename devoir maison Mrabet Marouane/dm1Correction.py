print ("**************************************************\n")
print ("-----Bienvenue au restaurant PyFood-----\n")

# Choix entrées  
print ("Voila ce qu'on propose comme entrée :\n")

print ("1- Salade de chef\t\t 12 euros\n")
print ("2- Salade niçoise\t\t 10 euros\n")
print ("3- Salade grecque\t\t 9 euros\n")
print ("4- Salade italienne\t\t 11 euros\n")


entrees= 0
while entrees== 0:
    entrees_str = input("Quel est votre entrees? : ")
    try:
        entrees= int(entrees_str) # si le cast fonctionne je passe à la suite :(else) et je saute except
    except: # si le cast ne fonctionne pas je lève une exception
        print("Vous n'avez pas saisi une valeur numérique")
    else:
        if entrees== 0: # si la valeur saisie est = zéro
            print("Vous avez saisi zéro")
        elif entrees< 0: # si la valeur saisie est négative
            print("Vous avez saisi une valeur négative")
            entrees= 0   #je réaffecte 0 à entrees pour revenir à la condition initiale
        elif entrees> 4:
            print("Nous n'avons pas cette  entrée !")
            entrees= 0
        else: # si la valeur saisi est correcte (différente de zéro, n'est pas négative et une valeur numérique)
            print("Vous avez choisi {}.".format(entrees))


prix_entrees = 0  # Initialisation de prix_entrees

if entrees in [1, 2, 3, 4]:
# Gestion des choix d'entrées
    if entrees == 1: 
        print("1- Salade de chef\t\t 12 euros\n")
        prix_entrees = 12
    elif entrees == 2: 
        print("2- Salade niçoise\t\t 10 euros\n")
        prix_entrees = 10
    elif entrees == 3: 
        print("3- Salade grecque\t\t 9 euros\n")
        prix_entrees = 9
    elif entrees == 4: 
        print("4- Salade italienne\t\t 11 euros\n")
        prix_entrees = 11




 # Choix plats 
    print ("Passons maintenant aux plats :\n")

    print ("1- Friture de poissons\t\t 25 euros\n")
    print ("2- Bavette de veau \t\t 19 euros\n")
    print ("3- Saumon à la plancha\t\t 22 euros\n")
    print ("4- Boeuf bourguinois\t\t 16 euros\n")



plats= 0
while plats== 0:
    plats_str = input("Veuillez saisir votre choix (1-4) : ")
    try:
        plats= int(plats_str) # si le cast fonctionne je passe à la suite :(else) et je saute except
    except: # si le cast ne fonctionne pas je lève une exception
        print("Vous n'avez pas saisi une valeur numérique")
    else:
        if plats== 0: # si la valeur saisie est = zéro
            print("Vous avez saisi zéro")
        elif plats< 0: # si la valeur saisie est négative
            print("Vous avez saisi une valeur négative")
            plats= 0   #je réaffecte 0 à plats pour revenir à la condition initiale
        elif plats> 4:
            print("Nous n'avons pas ce  plats !")
            plats= 0
        else: # si la valeur saisi est correcte (différente de zéro, n'est pas négative et une valeur numérique)
            print("Vous avez choisi {}.".format(plats))



prix_plats = 0  # Initialisation de prix_plats

if plats in [1, 2, 3, 4]:
 # Gestion des choix de plats
    if plats == 1: 
         print("1- Friture de poissons\t\t 25 euros\n")
         prix_plats = 25
    elif plats == 2: 
         print("2- Bavette de veau\t\t 19 euros\n")
         prix_plats = 19
    elif plats == 3: 
         print("3- Saumon à la plancha\t\t 22 euros\n")
         prix_plats = 22
    elif plats == 4: 
         print("4- Boeuf bourguinois\t\t 16 euros\n")
         prix_plats = 16
    




# Choix desserts
print ("Pour finir je vous propose un dessert  :\n")

print ("1- Créme brulée\t\t 7 euros\n")
print ("2- Tiramissu\t\t 8 euros\n")
print ("3- Glace aux choix\t 9 euros\n")
print ("4- Panacota\t\t 6 euros\n")


desserts= 0
while desserts== 0:
    desserts_str = input("Veuillez saisir votre choix (1-4) : ")
    try:
        desserts= int(desserts_str) # si le cast fonctionne je passe à la suite :(else) et je saute except
    except: # si le cast ne fonctionne pas je lève une exception
        print("Vous n'avez pas saisi une valeur numérique")
    else:
        if desserts== 0: # si la valeur saisie est = zéro
            print("Vous avez saisi zéro")
        elif desserts< 0: # si la valeur saisie est négative
            print("Vous avez saisi une valeur négative")
            desserts= 0   #je réaffecte 0 à desserts pour revenir à la condition initiale
        elif desserts> 4:
            print("Nous n'avons pas ce  desssert !")
            desserts= 0
        else: # si la valeur saisi est correcte (différente de zéro, n'est pas négative et une valeur numérique)
            print("Vous avez choisi {}.".format(desserts))


prix_desserts = 0  # Initialisation de prix_desserts
if desserts in [1, 2, 3, 4]:
# Gestion des choix de desserts

     if desserts == 1: 
         print("1- Créme brulée\t\t 7 euros\n")
         prix_desserts = 7
     elif desserts == 2: 
         print("2- Tiramissu\t\t 8 euros\n")
         prix_desserts = 8
     elif desserts == 3: 
         print("3- Glace aux choix\t\t9 euros\n")
         prix_desserts = 9
     elif desserts == 4: 
         print("4- Panacota\t\t 6 euros\n")
         prix_desserts = 6




# Calcul et affichage du total

prix_total = prix_entrees + prix_plats + prix_desserts
print(f"Total à payer : {prix_entrees} + {prix_plats} + {prix_desserts} = {prix_total} euros ")

print ("**************************************************\n")
print ("-----Bienvenue au restaurant PyFood-----\n")

# Choix entrées  
print ("Voila ce qu'on propose comme entrée :\n")

print ("1- Salade de chef\t\t 12 euros\n")
print ("2- Salade niçoise\t\t 10 euros\n")
print ("3- Salade grecque\t\t 9 euros\n")
print ("4- Salade italienne\t\t 11 euros\n")

entrees = int(input("Veuillez saisir votre choix (1-4) : "))

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
else:
    print("Choix invalide. Veuillez entrer un nombre entre 1 et 4.")

# Choix plats 
print ("Passons maintenant aux plats :\n")

print ("1- Friture de poissons\t\t 25 euros\n")
print ("2- Bavette de veau \t\t 19 euros\n")
print ("3- Saumon à la plancha\t\t 22 euros\n")
print ("4- Boeuf bourguinois\t\t 16 euros\n")

plats = int(input("Veuillez saisir votre choix (1-4) : "))

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
else:
    print("Choix invalide. Veuillez entrer un nombre entre 1 et 4.")

# Choix desserts
print ("Pour finir je vous propose un dessert  :\n")

print ("1- Créme brulée\t\t 7 euros\n")
print ("2- Tiramissu\t\t 8 euros\n")
print ("3- Glace aux choix\t 9 euros\n")
print ("4- Panacota\t\t 6 euros\n")

desserts = int(input("Veuillez saisir votre choix (1-4) : "))

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
else:
    print("Choix invalide. Veuillez entrer un nombre entre 1 et 4.")

# Calcul et affichage du total
prix_total = prix_entrees + prix_plats + prix_desserts
print(f"Total à payer : {prix_entrees} + {prix_plats} + {prix_desserts} = {prix_total} euros ")
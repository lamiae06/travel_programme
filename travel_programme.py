def hotel_frais(nuit):
    prix_nuits = 90*nuit 
    return prix_nuits   
def location_voiture_frais(jours):
    prix_location = 40*jours
    if jours >= 3 and jours <7:
        prix_location -= 20
    elif jours >= 7:
        prix_location -= 50
    return prix_location
def vol_frais(ville):
    ville = ville.lower()  # ignore majuscules/minuscules
    if ville == "marrakech":
        return 35
    elif ville == "paris":
        return 200
    elif ville == "oran":
        return 78
    elif ville == "carthage":
        return 182
    elif ville == "dakar":
        return 25
    else:
        print("Ville non reconnue, prix du vol = 0")
        return 0
def voyage_frais(nuit, jours, ville):
    total_frais = hotel_frais(nuit) + location_voiture_frais(jours) + vol_frais(ville)
    return total_frais
def main():
    print("========================================")
    print("         Bienvenue dans TravelApp       ")
    print("========================================")
    print("Tarifs disponibles :")
    print("- Hôtel : 90 € par nuit")
    print("- Location voiture : 40 € par jour")
    print("  * 3 à 6 jours : réduction de 20 €")
    print("  * 7 jours et plus : réduction de 50 €")
    print("Vols disponibles :")
    print("- Marrakech : 35 €")
    print("- Paris : 200 €")
    print("- Oran : 78 €")
    print("- Carthage : 182 €")
    print("- Dakar : 25 €")
    print("========================================\n") 
    nuit = int(input("Entrez le nombre de nuits : "))
    jours = int(input("Entrez le nombre de jours de location de voiture : "))
    ville = input("Entrez la ville de destination (marakech, paris, oran, carthage, dakar) : ")
    print("Le coût total de votre voyage est de : ", voyage_frais(nuit, jours, ville), "euros")

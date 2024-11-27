def to_int(data):
    # Retirer les espaces éventuels et convertir en secondes
    hour, minute, second = map(int, data.strip().split(':'))
    return hour * 3600 + minute * 60 + second

dictionnaire = {}

# Ouvrir le fichier CSV
with open('horaires_semaine.csv', 'r') as file:
    for line in file:
        if line[0] != ',':  # Vérifie si la ligne n'est pas vide
            data = line.strip().split(',')
            # Calcul du temps travaillé
            travail_matin = to_int(data[3]) - to_int(data[2])  # Départ midi - Arrivée matin
            travail_apresmidi = to_int(data[5]) - to_int(data[4])  # Départ soir - Arrivée midi
            total_travail = travail_matin + travail_apresmidi
            if data[0] in dictionnaire:
                dictionnaire[data[0]] += total_travail
            else:
                dictionnaire[data[0]] = total_travail
cible = 35 * 3600
min_diff = float('inf')
for clef in dictionnaire:
    diff = abs(dictionnaire[clef] - cible)
    if diff<min_diff:
        print('HIT : ', clef)
        min_diff = diff

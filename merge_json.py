import json

# Lire le contenu du premier fichier JSON
with open('part_aa_translated_fr.json', 'r', encoding='utf-8') as file:
    data_aa = json.load(file)

# Lire le contenu du deuxième fichier JSON
with open('part_ab_translated_fr.json', 'r', encoding='utf-8') as file:
    data_ab = json.load(file)

# Fusionner les données des deux fichiers
merged_data = data_aa + data_ab

# Écrire les données fusionnées dans un nouveau fichier JSON
with open('merged_file.json', 'w', encoding='utf-8') as file:
    json.dump(merged_data, file, ensure_ascii=False, indent=4)

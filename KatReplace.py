import csv
import os

# Fichiers à utiliser
csv_file = "KatSearch.csv"  # Fichier CSV à modifier
txt_file = "KatFind.txt"  # Fichier TXT contenant les KatSearch et KatFind
csv_output = "FinalKat.csv"  # Fichier CSV où seront enregistrées les lignes modifiées
erreur_file = "erreur.txt"  # Fichier pour les lignes avec erreurs

# Charger les paires de KatSearch:KatFind depuis le fichier txt
replacements = {}
with open(txt_file, 'r', encoding='utf-8') as f:
    for line in f:
        if ':' in line:
            parts = line.strip().split(':')
            if len(parts) == 2:  # Assurer que la ligne a bien un format "KatSearch:KatFind"
                replacements[parts[0].strip()] = parts[1].strip()
            else:
                # Ajouter dans erreur.txt les lignes mal formatées
                with open(erreur_file, 'a', encoding='utf-8') as err_f:
                    err_f.write(line)

# Lire le fichier CSV, chercher les correspondances et appliquer les remplacements
found_rows = []
remaining_rows = []
with open(csv_file, 'r', encoding='utf-8') as csv_in:
    reader = csv.reader(csv_in)
    header = next(reader)  # En-tête du fichier CSV

    # Index de la colonne KatSearch (dernière colonne dans le CSV d'origine)
    kat_search_index = header.index("KatSearch")

    for row in reader:
        kat_search = row[kat_search_index].strip()  # La colonne KatSearch contient KatSearch
        if kat_search in replacements:
            # Ajouter KatFind correspondante à la ligne
            kat_find = replacements[kat_search]
            row.append(kat_find)
            found_rows.append(row)
        else:
            # Ajouter la ligne dans les lignes restantes
            remaining_rows.append(row)

# Écrire les lignes modifiées dans le fichier FinalKat.csv
with open(csv_output, 'w', encoding='utf-8', newline='') as csv_out:
    writer = csv.writer(csv_out)

    # Ajouter la colonne 'KatFind' dans l'en-tête, juste après 'KatSearch'
    writer.writerow(header + ['KatFind'])
    
    for row in found_rows:
        writer.writerow(row)

# Écrire les lignes restantes dans le fichier CSV d'origine
with open(csv_file, 'w', encoding='utf-8', newline='') as csv_in:
    writer = csv.writer(csv_in)
    writer.writerow(header)  # Réécrire l'en-tête original
    for row in remaining_rows:
        writer.writerow(row)

# Supprimer les lignes traitées du fichier txt
with open(txt_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

with open(txt_file, 'w', encoding='utf-8') as f:
    for line in lines:
        kat_search = line.split(':')[0].strip()
        if kat_search not in replacements or kat_search not in [row[kat_search_index].strip() for row in found_rows]:
            f.write(line)

print(f"Le fichier modifié a été sauvegardé sous le nom : {csv_output}")
print(f"Les lignes incorrectes ont été enregistrées dans : {erreur_file}")


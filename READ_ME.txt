README

Ce script permet de modifier un fichier CSV en ajoutant des informations basées sur un fichier texte de correspondances.
Format des fichiers :

    KatFind.txt : Chaque ligne doit avoir la forme texte-a-chercher:texte-a-ajouter.
    KatSearch.csv : Doit contenir une colonne nommée KatSearch avec les identifiants à chercher.

Exécution du script :

    Placez KatSearch.csv, KatFind.txt et le script dans le même dossier.
    Exécutez le script avec la commande :

    bash

    python3 KatReplace.py

Fichiers générés :

    FinalKat.csv : Contient les lignes modifiées.
    erreur.txt : Contient les lignes mal formatées.


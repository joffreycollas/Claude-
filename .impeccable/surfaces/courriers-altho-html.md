---
version: 1
slug: "courriers-altho-html"
primary_target: "Courriers_ALTHO.html"
related_targets: []
---

## Scope

Application de campagne de révision d'honoraires (fichier HTML unique, hors ligne). Mode : Operate. Tâche : préparer, vérifier et imprimer en une séance les courriers d'augmentation de tous les clients.

## Audience and task

L'expert-comptable d'ALTHO EXPERTISE, seul, à son bureau, une fois par an. Importer ou saisir les clients, ajuster les taux, relire chaque lettre, imprimer la sélection (ou PDF).

## Direction contract

THESIS: La lettre imprimée est le produit : une feuille A4 à l'échelle réelle occupe le centre du bureau, et chaque contrôle autour modifie ce qui est sur le papier. Refuse le tableau de bord d'admin (menu latéral + cartes de chiffres + tableau) et le tableur.

OWN-WORLD: Un bureau en lumière du jour : plan de travail gris chaud clair, feuille blanche avec une ombre de papier réelle, une seule encre d'accent, le bleu marine de l'en-tête ALTHO, pour l'action principale, la sélection et le focus. Chiffres tabulaires partout. Une seule famille (Source Sans 3, embarquée) pour l'interface et la lettre. Filets fins, rayons 6–8 px, pas de cartes.

STORY: L'utilisateur voit tout de suite la lettre d'un vrai client, comprend qu'elle se remplit toute seule, parcourt ses clients à gauche, corrige à droite, puis imprime la sélection en un clic.

FIRST VIEWPORT: Barre haute : ALTHO EXPERTISE, onglets Courriers / Clients / Réglages, bouton principal « Imprimer la sélection (N) » à droite. Colonne gauche 300 px : recherche, filtres, liste des clients (société, nouveau total, écart), case « à envoyer ». Centre : la feuille A4 à la hauteur de l'écran. Droite 340 px : fiche du client sélectionné (identité, adresse, honoraires par mission avec nouveau montant en direct). Interaction signature : survoler ou éditer un champ fait briller sa place sur la lettre ; un interrupteur « Fenêtre d'enveloppe » dessine la fenêtre DL sur la feuille pour prouver que l'adresse y tient.

FORM: Pick grounded candidate #1 (la lettre au centre), choisie par l'utilisateur à la place du tirage (#7, bordereau à souches). Seed key 29a83770 (tirage dégradé, sans challengers).

FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance

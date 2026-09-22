# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

Fichier HTML unique, autonome (HTML/CSS/JS sans framework, sans serveur), ouvert par double-clic dans le navigateur (Chrome, Edge). Fonctionne hors ligne. Choix confirmé par l'utilisateur (« Fichier à ouvrir »).

## Users

Un seul utilisateur : l'expert-comptable (ou son assistant) d'ALTHO EXPERTISE qui prépare, une fois par an, la campagne de révision des honoraires. Il n'est pas technicien : il connaît Excel et l'impression, pas les outils de développement. Il travaille à son bureau, sur ordinateur, avec une imprimante et des enveloppes à fenêtre.

## Product Purpose

Produire en une séance les courriers de révision tarifaire de tous les clients du cabinet (missions comptabilité, paye, juridique, plateforme agréée de facturation électronique) : saisir ou importer les clients et leurs honoraires actuels, appliquer les taux d'augmentation, relire, puis imprimer tous les courriers d'un coup ou les exporter en PDF. Réussite : la campagne est bouclée en une matinée, chaque lettre est juste (montants, civilité, adresse) et présentable.

## Positioning

Remplace le classeur Excel de publipostage du même projet (`Courrier_augmentation_tarifaire.xlsx`), jugé trop technique. L'outil fait une seule chose : la campagne annuelle d'augmentation d'honoraires d'un cabinet comptable, du tableau des clients à la pile de lettres imprimées.

## Operating Context

- Données clients importées depuis Excel/CSV (export du logiciel de production ou de l'ancien classeur), puis corrigées à la main.
- Impression papier A4 portrait, adresse destinataire positionnée pour enveloppe à fenêtre (DL/C5, fenêtre à droite), et export PDF via la boîte d'impression du navigateur.
- Certains clients reçoivent le courrier par e-mail (PDF), d'autres par la poste.
- Données stockées localement dans le navigateur de l'utilisateur ; sauvegarde/restauration par fichier.

## Capabilities and Constraints

- Paramètres : coordonnées du cabinet, signataire, date du courrier, date d'effet, taux par mission, arrondi, nombre d'échéances, TVA, textes du courrier modifiables avec balises.
- Clients : code, civilité, prénom, nom, société, adresse (2 lignes), CP, ville, e-mail, honoraires annuels HT actuels par mission, taux personnalisé facultatif, à envoyer (oui/non), mode d'envoi (courrier / e-mail / les deux).
- Calculs : nouveau montant = actuel × (1 + taux), arrondi au pas choisi (au-dessus) ; totaux, écarts, mensualité HT/TTC.
- Courrier : 1 page A4, seules les missions souscrites apparaissent.
- Impression en masse de la sélection, une lettre par page.
- Aucune donnée ne quitte l'ordinateur. Pas de compte, pas de serveur.

## Brand Commitments

ALTHO EXPERTISE — SAS au capital de 10 000 €, RCS Pontoise 919 706 325, TVA FR62919706325, 141 rue Charles de Gaulle, 95130 Le Plessis-Bouchard, Tél. 01 34 14 53 45, altho@altho-experts.com, altho-experts.com (source : registre du commerce via Pappers). Aucun logo ni charte graphique fourni.

## Evidence on Hand

- Textes du courrier et règles de calcul validés dans `generer_courrier.py` / `Courrier_augmentation_tarifaire.xlsx`.
- Aucun client réel fourni : les clients d'exemple sont fictifs et doivent être signalés comme tels.
- À confirmer par l'utilisateur : nom et fonction du signataire, intitulé exact de l'inscription à l'Ordre.

## Product Principles

1. Le courrier imprimé est le produit : ce qui sort de l'imprimante doit être irréprochable.
2. Zéro jargon : chaque écran parle comme un cabinet comptable, pas comme un logiciel.
3. Vérifier avant d'envoyer : les montants et la sélection sont visibles d'un coup d'œil avant l'impression.
4. Les données restent chez le cabinet.

## Accessibility & Inclusion

Utilisateur non technicien : libellés explicites en français, actions nommées par leur résultat, contrastes lisibles, utilisable au clavier.

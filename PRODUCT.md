# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

Fichier HTML unique, autonome (HTML/CSS/JS sans framework, sans serveur), ouvert par double-clic dans le navigateur (Chrome, Edge). Fonctionne hors ligne. Choix confirmé par l'utilisateur (« Fichier à ouvrir »).

## Users

Un seul utilisateur : l'expert-comptable (ou son assistant) d'ALTHO EXPERTISE qui prépare, une fois par an, la campagne de révision des honoraires. Il n'est pas technicien : il connaît Excel et l'impression, pas les outils de développement. Il travaille à son bureau, sur ordinateur, avec une imprimante et des enveloppes à fenêtre.

## Product Purpose

Produire en une séance les courriers de révision tarifaire de tous les clients du cabinet (missions comptabilité, paye, juridique, plateforme agréée de facturation électronique) : saisir ou importer les clients et leurs nouveaux honoraires, relire, puis imprimer tous les courriers d'un coup ou les exporter en PDF. Réussite : la campagne est bouclée en une matinée, chaque lettre est juste (montants, civilité, adresse) et présentable.

## Positioning

Remplace le classeur Excel de publipostage du même projet (`Courrier_augmentation_tarifaire.xlsx`), jugé trop technique. L'outil fait une seule chose : la campagne annuelle d'augmentation d'honoraires d'un cabinet comptable, du tableau des clients à la pile de lettres imprimées.

## Operating Context

- Données clients importées depuis le modèle Excel fourni (`Modele_import_clients.xlsx`, téléchargeable aussi depuis l'application), puis corrigées à la main.
- Impression papier A4 portrait, adresse destinataire positionnée pour enveloppe à fenêtre (DL/C5, fenêtre à droite), et export PDF via la boîte d'impression du navigateur.
- Certains clients reçoivent le courrier par e-mail (PDF), d'autres par la poste.
- Données stockées localement dans le navigateur de l'utilisateur ; sauvegarde/restauration par fichier.

## Capabilities and Constraints

- Paramètres : nom du cabinet et ville de signature, signataire, date du courrier, date d'effet, périodicité de facturation par défaut (mensuelle, trimestrielle, semestrielle, annuelle), TVA, intitulés des missions, textes du courrier modifiables avec balises.
- Clients : code, civilité, prénom, nom, société, adresse (2 lignes), CP, ville, e-mail, nouveaux honoraires annuels HT par mission, périodicité propre (facultative), à envoyer (oui/non), mode d'envoi (courrier / e-mail / les deux).
- Montants : on importe les honoraires ACTUELS (format du fichier « liste clients et hono » du cabinet : Société / Nom, Nom, Adresse, Code postal, Ville, Clôture, Récurrence, Honoraires 2026, Bilan 2026, Juridique, Prix bulletin, LM AE, ECF, Informations complémentaires). Nouveau montant = actuel + augmentation générale (x %, Réglages, arrondi réglable), chaque case « nouveau » pouvant être saisie à la main. La lettre n'affiche que les nouveaux montants, ligne par prestation (Prestations comptables {récurrence}, Gestion de la paie par bulletin, Facturation annuelle du bilan, Juridique – approbation des comptes, Plateforme agréée), sans total. Toute suppression demande une confirmation.
- Courrier : 1 page A4, seules les missions souscrites apparaissent.
- Impression en masse de la sélection, une lettre par page.
- Aucune donnée ne quitte l'ordinateur. Pas de compte, pas de serveur.

## Brand Commitments

ALTHO EXPERTISE — SAS au capital de 10 000 €, RCS Pontoise 919 706 325, TVA FR62919706325, 141 rue Charles de Gaulle, 95130 Le Plessis-Bouchard, Tél. 01 34 14 53 45, altho@altho-experts.com, altho-experts.com (source : registre du commerce via Pappers).

Identité visuelle fournie par le cabinet : logo « AE | ALTHO EXPERTISE » et papier à en-tête (`Papier_en_t_te_definitif.docx`), couleur bordeaux #9D202E et noir. L'en-tête et le pied de page de la lettre sont les images de ce papier à en-tête, reprises telles quelles (fichiers dans `app/assets/`). E-mail du pied de page officiel : ae@altho-expertise.com.

## Evidence on Hand

- Courrier de décembre 2024 fourni (`courrier_augmentation.docx`, publipostage Word, signé ERIC PAYET, Expert-comptable) : textes par défaut repris de ce courrier.
- Fichier réel des clients et honoraires 2026 fourni par l'utilisateur (63 clients) : données confidentielles, jamais versées dans le dépôt.
- Aucun client réel fourni : les clients d'exemple sont fictifs et doivent être signalés comme tels.
- Signataire : ERIC PAYET, Expert-comptable (courrier 2024).

## Product Principles

1. Le courrier imprimé est le produit : ce qui sort de l'imprimante doit être irréprochable.
2. Zéro jargon : chaque écran parle comme un cabinet comptable, pas comme un logiciel.
3. Vérifier avant d'envoyer : les montants et la sélection sont visibles d'un coup d'œil avant l'impression.
4. Les données restent chez le cabinet.

## Accessibility & Inclusion

Utilisateur non technicien : libellés explicites en français, actions nommées par leur résultat, contrastes lisibles, utilisable au clavier.

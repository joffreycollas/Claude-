# ALTHO EXPERTISE — Courrier d'augmentation tarifaire (publipostage Excel)

Missions couvertes : comptabilité · paye · juridique · plateforme agréée (facturation électronique).

| Fichier | Rôle |
|---|---|
| `Courrier_augmentation_tarifaire.xlsx` | Le classeur à utiliser |
| `Module_Courriers.bas` | Macro VBA pour exporter/imprimer tous les courriers d'un coup |
| `Exemple_courrier_C001.pdf` | Exemple de courrier généré |
| `Exemple_impression_en_masse.pdf` | Exemple d'impression en masse (2 clients) |
| `generer_courrier.py` | Script qui régénère le classeur (facultatif) |

## Utilisation
1. **Paramètres** : coordonnées du cabinet, signataire, date d'effet, taux par mission, textes.
2. **Clients** : une ligne par client, honoraires annuels HT actuels par mission (0 = mission non souscrite, elle n'apparaît pas dans le courrier).
3. **Courrier** : choisir le code client en cellule jaune `I3` → Fichier > Exporter > PDF, ou Imprimer.
4. **Impression en masse (sans macro)** : onglet `Impression en masse` → Fichier > Imprimer (ou Exporter > PDF). Tous les clients « À envoyer = Oui » (mode Courrier / Les deux par défaut) sortent à la suite, 1 page chacun. Jusqu'à 300 courriers.
5. **Un PDF par client (facultatif)** : enregistrer en `.xlsm`, importer `Module_Courriers.bas` (Alt+F11 > Fichier > Importer), puis lancer `ExporterTousLesPDF`, `ExporterUnSeulPDF` ou `ImprimerCourriersPostaux` (Alt+F8).

---

# Comparateur SCI à l'IR ou à l'IS

`Comparateur_SCI_IR_IS.html` : fichier autonome, à ouvrir par double-clic dans Chrome ou Edge. Fonctionne hors ligne, aucune donnée ne quitte l'ordinateur (la dernière saisie est gardée dans le navigateur).

Compare, de l'acquisition à la revente, ce que la SCI laisse aux associés selon le régime :

- **IR** : revenus fonciers au réel (barème + prélèvements sociaux, CSG déductible), déficit foncier imputé sur le revenu global puis reporté 10 ans, plus-value des particuliers (forfaits 7,5 % et 15 %, abattements pour durée de détention, surtaxe au-delà de 50 000 € par associé).
- **IS** : amortissements (terrain exclu), taux réduit 15 % jusqu'à 42 500 €, déficits reportables, plus-value sur valeur nette comptable, dividendes au PFU (31,4 % en 2026), distribution annuelle et sortie des réserves à la revente.

Résultat : rapport de 3 pages aux couleurs d'**ALTHO EXPERTISE** ou d'**ALTHO** (bouton en haut), à imprimer ou enregistrer en PDF. Taux 2026 modifiables dans « Taux appliqués ».

| Fichier | Rôle |
|---|---|
| `comparateur-sci/moteur.js` | Moteur de calcul (sans interface, testable avec Node) |
| `comparateur-sci/index.src.html` | Interface et rapport |
| `comparateur-sci/build.py` | Assemble `Comparateur_SCI_IR_IS.html` (moteur, polices et papier à en-tête embarqués) |

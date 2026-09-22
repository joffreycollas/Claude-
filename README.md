# Courrier d'augmentation tarifaire — publipostage Excel

Missions couvertes : comptabilité · paye · juridique · plateforme agréée (facturation électronique).

| Fichier | Rôle |
|---|---|
| `Courrier_augmentation_tarifaire.xlsx` | Le classeur à utiliser |
| `Module_Courriers.bas` | Macro VBA pour exporter/imprimer tous les courriers d'un coup |
| `Exemple_courrier_C002.pdf` | Exemple de courrier généré |
| `generer_courrier.py` | Script qui régénère le classeur (facultatif) |

## Utilisation
1. **Paramètres** : coordonnées du cabinet, signataire, date d'effet, taux par mission, textes.
2. **Clients** : une ligne par client, honoraires annuels HT actuels par mission (0 = mission non souscrite, elle n'apparaît pas dans le courrier).
3. **Courrier** : choisir le code client en cellule jaune `I3` → Fichier > Exporter > PDF, ou Imprimer.
4. **Envoi en masse** : enregistrer en `.xlsm`, importer `Module_Courriers.bas` (Alt+F11 > Fichier > Importer), puis lancer `ExporterTousLesPDF`, `ExporterUnSeulPDF` ou `ImprimerCourriersPostaux` (Alt+F8).

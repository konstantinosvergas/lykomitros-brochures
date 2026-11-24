# Lykomitros Steel – σελίδες φυλλαδίων

Μία σελίδα ανά φυλλάδιο, δημοσιευμένη δωρεάν με GitHub Pages:
`https://konstantinosvergas.github.io/lykomitros-brochures/<όνομα>/`

| Φυλλάδιο | Σελίδα |
|---|---|
| Company Profile | `/company-profile/` |
| Oil & Gas | `/oil-gas/` |
| Offshore Wind | `/offshore-wind/` |
| Energy & Electrical Infrastructure | `/energy-electrical-infrastructure/` |
| Bridges | `/bridges/` |
| Glass Roofs & Buildings | `/glass-roofs-buildings/` |
| Defence & Naval Industries | `/defence-naval-industries/` |
| Industrial & Energy | `/industrial-energy/` |
| Capabilities Brochure | `/capabilities-brochure/` |

## Πώς ενημερώνονται τα PDF

Πηγή είναι ο τοπικός φάκελος φυλλαδίων δίπλα στο Excel. Το κουμπί της μακροεντολής ανεβάζει
όσα PDF άλλαξαν στον φάκελο `pdf/` αυτού του repo ως `<slug>.pdf` (π.χ. `oil-gas.pdf`).
Κάθε ανέβασμα ξαναχτίζει αυτόματα τις σελίδες (περίπου 1 λεπτό).

- Αν λείπει κάποιο PDF από το `pdf/`, η σελίδα του παίρνει το τρέχον PDF από το lykomitros-steel.gr.
- Το «Download PDF» κατεβάζει το ίδιο αρχείο που δείχνει η σελίδα.
- Το lykomitros-steel.gr δεν επιτρέπει να εμφανίζονται τα PDF του μέσα σε άλλη σελίδα, γι' αυτό τα PDF φιλοξενούνται εδώ και εμφανίζονται με το PDF.js (δουλεύει και σε κινητά).
- Το μακροεντολή χρειάζεται ένα fine-grained token με πρόσβαση μόνο σε αυτό το repo (Contents: Read and write).

## Αρχεία

- `brochures.json` – λίστα φυλλαδίων (τίτλος, κείμενο, όνομα PDF, σχετική σελίδα του site)
- `tools/build.py` – φτιάχνει τις σελίδες · `tools/fetch_pdfs.py` – κατεβάζει τα PDF
- `assets/` – εμφάνιση, viewer, PDF.js 3.11.174 (Apache-2.0)

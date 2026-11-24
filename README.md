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

Το lykomitros-steel.gr δεν επιτρέπει σε άλλα sites να δείχνουν τα PDF του μέσα σε πλαίσιο
(`X-Frame-Options: SAMEORIGIN`, `frame-ancestors 'self'`). Γι' αυτό το GitHub κατεβάζει τα PDF
από το site και τα δείχνει με το PDF.js (δουλεύει και σε κινητά):

- **Αυτόματα κάθε μέρα** στις 06:15/07:15 ώρα Ελλάδας.
- **Αμέσως**, αν αλλάξετε ένα PDF: Actions → «Build and publish brochure pages» → Run workflow.

Το κουμπί «Download PDF» ανοίγει πάντα το αρχείο απευθείας από το site.
Αν αλλάξει το όνομα ενός PDF στο site (π.χ. `-2027.pdf`), αλλάζει μόνο η γραμμή του στο `brochures.json`.

Σημείωση: το GitHub παγώνει τις καθημερινές εκτελέσεις αν το repo μείνει 60 μέρες χωρίς αλλαγή·
τότε αρκεί ένα πάτημα στο «Enable workflow» ή στο «Run workflow».

## Αρχεία

- `brochures.json` – λίστα φυλλαδίων (τίτλος, κείμενο, όνομα PDF, σχετική σελίδα του site)
- `tools/build.py` – φτιάχνει τις σελίδες · `tools/fetch_pdfs.py` – κατεβάζει τα PDF
- `assets/` – εμφάνιση, viewer, PDF.js 3.11.174 (Apache-2.0)

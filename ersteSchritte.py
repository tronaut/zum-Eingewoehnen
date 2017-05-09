


# Mein erstes Programm!
print("hello " + "world")

# Frei nach Pieter Spronk
buch_preis = 24.95
rabatt = 40 # in Prozent
versand_erstes_buch = 3
versand_weitere = 0.75
anzahl_bücher = 60

kosten_bücher = (buch_preis
                 * anzahl_bücher)
                 * (100 - rabatt)
                 / 100
kosten_versand = versand_erstes_buch
                 + (anzahl_bücher - 1)
                 * versand_weitere
gesamt_kosten = kosten_bücher
                + kosten_versand
print("Die Bestellung kostet:", gesamt_kosten, "€")
# noch ein Kommentar

"""status: ferdig"""

def meditate(mana, max_mana, num_potions):
    potions_left = num_potions              #lagte en ny variabel fordi eg trengte å holde tellinga på kor mange potions var igjen uten å endre rangen til for loopen
    for n in range(num_potions):
        if mana < max_mana:                 #det andre kravet til oppgaven var å stoppe hvis manaen var lik som max_mana
            mana += 1
            potions_left -= 1
    return mana, potions_left



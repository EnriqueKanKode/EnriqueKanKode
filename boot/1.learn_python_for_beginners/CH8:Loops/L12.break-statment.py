"""status: løst"""

#break gjør at for-loopen stopper helt
#her ville boot at når et enchantment var sterkere enn et angrep så skulle man printe "Attack blocked!"
#og man skulle stoppe å sammenligne fordi vi då viste at sterkere enchantments ville blokkere angrepet også
def check_defense(attack_strength, min_enchantment, max_enchantment):
    for enchantment_strength in range(min_enchantment, max_enchantment + 1):
        print(
            f"Comparing attack strength {attack_strength} to enchantment strength {enchantment_strength}."
        )

        if enchantment_strength >= attack_strength:
            print("Attack blocked!")
            #Dette var løsningen til oppgaven XD
            break


# Don't touch below this line


def test(attack_strength, min_enchantment, max_enchantment):
    print(
        f"Testing attack strength {attack_strength} vs. enchantment strengths {min_enchantment}–{max_enchantment}:"
    )
    check_defense(attack_strength, min_enchantment, max_enchantment)
    print("========================================")


def main():
    test(5, 8, 12)
    test(8, 6, 10)
    test(10, 5, 8)
    test(7, 4, 7)


main()

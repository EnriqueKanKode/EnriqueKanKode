#først så prøve jeg å løse uten en loop (fordi jeg glømte at det fantes og at kapitelet er om loops)
#det går sikkert an å lage en funskjon uten loops for å løse det
#men klarte å løse oppgaven med trial and error men jeg skal prøve å forklare hva funksjonen gjør

#har også noen notater/ rabbel skrevet på batman notatblokk, se det for å få full kontekst

def calculate_experience_points(level):
    xp_so_far = 0                           #Definerer xp_so_far
    xp_for_next_level = 0                   #Definerer xp_for_next_level
    for x in range(level - 1):              #operasjonen må bli gjentatt for hvert level så det er perf for en loop, "level -1" er siden den inkluderer start nivået, men man trenger bare nivåene mellom start og slutt nivå
        xp_for_next_level += 5              #hoppet mellom xp-en som trengs for å gå til neste level øker med 5 hver gang så jeg skrev det bokstaveligt ned
        xp_so_far += xp_for_next_level      #og for å gå opp i nivå så trenger man xp antallet: "xp_for_next_level" for å gå opp i level 
    return xp_so_far                        #når loppen har kjørt ferdig så har total mengden xp trengt for å nå nivået ønsket regnet ut i xp_so_far




from random import randint

# Naključno število med 0 in 9
random_number = randint(0, 9)

# Število poizkusov:
st_poizkusov = 0

# Zanka
while st_poizkusov < 5:
    
    # User input:
    uporabnik = int(input("V mislih imam število med 0 in 9. Poizkusi svojo srečo:  "))

    #povečujemo število poizkusov
    st_poizkusov = st_poizkusov + 1

    # pogoji
    if random_number < uporabnik:
        print("Narobe, poizkusi z nižjo številko!") 
    elif random_number > uporabnik:
        print("Narobe, poizkusi z višjo številko!")
    else:
        break


# Zmaga
if random_number == uporabnik:
    st_poizkusov = str(st_poizkusov)
    print("Bravo zmagal si in to kar v " + st_poizkusov + " poizkusu")

# Poraz
if random_number != uporabnik:
    print("Skoda več sreče prihodnjič!")

    

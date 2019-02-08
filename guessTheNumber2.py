from random import randint


# Naključno število med 0 in poljubno izbrano številko:
def random_number(number):
    x = randint(0, number)
    return x

#print(random_number(5))

uporabnik_razpon = int(input("Vnesi cifro razpona: "))

game_number = random_number(uporabnik_razpon)


def main():

    # Število poizkusov:
    st_poizkusov = 0
    
    # Zanka
    while st_poizkusov < 5:
        
        # User input:
        uporabnik = int(input(f"V mislih imam število med 0 in {uporabnik_razpon}. Poizkusi svojo srečo:  "))

        #povečujemo število poizkusov
        st_poizkusov = st_poizkusov + 1

        # pogoji
        if game_number < uporabnik:
            print("Narobe, poizkusi z nižjo številko!") 
        elif game_number > uporabnik:
            print("Narobe, poizkusi z višjo številko!")
        else:
            break


    # Zmaga
    if game_number == uporabnik:
        st_poizkusov = str(st_poizkusov)
        print(f"Bravo zmagal si in to kar v {st_poizkusov} poizkusu")

    # Poraz
    if game_number != uporabnik:
        print("Skoda več sreče prihodnjič!")

if __name__ == "__main__":  # this means that if somebody ran this Python file, execute only the code below
    main()
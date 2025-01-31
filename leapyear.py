#scrivere codice python per calcolare gli anni bisestili nel calendario gregoriano

n = int(input("Inserire anno per vederne la bisestilità: "))

if n > 0 and n % 4 == 0 and not n % 100 == 0:

    print("l'anno è bisestile")

elif n > 0 and n % 100 == 0:

    if n % 400 == 0:

        print("l'anno è bisestile")

    else:

        print("l'anno non è bisestile")

else:

    print("l'anno non è bisestile")

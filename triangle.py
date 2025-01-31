#determinare se un triangolo è equilatero, ioscele o scaleno

a = int(input("Lato a del triangolo: "))

b = int(input("Lato b del triangolo: "))

c = int(input("Lato c del triangolo: "))

if a > 0 and b > 0 and c > 0:

    if a + b >= c and a + c >= b and b + c >= a:

        if a == b == c:

            print("il triangolo è equilatero")
        
        elif a == b or a == c or b == c:

            print("Il triangolo è isoscele")

        else:

            print("il triangolo è scaleno")

    else:

        print("error")

else:

    print("Uagliù chill nun è un triangolo")
    

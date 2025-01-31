#calcolare numero di grano su di una scacchiera. Il grano raddoppia ad ogli casella

chess_square = 64
grain_sum = 0

for i in range(1, chess_square + 1):

    n = 2 ** (i - 1)

    grain_sum = grain_sum + n

    

    print("La casella è: ", i ,"il grano su quella casella è: ", n)

print("La somma di tutto il grano è: ", grain_sum)





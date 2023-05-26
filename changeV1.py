def change_machine(change, coins):

    change_list = []
    i = 0

    if change >= 0:
        while True:
            if change - coins[i] >= 0:
                change -= coins[i]
                change_list.append(coins[i])

            if change == 0:
                return change_list
            
            if change - coins[i] >= 0:
                pass
            else:
                i += 1
            
change = int(input("Reszta do wydania: "))

coins = [50, 20, 10, 5, 2, 1]
coins_2 = [5, 1]

print(change_machine(change, coins_2))
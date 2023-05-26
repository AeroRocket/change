def change_return(change, coins):
    change_backup = change

    change_options = []
    for i in range(len(coins)-1):
        change = change_backup

        if i > 0:
            coins.pop(0)
        change_list = []
        i = 0

        if change >= 0:
            while True:
                if change - coins[i] >= 0:
                    change -= coins[i]
                    change_list.append(coins[i])

                if change == 0:
                    change_options.append(change_list)
                    break
                
                if change - coins[i] >= 0:
                    pass
                else:
                    i += 1

    min_index = 0
    for x in range(1, len(change_options)):
        if len(change_options[x]) < len(change_options[min_index]):
            min_index = x

    return change_options[min_index]

coins = [6, 4, 1]
change = int(input())

print(change_return(change, coins))
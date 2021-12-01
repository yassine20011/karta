def list_from_1_13_card():
    list = []
    types = ["spade","heart", "diamond","club"]
    for symbole in types:
        for i in range(1, 14):
            list.append([i,symbole])
    #print(list)
    return list

list_from_1_13_card()
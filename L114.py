#Lab11
#Author: Vincenza Paradiso and Saerin Bong
red_velvet ={"milk":1, "egg":2, "sugar":4, "chocolate":2.4, "flour": 1.5}
lemon = {"milk": 2, "salt": 5, "flour": 3, "baking powder": 1.5, "egg": 4}

def similar(g):
    v=red_velvet
    l=lemon
    if g in v:
        if g in l:
            print(g, "is in both cakes.")
        else:
            print(g, "is not in both cakes.")
    else:
        print(g, "is in the lemon cake.")


similar("milk")
similar("baking powder")

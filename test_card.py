import random
from card import Carte


def random_card_Nbr():
    types = ["PIQUE","COEUR","CARREAU","TREFLE"]
    nums = [i for i in range(1,14)]
    t = random.choice(types)
    n = random.choice(nums)
    c = Carte(n,t)
   
    return [n,t]



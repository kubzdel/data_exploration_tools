import math


def general_balance(bid, budget, spent):
    return bid * (1 - math.exp(-(1 - (spent / budget))))


bid = 2
budget = 2000
spent = 1000

print(general_balance(bid, budget, spent))


# https://www.algoexpert.io/questions/Non-Constructible%20Change
def nonConstructibleChange(coins):
    coins.sort() # Sorting array
    minCoin = 0 # Creating variable which will be the smallest coin, set to 0
    for i in coins: # Traverse through the coins
        if i > minCoin + 1: # Seeing if the element of coins is smaller than our min coin value + 1
            return minCoin + 1 # If smaller, we return the minCoin + 1 as that would be our smallest value
        minCoin += i # if not we increase our smallest coin value by the i value
    return minCoin + 1

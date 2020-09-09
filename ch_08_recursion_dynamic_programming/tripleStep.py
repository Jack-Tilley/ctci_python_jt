memo = {1 : 1, 2:2, 3: 4}
def tripleStep(n, memo): # n is number of steps
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif n in memo:
        return memo[n]
    else:
        memo[n] = tripleStep(n -1, memo) + tripleStep(n - 2, memo) + tripleStep(n - 3, memo)
        return memo[n]
    



print(tripleStep(4, memo))
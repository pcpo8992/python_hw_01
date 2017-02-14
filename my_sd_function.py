import math

def getSD(x, n):
    
    def getSum(x):
        x_sum = 0
        for xi in x:
            x_sum += xi
        return x_sum

    def getAvg(x, n):
        return getSum(x) / n

    Variance = 0
    
    for xi in x:
        Variance += math.pow(xi - getAvg(x, n), 2)

    return math.sqrt(Variance / n)
        
x = [1, 2, 3, 4, 5]

print(str(getSD(x, len(x))))

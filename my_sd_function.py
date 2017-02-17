import math

def GetSD(x):
    
    def GetSum(x):
        x_sum = 0
        for xi in x:
            x_sum += xi
        return x_sum

    def GetAvg(x):
        return GetSum(x) / len(x)

    Variance = 0
    
    for xi in x:
        Variance += math.pow( (xi - GetAvg(x)), 2)

    return math.sqrt(Variance / len(x))

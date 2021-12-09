def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += abs(x[i] - y[i])
    return res

def jaccard_dist(x, y):
    numerator = set(y).intersection(x)
    denominator = set(y).union(x)
    res = 1 - (numerator/denominator)
    return res

def cosine_sim(x, y):
    nx = 0
    ny = 0
    numerator = 0
    for i in range(len(x)):
        nx += x[i] ** 2
        ny += y[i] ** 2
        numerator += x[i]*y[i]
    denominator = (nx ** 0.5) * (ny ** 0.5)
    res = numerator/denominator
    return res

# Feel free to add more

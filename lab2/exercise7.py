import random
def iterate():
    n = 1000000
    k = 0
    for i in range(0,n):
        t = 0
        for b in range (0,1024):
            u = random.random()
            if(u < 0.005):
                t = t + 1
        if(t<=3):
            k=k+1
    print(k/n)
iterate()

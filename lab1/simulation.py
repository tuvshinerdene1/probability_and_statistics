import random
def event(p):
    num = random.random()
    if(num<p):
        return True
    else:
        return False
def iterate(p, count):
    sum = 0
    for i in range(0, count):
        if(event(p)):
            sum += 1/count
    print(sum)
iterate(0.6969, 10000000)

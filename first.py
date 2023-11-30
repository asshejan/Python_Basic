def doubly(*args):
    sum = 0
    for num in args:
        sum += num
    return sum


res = doubly(17, 32, 33, 10, 20, 30) 
print(res)
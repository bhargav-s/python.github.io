def numbers(*args):
    total = 1
    for a in args:
        total += a
    print(total)

numbers(5,7,8,4,3,7,1,2)
numbers(4)
numbers(9,10,11,12,13,14)
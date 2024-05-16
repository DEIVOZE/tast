from random import randint, shuffle


def gen_lvl1_module1():
    x = randint(-10, 10)
    print(x)
    n = [randint(-10, 10) for i in range(randint(1, 4))]
    res = n + [sum(n) + x, 'x']
    shuffle(res)
    strr = f"{res[0]}{''.join(map(lambda x: '+' + str(x) if type(x) == int and x >= 0 else str(x), res[1:]))}"
    return strr


print(gen_lvl1_module1())
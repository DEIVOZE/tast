from random import randint, shuffle


def gen_lvl1(k=1, b=0):
    if k != 1:
        k = randint(-10, 10)
        while k == 0 or k == 1:
            k = randint(-10, 10)
    x = randint(-10, 10)
    if b:
        b = randint(-10, 10)
        while b == 0:
            b = randint(-10, 10)
    if b:
        return f'{k if k != 1 else ""}x {"- " + str(abs(b)) if b <= 0 else "+ " + str(b)} = {k * x + b}', x
    else:
        return f'{k if k != 1 else ""}x = {k * x}', x


def lvl2_module1():
    x1, x2 = randint(-10, 10), randint(-10, 10)

    a = randint(-10, 10)
    while a == 0:
        a = randint(-10, 10)
    b = -a * (x1 + x2)
    c = a * (x1 * x2)
    return (f'{a}x²{"+" + str(b) if b > 0 else "-" + str(-b) if b != 0 else ""}x'
            f'{"+" + str(c) if c > 0 else "-" + str(-c) if c != 0 else ""} = 0')


print(lvl2_module1())
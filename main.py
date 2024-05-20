from random import randint, choice, shuffle


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


def gen_lvl2_module2(c=0):
    if c:
        x1, x2 = randint(-10, 10), randint(-10, 10)
        while x1 == x2:
            x1, x2 = randint(-10, 10), randint(-10, 10)
    else:
        x1, x2 = 0, randint(-10, 10)
        while x1 == x2:
            x2 = randint(-10, 10)

    a = randint(-3, 3)
    while a == 0:
        a = randint(-3, 3)
    b = -a * (x1 + x2)
    c = a * (x1 * x2)
    return (
        f'{"" if a > 0 else "-" if abs(a) == 1 else a}x²{"+" + str(b) if b > 0 else "-" + str(-b) if b != 0 else "+"}x'
        f'{"+" + str(c) if c > 0 else "-" + str(-c) if c != 0 else ""}=0'), (x1, x2)


def gen_lvl2_module1():
    x = randint(1, 10)
    if choice([True, False]):
        return f'x²-{x ** 2}=0', (x, -x)
    else:
        g = randint(-(x ** 2), x ** 2)
        while g == 0 or g == x ** 2:
            g = randint(-(x ** 2), x ** 2)
        r = [g, x ** 2 - g]
        shuffle(r)
        return f'x²{-r[0] if -r[0] < 0 else "+" + str(-r[0])}={r[1]}', (x, -x)


print(gen_lvl2_module2())

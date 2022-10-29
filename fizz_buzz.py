def gen_fizz():
    i = 1
    while True:
        if i % 3 == 0 and i % 5 == 0:
            yield "Fizz Buzz"
        elif i % 3 == 0:
            yield "Fizz"
        elif i % 5 == 0:
            yield "Buzz"
        else:
            yield str(i)
        i += 1

g = gen_fizz()
num_gamers = 5
k = 1
for i in range(30):
    if k < num_gamers:
        print(f"{k} {next(g)}")
        k += 1
    elif k == num_gamers:
        print(f"{k} {next(g)}")
        k = 1

import random
import matplotlib.pyplot as plt
matplotlist = []
rangetop = []
rangelow = []
guessed = False
x = []
a = 0
starting = True
gues = 1
down = 0
up = 100
print("Welcome to game!")


def cheated():
    count = 0
    while True:
        print("fuck you")
        print("cheater")
        count += 1
        if count >= 10:
            quit("cheated")


def sqrt(i):
    i2 = i ** 1/2
    return i2


def guess(hi, lo):
    num = sqrt(hi - lo)
    if (num ** 2) < 10:
        new_guess = random.randint(lo, hi)
    else:
        new_guess = (hi + lo) / 2
    return new_guess


def check_in(inp):
    if inp == "high":
        pass
    elif inp == "low":
        pass
    elif inp == "yes":
        pass
    else:
        print("no")


def update_range(inp, hi, lo, ges):
    if inp == "high":
        hi = ges
    elif inp == "low":
        lo = ges
    return hi, lo


while not guessed:
    if starting:
        gues = random.randint(25, 75)
        starting = False
    else:
        gues = round(guess(up, down))
    if (sqrt(up - down) ** 2) <= 0:
        print("fucking cheater")
        cheated()
    print("my guess is " + str(gues))
    print("if this is too high type 'high' if low type 'low'")
    hilo = input("> ")
    if hilo == "yes":
        guessed = True
    check_in(hilo)
    up, down = update_range(hilo, up, down, gues)
    a += 1
    matplotlist.append(gues)
    rangetop.append(up)
    rangelow.append(down)
    x.append(a)
print("BAM! I got it!")
print("Your guess was: " + str(gues))
print("I got it in " + str(a) + " guesses")
plt.plot(x, rangelow)
plt.plot(x, rangetop)
plt.plot(x, matplotlist)
plt.show()

high = ["high", "hi", "h"]
low = ["low", "lo", "l"]
yes = ["yes", "mhm", "ok", "alrighy", "omg yes", "y", "yeah"]
guessed = False
a = 0
starting = True
gues = 1
down = 0
up = 100
print("")
print("Welcome to my number guessing game!")
print("By: 11111010111")
print("")


def cheated():
    count = 0
    while True:
        print("stupid")
        print("cheater")
        count += 1
        if count >= 50:
            quit("cheated")


def sqrt(i):
    i2 = i ** 1/2
    return i2


def guess(hi, lo):
    new_guess = (hi + lo) / 2
    return new_guess


def check_in(inp):
    if inp in high:
        return True
    elif inp in low:
        return True
    elif inp in yes:
        return True
    else:
        print("no")
        return False


def update_range(inp, hi, lo, ges):
    if inp in high:
        hi = ges
    elif inp in low:
        lo = ges
    return hi, lo


while not guessed:
    if starting:
        gues = round(guess(up, down))
        starting = False
    else:
        gues = round(guess(up, down))
    if up - down <= 0:
        print("no cheating, cheater")
        cheated()
    print("My guess is " + str(gues))
    print("If this is too high type 'high' if low type 'low'")
    hilo = input("> ")
    if hilo in yes:
        guessed = True
    if check_in(hilo):
        up, down = update_range(hilo, up, down, gues)
        a += 1
    else:
        print("please use 'high', 'low' or 'yes'")
print("BAM! I got it!")
print("Your number was: " + str(gues))
print("I got it in " + str(a) + " guesses")

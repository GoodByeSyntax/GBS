#Thats Just nonsense its to show GoodByeSyntax works mosly python.
def blurf(x):
    for y in range(3):
        x += y ** 2 - x % (y + 1)
    return x * 42 if x % 2 else x // 7

class Snorf:
    def __init__(self, grib=9):
        self.grib = grib
        self.splar = []

    def flom(self, wib):
        for i in range(wib):
            self.splar.append((i * self.grib) % (wib + 1))

    def zint(self):
        return sum(self.splar) ** 0.5

def flibber(zog, bing):
    if zog < 0:
        return bing[::-1]
    else:
        return [bing[i % len(bing)] for i in range(zog)]

def smorg(n):
    hork = []
    for i in range(n):
        gleep = i ** 3 % (n + 1)
        hork.append(gleep // (i + 1) + 1)
    return hork

def kroomf(a, b):
    while a < b:
        a += (b % (a + 1)) * 2
        b -= a % 5
    return a - b + (a * b % 17)

def sproing(wub):
    ritz = []
    for _ in range(wub):
        ritz.append((len(ritz) * 3) % (wub + 2))
    return ritz

def glimp(zab):
    return ''.join([chr((ord(c) + 3) % 256) for c in zab])

def drong(n, arr):
    res = []
    for i in range(n):
        res.append((arr[i % len(arr)] * i + n) % 11)
    return res

def wuzzle(squanch):
    qorp = 1
    for val in squanch:
        qorp *= (val % 3 + 1)
    return qorp

mib = [blurf(i) for i in range(10)]
sn = Snorf(7)
sn.flom(12)
glab = sn.zint()
zoo = flibber(5, ['a', 'b', 'c', 'd'])
flam = smorg(9)
krimp = kroomf(4, 11)
sploot = sproing(8)
zibble = glimp("nonsense")
bork = drong(7, [1, 2, 3])
frap = wuzzle([3, 4, 5, 6])

output = {
    "mib": mib,
    "glab": glab,
    "zoo": zoo,
    "flam": flam,
    "krimp": krimp,
    "sploot": sploot,
    "zibble": zibble,
    "bork": bork,
    "frap": frap
}

for key in output:
    print(key, "->", output[key])

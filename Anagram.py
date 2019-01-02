from collections import defaultdict
pokes = [x.strip() for x in pokes.split(",")]
def unscramble(anagram, wordbank):
    l = []
    for poke in wordbank:
        d = defaultdict(int)
        for c in anagram.lower().replace(" ", ""):
            d[c] += 1
        check = True
        for c in poke:
            d[c] -= 1
            if d[c] < 0:
                check = False
                break
        if check:
            l.append(poke)
    for poke in l:
        d = defaultdict(int)
        master = defaultdict(int)
        for c in anagram.lower().replace(" ", ""):
            d[c] += 1
            master[c] += 1
        for c in poke:
            d[c] -= 1
            master[c] -= 1
        for p in l:
            check = True
            for c in p:
                d[c] -= 1
                if d[c] < 0:
                    check = False
                    break
            if check:
                check2 = True
                for k, v in d.items():
                    if v != 0:
                        check2 = False
                if check2:
                    return " ".join(sorted([p, poke]))
            else:
                for k, v in d.items():
                    d[k] = master[k]
    return None


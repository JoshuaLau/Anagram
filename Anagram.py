from collections import defaultdict
def unscramble(anagram, wordbank):
    l = []
    for word in wordbank:
        d = defaultdict(int)
        for c in anagram.lower().replace(" ", ""):
            d[c] += 1
        check = True
        for c in word:
            d[c] -= 1
            if d[c] < 0:
                check = False
                break
        if check:
            l.append(word)
    for word in l:
        d = defaultdict(int)
        master = defaultdict(int)
        for c in anagram.lower().replace(" ", ""):
            d[c] += 1
            master[c] += 1
        for c in word:
            d[c] -= 1
            master[c] -= 1
        for word2 in l:
            check = True
            for c in word2:
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
                    return " ".join(sorted([word2, word]))
            else:
                for k, v in d.items():
                    d[k] = master[k]
    return None #didn't find an exact unscramble

import re

def subst(string):
    """Replace words with ints edge cases due to replacement sevenine parses as 79, hack this by placing the last letter back"""
    words = {'one':'1e', 'two':'2o', 'three':'3e', 'four':'4r', 'five':'5e', 'six':'6x', 'seven':'7n', 'eight':'8t', 'nine':'9e'}
    keys = words.keys()

    new_string = string

    ind = list()
    for k in keys:
        it = re.finditer(k, string)
        for y in it:
            if y is not None:
                ind.append((y.start(), k))

    # Sort by first replacement
    ind = sorted(ind, key=lambda x: x[0])

    for j in ind:
        new_string = re.sub(j[1], words[j[1]], new_string, count=1)

    return new_string

def relookup(s):
    try:
        l = re.match('.*?(\d{1}).*?', s)
        return l.group(1)
    except:
        return 0


with open('1.input.txt', 'r') as fh:
    data = fh.read().split('\n')
    s = 0
    s2 = 0
    for d in data:
        newd = subst(d)

        first = relookup(d)
        first2 = relookup(newd)

        last = relookup(d[::-1])
        last2 = relookup(newd[::-1])

        d = first + last
        d2 = first2 + last2
        d = int(d)
        d2 = int(d2)
        s += d
        s2 += d2

    print('Part1:', s)
    print('Part2:', s2)

import data


def rank_symbols():
    for symbol in data.ALLOWED_SYMBOLS:
        data.ranks.append(ord(symbol))
    data.ranks.sort()
    return data.ranks


def unrank_symbols():
    rank_symbols()
    for rank in data.ranks:
        data.unranks.append(chr(rank))
    return data.unranks


def find_rank(char, list):
    rank = 0
    for l in list:
        if char == l:
            rank = list.index(l)
    return rank
#value error

rank_symbols()
print(data.ranks)

"""
Moser-de Bruijn sequence

0, 1, 4, 5, 16, 17, 20, 21, 64, 65, ...
"""


def moser_de_bruijn(n):
    return int(bin(n)[2:], 4)


def rec_moser_de_bruijn(n):
    if n in (0, 1):
        return n
    elif n % 2 == 0:
        return 4 * rec_moser_de_bruijn(n // 2)
    else:
        return 4 * rec_moser_de_bruijn(n // 2) + 1

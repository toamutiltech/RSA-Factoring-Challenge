#!/usr/bin/python3
p = 1
q = 25
while p < 25:
    if (p%2 != 0) or (p%3 != 0) or (p%5 != 0) and (q%2 != 0) or (q%3 != 0) or (q%5 != 0):
        n = p * q
        print(f"{n} = {p} * {q}")
        p = p + 2
        q = q-2
        exit

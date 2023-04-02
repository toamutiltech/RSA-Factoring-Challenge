#!/usr/bin/python3
n = 1
b = 25
while n < b:
    if n%2 != 0 or n%3 != 0 or n%5 != 0 and b%2 != 0 or b%3 != 0 or b%5 != 0:
        j = n * b
        print(f"{j} = {n} * {b}")
        n = n + 2
        exit

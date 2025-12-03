#!/usr/bin/env python3

with open("input.txt", "r") as f:
    proc = [rng.split("-") for rng in f.read().split(",")]

_sum = 0

for low, high in proc:
    for i in range(int(low), int(high) + 1):
        string = str(i)
        for j in range(1, len(string) // 2 + 1):
            if set(string.split(string[:j])) == {""}:
                _sum += i
                break

print(_sum)

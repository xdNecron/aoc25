with open("input.txt", "r") as f:
    inputs = f.read()
    proc = [rng.split("-") for rng in inputs.split(",")]
_sum = 0

for low, high in proc:
    for i in range(int(low), int(high) + 1):
        string = str(i)
        half = len(string) // 2
        if string[:half] == string[half:]:
            _sum += i

print(_sum)

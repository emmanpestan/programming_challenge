numbers = []

for i in range(10):
    numbers.append(int(input()))

for n in numbers:
    if numbers.count(n) > 1:
        print(n)
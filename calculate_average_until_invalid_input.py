numbers = []

while True:
    x = input()
    if not x.isdigit():
        break
    numbers.append(int(x))

print(sum(numbers) / len(numbers))
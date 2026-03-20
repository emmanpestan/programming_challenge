numbers = []

while True:
    x = input()
    if not x.isdigit():
        break
    numbers.append(int(x))

most = 0
answer = 0

for n in numbers:
    if numbers.count(n) > most:
        most = numbers.count(n)
        answer = n

print(answer)
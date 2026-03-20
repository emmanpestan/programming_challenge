numbers = []

for i in range(10):
    numbers.append(int(input("Enter number: ")))

for num in numbers:
    if num not in numbers[:numbers.index(num)]:
        print(num)
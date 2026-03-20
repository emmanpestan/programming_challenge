numbers = []

for i in range(10):
    numbers.append(int(input("Enter number: ")))

for num in numbers:
    if numbers.count(num) == 1:
        print(num)
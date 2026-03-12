nums = []

for i in range(10):
    n = int(input("Enter number: "))
    nums.append(n)

for n in nums:
    if nums.count(n) == 1:
        print(n)
nums = []

while True:
    try:
        n = int(input("Enter number: "))
        nums.append(n)
    except:
        break

nums.sort()

for n in nums:
    print(n)
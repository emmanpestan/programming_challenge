nums = []

while True:
    try:
        n = int(input("Enter number: "))
        nums.append(n)
    except:
        break

nums.sort(reverse=True)

for n in nums:
    print(n)
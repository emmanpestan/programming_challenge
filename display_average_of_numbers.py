nums = []

while True:
    try:
        n = int(input("Enter number: "))
        nums.append(n)
    except:
        break

avg = sum(nums) / len(nums)

print(avg)
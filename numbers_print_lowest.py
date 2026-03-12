nums = []

while True:
    try:
        n = int(input("Enter number: "))
        nums.append(n)
    except:
        break

print(min(nums))
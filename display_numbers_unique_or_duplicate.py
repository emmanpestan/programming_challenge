nums = []

while True:
    try:
        n = int(input("Enter number: "))
    except:
        break

    if n in nums:
        print("Duplicate")
    else:
        print("Unique")

    nums.append(n)
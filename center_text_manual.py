text = input()
n = int(input())

space = n - len(text)
left = space // 2
right = space - left

print(" " * left + text + " " * right)
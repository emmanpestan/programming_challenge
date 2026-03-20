a = int(input())
b = int(input())

start = min(a, b)
end = max(a, b)

for i in range(start + 1, end):
    print(i)
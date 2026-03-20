text = input()
n = int(input())

while len(text) < n:
    text = " " + text

print(text)
text = input()
n = int(input())

while len(text) < n:
    text = "0" + text

print(text)
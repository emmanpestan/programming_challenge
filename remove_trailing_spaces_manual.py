text = input()
i = len(text) - 1

while i >= 0 and text[i] == " ":
    i -= 1

print(text[:i+1])
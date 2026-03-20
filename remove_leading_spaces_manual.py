text = input()
i = 0

while i < len(text) and text[i] == " ":
    i += 1

print(text[i:])
text = input()
result = ""
new = True

for ch in text:
    if ch == " ":
        result += ch
        new = True
    else:
        if new and 'a' <= ch <= 'z':
            result += chr(ord(ch) - 32)
        elif not new and 'A' <= ch <= 'Z':
            result += chr(ord(ch) + 32)
        else:
            result += ch
        new = False

print(result)
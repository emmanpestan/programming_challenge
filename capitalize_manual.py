text = input()
result = ""

for i in range(len(text)):
    ch = text[i]
    
    if i == 0 and 'a' <= ch <= 'z':
        result += chr(ord(ch) - 32)
    elif i > 0 and 'A' <= ch <= 'Z':
        result += chr(ord(ch) + 32)
    else:
        result += ch

print(result)
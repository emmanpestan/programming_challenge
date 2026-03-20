text = input()
ok = True

for ch in text:
    if 'A' <= ch <= 'Z':
        ok = False

print(ok)
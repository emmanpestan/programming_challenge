text = input()
ok = True

for ch in text:
    if 'a' <= ch <= 'z':
        ok = False

print(ok)
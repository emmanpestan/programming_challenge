text = input()
prefix = input()

if text[:len(prefix)] == prefix:
    print(text[len(prefix):])
else:
    print(text)
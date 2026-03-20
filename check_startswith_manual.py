text = input()
start = input()

if text[:len(start)] == start:
    print(True)
else:
    print(False)
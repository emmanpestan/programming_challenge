text = input()
end = input()

if text[-len(end):] == end:
    print(True)
else:
    print(False)
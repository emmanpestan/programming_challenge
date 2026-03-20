text = input()
suffix = input()

if text[-len(suffix):] == suffix:
    print(text[:-len(suffix)])
else:
    print(text)
text = input()
sub = input()

for i in range(len(text) - len(sub), -1, -1):
    if text[i:i+len(sub)] == sub:
        print(i)
        break
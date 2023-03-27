d = 'C:/python373'
s = [d[i] for i in range(len(d))]

for i in range(len(s)):
    if s[i] == '/':
        s[i] = '\\'

print(s)
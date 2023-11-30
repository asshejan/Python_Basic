s = input()
l, r = 0, 0
res = []
ans = ""
idx = 0

for i in range(len(s)):
    if s[i] == 'L':
        l += 1
        ans += 'L'
    else:
        r += 1
        ans += 'R'

    if l == r:
        res.append(ans)
        ans = ""
        idx += 1

print(idx)
for i in range(idx):
    print(res[i])

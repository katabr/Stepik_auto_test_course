s = input()
s0 = '+'
SUM = ''
sk = '+'
s1 = s + s0
l = len(s)
i = 1
k = 1
j = 0
ss = []
while i <= l:
    if s[i - 1] == s1[i]:
        k = k + 1

    else:

        s0 = s[i - 1]
        sk = str(k)
        ss = ss + [s[i - 1], k]
        SUM = SUM + s0 + sk

        k = 1
    i += 1

print(SUM)

d = {}
s = input().lower().split()

l = len(s)

for i = 1 to n:
    d[ai] = i

    if key in d:
        k = k + 1
        d[key] = k

while i <= l:
    if s[i - 1] == s1[i]:
        k = k + 1

    else:

        s0 = s[i - 1]
        sk = str(k)
        ss = ss + [s[i - 1], k]
        SUM = SUM + s0 + sk

        k = 1
    i += 1

for key, value in d.items():
    print(key, value, end="
                          ")


def update_dictionary(d, key, value):
    if key in d:

        if isinstance(d[key], list):
            d[key].append(value)
        else:
            d[key] = [d[key], value]

    elif 2 * key in d:
        try:
            d[2 * key].append(value)
        except AttributeError:
            d[2 * key] = [d[2 * key], value]
    else:
        d[2 * key] = [value]


d = {}
print(update_dictionary(d, 1, -1))  # None
print(d)  # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)  # {2: [-1, -2]}
update_dictionary(d, 1, -3)
print(d)
dict = {}
for _ in range(int(raw_input())):
    name = raw_input()
    grade = float(raw_input())
    dict[name] = grade
scores = dict.values()
second = sorted(list(set(scores)))[1]
second_lowest = []
for key, value in dict.items():
    if value == second:
        second_lowest.append(key)
second_lowest.sort()
for name in second_lowest:
    print name

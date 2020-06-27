from collections import namedtuple

n = int(input())
columns = input().split()

masterlist = []
data = namedtuple('student', columns)
for i in range(n):
    columns = input().split()
    student = data(*columns)
    masterlist.append(student)

print(sum(masterlist.MARKS)/n)
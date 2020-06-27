(depth, width) = map(int, input().split())

for i in range(1, depth, 2):
    print((i * ".|.").center(width, "-"))
print ("WELCOME".center(width, "-"))
for i in range(depth - 2, -1, -2):
    print((i * ".|.").center(width, "-"))

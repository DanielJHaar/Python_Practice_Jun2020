def func(x,y,z,n):
    print ([[i, j, k] for i in range (0, x+1) for j in range (0, y+1) for k in range (0, z+1) if i + j + k != n])
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

func(x,y,z,n)
def weird(n):
    if n % 2 != 0:
        print('Weird')
    elif n % 2 == 0 and n > 1 and n < 6:
        print ('Not Weird')
    elif n % 2 == 0 and n > 5 and n < 21:
        print ('Weird')
    else:
        print ('Not Weird')

if __name__ == '__main__':
    n = int(input())
weird(n)
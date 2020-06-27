import string

alphabet = list(string.ascii_lowercase)

def print_rangoli(size):
    order = size - 1
    for i in range (order, 0, -1):
        row = ['-'] * (2 * size - 1)
        for j in range(size - i):
            row[order - j] = row[order + j] = alphabet[j + i]
        print('-'.join(row))    
        
    for i in range (0, size):
        row = ['-'] * (2 * size - 1)
        for j in range (0, size - i):
            row[order - j] = row[order + j] = alphabet[j + i]
        print('-'.join(row))    
            
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
import string


def print_rangoli(size):
    N = int(size)
    mid = N - 1

    for i in range(N - 1, 0, -1):
        row = ['-'] * (2 * N - 1)
        for j in range(N - i):
            row[mid - j] = row[mid + j] = string.ascii_lowercase[j + i]
        print('-'.join(row))

    for i in range(0, N):
        row = ['-'] * (2 * N - 1)
        for j in range(0, N - i):
            row[mid - j] = row[mid + j] = string.ascii_lowercase[j + i]
        print('-'.join(row))


def AlphabetRangoli(size):
    n = int(size)
    alpha = string.ascii_lowercase
    row = ''
    row_width = (n * 4) - 3
    for i in range(1, n+1):
        for j in range(0, i):
            row = row + alpha[n - j - 1]
            if len(row) < row_width:
                row = row + '-'
        for k in range(i-1,0,-1):
            row = row + alpha[n - k]
            if len(row) < row_width :
                row = row + '-'
        print(row.center(row_width,'-'))
        row = ''
    for i in range(n-1, 0, -1):
        row = ''
        for j in range(0, i):
            row = row + alpha[n - j - 1]
            if len(row) < row_width:
                row = row + '-'
        for k in range(i-1, 0, -1):
            row = row + alpha[n - k]
            if len(row) < row_width:
                row = row + '-'
        print(row.center(row_width, '-'))
        row = ''


print_rangoli(5)
AlphabetRangoli(5)


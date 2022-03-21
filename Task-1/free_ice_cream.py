'''CodeForces: Free Ice Cream'''

if __name__ == '__main__':
    n, x = map(int, input().split())
    count = 0
    for _ in range(n):
        line = input().split()
        if line[0] == '+':
            x += int(line[1])
        else:
            if int(line[1]) > x:
                count += 1
            else:
                x -= int(line[1])

    print(x, count, sep=' ')

'''CodeForces: Sum of Digits'''

if __name__ == '__main__':
    n = input()
    count = 0
    while len(n) > 1:
        s = 0
        count += 1
        for i in n:
            s += int(i)
        n = str(s)

    print(count)

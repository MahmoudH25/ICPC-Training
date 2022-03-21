'''CodeForces: Steps'''
import math

if __name__ == '__main__':
    # input Operation
    n, m = list(map(int, input().split()))
    x, y = list(map(int, input().split()))
    steps = 0
    for _ in range(int(input())):
        a = math.inf
        dx, dy = map(int, input().split())
        if dx > 0:
            a = min(a, (n - x) // dx)
        if dx < 0:
            a = min(a, (x - 1) // -dx)
        if dy > 0:
            a = min(a, (m - y) // dy)
        if dy < 0:
            a = min(a, (y - 1) // -dy)

        x += dx * a
        y += dy * a
        steps += a

    print(steps)

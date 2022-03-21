'''CodeForcess: Boy or Girl'''

if __name__ == '__main__':
    s = list(input())
    s = set(s)
    if len(s) % 2 == 0:
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")

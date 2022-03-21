'''HackerRank: President's Office'''

if __name__ == '__main__':
    line = input().split()
    n, m, c = int(line[0]), int(line[1]), line[2]
    mat = [input() for _ in range(n)]
    count = set()
    for i in range(n):
        for j in range(m):
            if mat[i][j] == c:
                if i-1 >= 0 and mat[i-1][j] != '.' and mat[i-1][j] != c:
                    count.add(mat[i-1][j])
                if i+1 < n and mat[i+1][j] != '.' and mat[i+1][j] != c:
                    count.add(mat[i+1][j])
                if j-1 >= 0 and mat[i][j-1] != '.' and mat[i][j-1] != c:
                    count.add(mat[i][j-1])
                if j+1 < m and mat[i][j+1] != '.' and mat[i][j+1] != c:
                    count.add(mat[i][j+1])

    print(len(count))

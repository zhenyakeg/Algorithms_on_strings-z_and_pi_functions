def levenstein(s1, s2):
    lev_dist = [[0 for i in range(len(s1) + 1)] for i in range(len(s2) + 1)]
    for x in range(len(s1)):
        lev_dist[0][x] = x
    for y in range(len(s2)):
        lev_dist[y][0] = y
    for i in range(1, len(s2) + 1):
        for j in range(1, len(s1) + 1):
            if s2[i - 1] == s1[j - 1]:
                lev_dist[i][j] = lev_dist[i-1][j-1]
            else:
                lev_dist[i][j] = min(lev_dist[i][j-1],
                                     lev_dist[i-1][j],
                                     lev_dist[i-1][j-1]) + 1
    return lev_dist[len(s2)][len(s1)]

input_s1 = input()
input_s2 = input()
print(levenstein(input_s1, input_s2))

#!/usr/bin/python


def edit_distance(x, y):
    n, m = len(x), len(y)
    dp = [[0 for j in range(m + 1)] for i in range(n + 1)]

    if n is 0:
        return m
    elif m is 0:
        return n

    for i in range(n + 1):
        for j in range(m + 1):
            if i is 0:
                dp[i][j] = j
            elif j is 0:
                dp[i][j] = i
            elif x[i - 1] is y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j - 1],
                                   dp[i - 1][j], dp[i][j - 1])
    return dp[n][m]

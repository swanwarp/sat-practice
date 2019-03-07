def check(R, L, K, xy):
    N = len(R)

    for i in range(0, N):
        if not (-1 < xy[i][0] < L and -1 < xy[i][1] < L):
            return False

    for i in range(0, N - 1):
        if abs(xy[i][0] - xy[i + 1][0]) == abs(xy[i][1] - xy[i + 1][1]):
            return False

    k = 0

    for i in range(0, N - 2):
        for j in range(i + 2, N):

            if xy[i][0] == xy[j][0] and xy[i][1] == xy[j][1]:
                return False

            if R[i] == "H" and R[j] == "H" and ((abs(xy[i][0] - xy[j][0]) == 1 and abs(xy[i][1] - xy[j][1]) == 0) or (abs(xy[i][0] - xy[j][0]) == 0 and abs(xy[i][1] - xy[j][1]) == 1)):
                print(xy[i])
                print(xy[j])
                k += 1
                print()

    return k == K


print(check("HHPPHH", 3, 1, [[0, 0], [1, 0], [2, 0], [2, 1], [1, 1], [1, 2]]))

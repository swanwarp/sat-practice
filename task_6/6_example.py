peptide = "HHHPPHPHPHPPHPHPHPPH"

R = []

for p in peptide:
    R.append(p == "H")

N = len(R)
neighbours = []

for i in range(0, N):
    temp = []

    for j in range(0, N):
        temp.append(False)

    neighbours.append(temp)


def sat1(L, K):
    x_a = []
    y_a = []

    for i in range(0, L):
        x_a.append(False)
        y_a.append(False)

    right = []
    left = []
    up = []
    down = []
    H = []

    for i in range(0, N):
        right.append([])
        left.append([])
        up.append([])
        down.append([])
        H.append([])

        for j in range(0, N):
            right[i].append(False)
            left[i].append(False)
            up[i].append(False)
            down[i].append(False)
            H[i].append(False)



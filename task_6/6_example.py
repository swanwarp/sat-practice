from subprocess import run
from time import time


peptide = "HHHPPHPHPHPPHPHPHPPH"

R = []

for p in peptide:
    R.append(p == "H")


def sat2(R, L, K, x0, y0, x1, y1):
    clauses = []

    N = len(R)

    num = N * N * L

    xs = 0 * num + 1
    ys = 1 * num + 1
    ns = 2 * num + 1
    rs = 3 * num + 1
    ls = 4 * num + 1
    us = 5 * num + 1
    ds = 6 * num + 1
    mxs = 7 * num + 1
    mxms = 8 * num + 1
    mxps = 9 * num + 1
    mys = 10 * num + 1
    myms = 11 * num + 1
    myps = 12 * num + 1
    mxas = 13 * num + 1
    mxmas = 14 * num + 1
    mxpas = 15 * num + 1
    myas = 16 * num + 1
    mymas = 17 * num + 1
    mypas = 18 * num + 1
    bs = 19 * num + 1
    es = 20 * num + 1

    X = []
    Y = []

    Xa = {}
    Ya = {}

    for i in range(0, N):
        X.append({})
        Y.append({})

        for a in range(0, L):
            X[i].setdefault(a, xs + i * L + a)
            Y[i].setdefault(a, ys + i * L + a)
            Xa.setdefault(xs + i * L + a, (i, a))
            Ya.setdefault(ys + i * L + a, (i, a))

    right = []
    left = []
    up = []
    down = []
    neighbours = []
    begin = []
    end = []
    Na = {}
    Ba = {}
    Ea = {}

    mx = []
    mx_m = []
    mx_p = []

    my = []
    my_m = []
    my_p = []

    mxa = []
    mx_ma = []
    mx_pa = []

    mya = []
    my_ma = []
    my_pa = []

    for i in range(0, N):
        right.append({})
        left.append({})
        up.append({})
        down.append({})
        neighbours.append({})

        mx.append({})
        mx_m.append({})
        mx_p.append({})

        my.append({})
        my_m.append({})
        my_p.append({})

        mxa.append({})
        mx_ma.append({})
        mx_pa.append({})

        mya.append({})
        my_ma.append({})
        my_pa.append({})

        for j in range(0, N):
            right[i].setdefault(j, rs + i * N + j)
            left[i].setdefault(j, ls + i * N + j)
            up[i].setdefault(j, us + i * N + j)
            down[i].setdefault(j, ds + i * N + j)
            neighbours[i].setdefault(j, ns + i * N + j)
            Na.setdefault(ns + i * N + j, (i, j))

            mx[i].setdefault(j, mxs + i * N + j)
            mx_m[i].setdefault(j, mxms + i * N + j)
            mx_p[i].setdefault(j, mxps + i * N + j)

            my[i].setdefault(j, mys + i * N + j)
            my_m[i].setdefault(j, myms + i * N + j)
            my_p[i].setdefault(j, myps + i * N + j)

            mxa[i].setdefault(j, {})
            mx_ma[i].setdefault(j, {})
            mx_pa[i].setdefault(j, {})

            mya[i].setdefault(j, {})
            my_ma[i].setdefault(j, {})
            my_pa[i].setdefault(j, {})

            for a in range(0, L):
                mxa[i][j].setdefault(a, mxas + i * N * L + j * L + a)
                mx_ma[i][j].setdefault(a, mxmas + i * N * L + j * L + a)
                mx_pa[i][j].setdefault(a, mxpas + i * N * L + j * L + a)

                mya[i][j].setdefault(a, myas + i * N * L + j * L + a)
                my_ma[i][j].setdefault(a, mymas + i * N * L + j * L + a)
                my_pa[i][j].setdefault(a, mypas + i * N * L + j * L + a)

    for i in range(0, K):
        begin.append({})
        end.append({})

        for a in range(0, N):
            begin[i].setdefault(a, bs + i * N + a)
            end[i].setdefault(a, es + i * N + a)
            Ba.setdefault(bs + i * N + a, (i, a))
            Ea.setdefault(es + i * N + a, (i, a))

    for i in range(0, N):
        for j in range(0, N):
            # neighbours[i][j] <--> R[i][j] or L[i][j] or U[i][j] or D[i][j]
            clauses.append([-neighbours[i][j], right[i][j], left[i][j], up[i][j], down[i][j]])
            clauses.append([neighbours[i][j], -right[i][j]])
            clauses.append([neighbours[i][j], -left[i][j]])
            clauses.append([neighbours[i][j], -up[i][j]])
            clauses.append([neighbours[i][j], -down[i][j]])

            # right match formula
            clauses.append([-right[i][j], my[i][j]])
            clauses.append([-right[i][j], mx_p[i][j]])
            clauses.append([right[i][j], -my[i][j], -mx_p[i][j]])

            # left match formula
            clauses.append([-left[i][j], my[i][j]])
            clauses.append([-left[i][j], mx_m[i][j]])
            clauses.append([left[i][j], -my[i][j], -mx_m[i][j]])

            # up match formula
            clauses.append([-up[i][j], mx[i][j]])
            clauses.append([-up[i][j], my_m[i][j]])
            clauses.append([up[i][j], -mx[i][j], -my_m[i][j]])

            # down match formula
            clauses.append([-down[i][j], mx[i][j]])
            clauses.append([-down[i][j], my_p[i][j]])
            clauses.append([down[i][j], -mx[i][j], -my_p[i][j]])

            # match x and match xa formula
            temp = [-mx[i][j]]
            for a in range(0, L):
                clauses.append([mx[i][j], -mxa[i][j][a]])
                temp.append(mxa[i][j][a])

            clauses.append(temp)

            # match x+1 and match x+1a formula
            temp = [-mx_p[i][j]]
            for a in range(0, L):
                clauses.append([mx_p[i][j], -mx_pa[i][j][a]])
                temp.append(mx_pa[i][j][a])

            clauses.append(temp)

            # match x-1 and match x-1a formula
            temp = [-mx_m[i][j]]
            for a in range(0, L):
                clauses.append([mx_m[i][j], -mx_ma[i][j][a]])
                temp.append(mx_ma[i][j][a])

            clauses.append(temp)

            # match y and match ya formula
            temp = [-my[i][j]]
            for a in range(0, L):
                clauses.append([my[i][j], -mya[i][j][a]])
                temp.append(mya[i][j][a])

            clauses.append(temp)

            # match y+1 and match y+1a formula
            temp = [-my_p[i][j]]
            for a in range(0, L):
                clauses.append([my_p[i][j], -my_pa[i][j][a]])
                temp.append(my_pa[i][j][a])

            clauses.append(temp)

            # match y-1 and match y-1a formula
            temp = [-my_m[i][j]]
            for a in range(0, L):
                clauses.append([my_m[i][j], -my_ma[i][j][a]])
                temp.append(my_ma[i][j][a])

            clauses.append(temp)

    for i in range(0, N):
        for j in range(0, N):
            # match xa and actual x
            for a in range(0, L):
                clauses.append([-mxa[i][j][a], X[i][a]])
                clauses.append([-mxa[i][j][a], X[j][a]])
                clauses.append([mxa[i][j][a], -X[i][a], -X[j][a]])

            # match ya and actual y
            for a in range(0, L):
                clauses.append([-mya[i][j][a], Y[i][a]])
                clauses.append([-mya[i][j][a], Y[j][a]])
                clauses.append([mya[i][j][a], -Y[i][a], -Y[j][a]])

        for j in range(0, N):
            # match x-1a and actual x
            for a in range(1, L):
                clauses.append([-mx_ma[i][j][a], X[i][a]])
                clauses.append([-mx_ma[i][j][a], X[j][a - 1]])
                clauses.append([mx_ma[i][j][a], -X[i][a], -X[j][a - 1]])

            # match y-1a and actual y
            for a in range(1, L):
                clauses.append([-my_ma[i][j][a], Y[i][a]])
                clauses.append([-my_ma[i][j][a], Y[j][a - 1]])
                clauses.append([my_ma[i][j][a], -Y[i][a], -Y[j][a - 1]])

        for j in range(0, N):
            # match x+1a and actual x
            for a in range(0, L - 1):
                clauses.append([-mx_pa[i][j][a], X[i][a]])
                clauses.append([-mx_pa[i][j][a], X[j][a + 1]])
                clauses.append([mx_pa[i][j][a], -X[i][a], -X[j][a + 1]])

            # match y+1a and actual y
            for a in range(0, L - 1):
                clauses.append([-my_pa[i][j][a], Y[i][a]])
                clauses.append([-my_pa[i][j][a], Y[j][a + 1]])
                clauses.append([my_pa[i][j][a], -Y[i][a], -Y[j][a + 1]])

    clauses.append([X[0][x0]])
    clauses.append([X[1][x1]])
    clauses.append([Y[0][y0]])
    clauses.append([Y[1][y1]])

    for i in range(0, N):
        temp = []
        temp2 = []

        for a in range(0, L):
            temp.append(X[i][a])
            temp2.append(Y[i][a])

        clauses.append(temp)
        clauses.append(temp2)

    for i in range(0, N):
        for a in range(0, L):
            for b in range(0, L):
                if a == b:
                    continue

                clauses.append([-X[i][a], -X[i][b]])
                clauses.append([-Y[i][a], -Y[i][b]])

    for i in range(0, N):
        for j in range(0, N):
            if i >= j:
                continue
            for a in range(0, L):
                for b in range(0, L):
                    clauses.append([-X[i][a], -X[j][a], -Y[i][b], -Y[j][b]])

    for i in range(0, N - 1):
        clauses.append([neighbours[i][i + 1]])
        clauses.append([neighbours[i + 1][i]])

    for i in range(0, N):
        for j in range(0, N):
            clauses.append([-right[i][j], -left[i][j]])
            clauses.append([-right[i][j], -up[i][j]])
            clauses.append([-right[i][j], -down[i][j]])
            clauses.append([-left[i][j], -up[i][j]])
            clauses.append([-left[i][j], -down[i][j]])
            clauses.append([-up[i][j], -down[i][j]])

    for i in range(0, N):
        for j in range(0, N):
            for a in range(0, L):
                clauses.append([-neighbours[i][j], -X[i][a], -X[j][a], up[i][j], down[i][j]])
                clauses.append([-neighbours[i][j], -Y[i][a], -Y[j][a], right[i][j], left[i][j]])

    for i in range(0, N):
        for j in range(0, N):
            for a in range(0, L - 1):
                clauses.append([-right[i][j], -X[i][a], X[j][a + 1]])
                clauses.append([-down[i][j], -Y[i][a], Y[j][a + 1]])

            for a in range(1, L):
                clauses.append([-left[i][j], -X[i][a], X[j][a - 1]])
                clauses.append([-up[i][j], -Y[i][a], Y[j][a - 1]])

    for i in range(0, N):
        for j in range(0, N):
            if i == j:
                continue

            clauses.append([-X[i][0], -left[i][j]])
            clauses.append([-X[i][L - 1], -right[i][j]])
            clauses.append([-Y[i][0], -up[i][j]])
            clauses.append([-Y[i][L - 1], -down[i][j]])

    # only R[a] = true // b/e[i][a] <-> R[a]
    for i in range(0, K):
        for a in range(0, N):
            if not R[a]:
                clauses.append([-begin[i][a]])
                clauses.append([-end[i][a]])

    # b,e exist
    for i in range(0, K):
        temp_b = []
        temp_e = []

        for a in range(0, N):
            temp_b.append(begin[i][a])
            temp_e.append(end[i][a])

        clauses.append(temp_b)
        clauses.append(temp_e)

    # b[i][a] & e[i][c] -> n[a][c] & n[c][a]
    for i in range(0, K):
        for a in range(0, N):
            for b in range(0, N):
                clauses.append([-begin[i][a], -end[i][b], neighbours[a][b], neighbours[b][a]])

    for i in range(0, K):
        for j in range(0, K):
            if i == j:
                continue

            for a in range(0, N):
                for b in range(0, N):
                    clauses.append([-begin[i][a], -begin[j][a], -end[i][b], - end[j][b]])
                    clauses.append([-begin[i][a], -begin[j][b], -end[i][b], - end[j][a]])

    for i in range(0, K):
        clauses.append([-end[i][0], -begin[i][0]])
        clauses.append([-end[i][0], -begin[i][1]])
        clauses.append([-end[i][N - 1], -begin[i][N - 1]])
        clauses.append([-end[i][N - 1], -begin[i][N - 2]])

        for a in range(1, N - 1):
            clauses.append([-end[i][a], -begin[i][a]])
            clauses.append([-end[i][a], -begin[i][a - 1]])
            clauses.append([-end[i][a], -begin[i][a + 1]])

    # b_ia -> or_b e_ib
    for i in range(0, K):
        for a in range(0, N):
            temp_b = [-begin[i][a]]
            temp_e = [-end[i][a]]

            for b in range(0, N):
                temp_b.append(end[i][b])
                temp_e.append(begin[i][b])

            clauses.append(temp_b)
            clauses.append(temp_e)

    for i in range(0, K):
        for a in range(0, N):
            for b in range(0, N):
                if a == b:
                    continue

                clauses.append([-begin[i][a], -begin[i][b]])
                clauses.append([-end[i][a], -end[i][b]])

    inp = open("../lingeling/example.in", "w")

    inp.write("p cnf ")
    inp.write(str(21 * num))
    inp.write(" " + str(len(clauses)) + "\n")

    for c in clauses:
        for l in c:
            inp.write(str(l) + " ")

        inp.write("0\n")

    inp.close()

    inp = open("../lingeling/example.out", "w")
    compl = run("../lingeling/lingeling -q ../lingeling/example.in", shell=True, stdout=inp)
    inp.close()

    inp = open("../lingeling/example.out", "r")
    res = inp.readline()

    if res == "s UNSATISFIABLE\n":
        print("NO ANSWER")
    else:
        strs = inp.readlines()

        s = []

        for st in strs:
            t = st.split(" ")
            t.pop(0)

            if t[len(t) - 1] == "0\n":
                t.pop()

            s += t

        for i in range(xs - 1, xs + num - 1):
            if s[i][0] != '-':
                print(Xa[int(s[i])], end=" ")

        print()

        for i in range(ys - 1, ys + num - 1):
            if s[i][0] != '-':
                print(Ya[int(s[i])], end=" ")

        print()


start = time()
sat2(R, 5, 10, 3, 2, 2, 2)
print(time() - start)

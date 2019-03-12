from subprocess import run
from os import remove

n = int(input()) + 1
m = {}
m_reverse = {}

for i in range(1, n):
    for j in range(1, n):
        m.setdefault((i - 1) * (n - 1) + j, (i, j))
        m_reverse.setdefault((i, j), (i - 1) * (n - 1) + j)

clauses = []

for i in range(1, n):
    temp = []

    for j in range(1, n):
        temp.append(m_reverse[(i, j)])

    clauses.append(temp)

for i in range(1, n):
    for j in range(1, n):
        for k in range(j + 1, n):
            clauses.append([-m_reverse[(i, j)], -m_reverse[(i, k)]])

for i in range(1, n):
    for j in range(1, n):
        for k in range(j + 1, n):
            clauses.append([-m_reverse[(j, i)], -m_reverse[(k, i)]])

for k in range(1 - n, n - 1):
    for i1 in range(1, n):
        for j1 in range(1, n):
            if i1 - j1 == k:
                for i2 in range(i1 + 1, n):
                    for j2 in range(1, n):
                        if i2 - j2 == k:
                            clauses.append([-m_reverse[(i1, j1)], -m_reverse[(i2, j2)]])

for k in range(2, 2 * n):
    for i1 in range(1, n):
        for j1 in range(1, n):
            if i1 + j1 == k:
                for i2 in range(i1 + 1, n):
                    for j2 in range(1, n):
                        if i2 + j2 == k:
                            clauses.append([-m_reverse[(i1, j1)], -m_reverse[(i2, j2)]])

count = 0
ans = []

while True:
    inp = open("example.in", "w")

    inp.write("p cnf ")
    inp.write(str((n - 1) * (n - 1)))
    inp.write(" " + str(len(clauses)) + "\n")

    for c in clauses:
        for l in c:
            inp.write(str(l) + " ")

        inp.write("0\n")

    inp.close()

    inp = open("example.out", "w")
    compl = run("..\cms.exe --verb 0 example.in", shell=True, stdout=inp)
    inp.close()

    inp = open("example.out", "r")
    res = inp.readline()

    if res == "s UNSATISFIABLE\n":
        inp.close()
        break
    else:
        strs = inp.readlines()
        inp.close()

    s = []

    for st in strs:
        t = st.split(" ")
        t.pop(0)

        if t[len(t) - 1] == "0\n" or t[len(t) - 1] == "\n":
            t.pop()

        s += t

    count += 1
    ans.append(s)

    temp = []

    for ss in s:
        temp.append(-int(ss))

    clauses.append(temp)

print(count)

for a in ans:
    for vert in a:
        if int(vert) > 0:
            print(m[int(vert)], end=" ")

    print()

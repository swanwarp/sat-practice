f = open("task_4.tests", "r")
o = open("test_out.tests", "w")

strs = f.readlines()

i = 0

while i < len(strs):
    n = int(strs[i].split('\n')[0])

    i += 1

    k = int(strs[i].split('\n')[0])

    out = "{\"" + str(k) + "\", "

    for j in range(i + 1, i + k):
        out += "\"" + strs[j].split('\n')[0] + "\", "

    out += "\"" + strs[i + k].split('\n')[0] + "\"};\n\n"

    i += k + 2

    o.write(out)

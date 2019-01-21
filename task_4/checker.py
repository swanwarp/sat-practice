from subprocess import run, PIPE

inp = open("./task_4.tests", "r")

while True:
    N = inp.readline()[:-1]

    if N == "":
        break

    solution = run("python3.6 ./4_example.py", shell=True, stdout=PIPE, timeout=120, encoding="utf-8", input=N)

    result = solution.stdout.split("\n")

    if result[-1] == '':
        result.pop()

    for i in range(0, len(result)):
        if result[i][-1] == ' ':
            result[i] = result[i][:-1]

    answer = inp.readline()[:-1]
    flag = True

    while answer != "":
        if answer not in result:
            flag = False

        answer = inp.readline()[:-1]

    if flag:
        print("Test with N=" + N + " is passed.")
    else:
        print("Test with N=" + N + " isn't passed!")

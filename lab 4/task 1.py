# TODO решите задачу
def task() -> float:
    got = 0
    c1 = 0
    c2 = 0
    f = open("input.json", "r")
    file = f.readlines()
    for i in range(len(file)):
        if file[i].find("score") != -1:
            c1 = float(file[i][((file[i].find("score")) + 8):len(file[i]) - 2])
        elif (file[i].find("weight")) != -1:
            c2 = float(file[i][((file[i].find("weight")) + 9):len(file[i]) - 1])
        if (c1 != 0) and (c2 != 0):
            got += c1 * c2
            c1, c2 = 0, 0
    f.close()

    return round(got, 3)


print(task())

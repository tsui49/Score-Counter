scorelist = []

with open("SIRS201711381.csv",encoding="utf-8_sig") as f:
    lines = f.readlines()
    for i in range(len(lines)):
        # line = line.rstrip("\n")
        if i == 0:
            continue
        else:
            lines[i] = lines[i].replace("\"", "")
            scorelist.append(lines[i].split(","))

Ap = []
A = []
B = []
C = []
D = []
P = []

for i in range(len(scorelist)):
    if scorelist[i][7] == 'A+':
        Ap.append(float(scorelist[i][4]))
    elif scorelist[i][7] == 'A':
        A.append(float(scorelist[i][4]))
    elif scorelist[i][7] == 'B':
        B.append(float(scorelist[i][4]))
    elif scorelist[i][7] == 'C':
        C.append(float(scorelist[i][4]))
    elif scorelist[i][7] == 'D':
        D.append(float(scorelist[i][4]))
    elif scorelist[i][7] == 'P':
        P.append(float(scorelist[i][4]))

print("\t科目数\t単位数")
print("A+\t{}\t{}".format(len(Ap), sum(Ap)))
print("A\t{}\t{}".format(len(A), sum(A)))
print("B\t{}\t{}".format(len(B), sum(B)))
print("C\t{}\t{}".format(len(C), sum(C)))
print("D\t{}\t{}".format(len(D), sum(D)))
print("P\t{}\t{}".format(len(P), sum(P)))

credit = sum(Ap) + sum(A) + sum(B) + sum(C)
Aratio = (sum(Ap) + sum(A)) / credit * 100

print("A+, A, B, C合計: {}".format(credit))
print("A+とAの取得率: {}%".format(Aratio))
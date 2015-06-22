import binascii
import numpy as np
import matplotlib.pyplot as plt
import math
import random
import re

pattern = re.compile('([^\s\w]|_)+')  # usuwamy wszystko poza bialymi znakami i literami/liczbami

f = open('Gajcy', 'r')
# print(f.read())

''' usuwamy znaki interpunkcyjne '''
k = "".join(line for line in f if not line.isspace())
k = pattern.sub('', k)
binary = ' '.join(format(ord(x), 'b') for x in k).replace(' ', '') # tlumaczymy tekst na binarny
#print(binary)
dlugoscTekstu = len(binary)
print(dlugoscTekstu)

prob = binary.count('1') / dlugoscTekstu
entropy = -(1. - prob) * math.log(1. - prob, 2.) - prob * math.log(prob, 2.)
print(prob)
print(entropy)
print(abs(math.log(dlugoscTekstu, 2.*entropy)))

Max_Block = math.ceil(abs(math.log(dlugoscTekstu, 2.*entropy)))
S = 20000
R = [list() for _ in range(0, S)]
AveragesOfR = [0 for _ in range(0, Max_Block)]

''' Szukamy pierwszego powrotu n-bloku od s-tego miejsca '''
for i in range(0, S):
    for b in range(0, Max_Block):
        ReturnIndex = binary.find(binary[i:i + b + 1], i + 1)
        if ReturnIndex != -1:
            R[i].append(ReturnIndex - i)
        else:
            break

#print(R)

# A = np.array(R)
# print(A)
# AveLog = [0 for _ in range(0, Max_Block)]
# for i in range(0, Max_Block):
#     tempAveLog = [t for t in A[:, i] if t > 0]
#     temp = [abs(math.log(tempAveLog[t], 2.)) / (i + 1) for t in range(0, len(tempAveLog))]
#     if sum(temp) == 0 or len(temp) == 0:
#         continue
#     else:
#         AveLog[i] = sum(temp) / len(temp)

AveLog = [0 for _ in range(0, Max_Block)]
for i in range(0, Max_Block):
    tempAveLog = list()
    for j in range(0, S):
        if len(R[j]) > i:
            tempAveLog.append(R[j][i])
    temp = [abs(math.log(tempAveLog[t], 2.)) / (i + 1) for t in range(0, len(tempAveLog))]
    if sum(temp) == 0 or len(temp) == 0:
        continue
    else:
        AveLog[i] = sum(temp) / len(temp)

g2 = {i: AveLog[i] for i in range(1, len(AveLog))}
print(g2)
plt.plot(np.arange(1, len(AveLog), 1), list(g2.values()), color="red")
plt.ylabel('entropia')
plt.xlabel('n')
plt.savefig('PanTadeusz.png')

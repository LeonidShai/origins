import numpy as np

N = 3
M = 4
A = np.array([[2, 7, 9, 3],
              [12, 4, 1, 9],
              [1, 5, 2, 5]])


i = N
j = M


#подсчёт первого столбца
for i in range(1, N):
    A[i, 0] = A[i - 1, 0] + A[i, 0]
#подсчёт первой строки
for j in range(1, M):
    A[0, j] = A[0, j - 1] + A[0, j]

print(A)

for i in range(1, N):
    for j in range(1, M):
        top = A[i - 1, j]
        left = A[i, j - 1]

        if top < left:
            A[i, j] += top
        else:
            A[i, j] += left

steps = [(N-1, M-1)]
i = N-1
j = M-1

for _ in range(i + j):
    top = A[i - 1, j]
    left = A[i, j - 1]
    #проверили откуда пришли
    if top < left:
        i -= 1
    else:
        j -=1
    steps.append((i, j)) #добавляем шаг

print("--------------")
print(A)
steps.reverse()
print(steps)

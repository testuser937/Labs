import numpy as np

N = 57  # Количество объектов
m = 4  # Количество столбцов матрицы X
y = []  # целевой признак
X = []  # Матрица X

# тестовый пример
X_test = [[1, 3], [2, 1], [4, 5], [1, 2], [2, 1]]
y_test = [[4], [1], [3], [2], [6]]

with open('input2.txt', 'r') as inp:
    for _ in range(N):
        y.append(float(inp.readline().strip()))
    inp.readline()
    for _ in range(N):
        s = inp.readline()
        X.append([float(i) for i in s.strip().split()])


def transpose(mat):
    """Транспонирование матрицы"""
    m = len(mat)
    n = len(mat[0])
    tr = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            tr[i][j] = mat[j][i]
    return tr


def multiplication(a, b):
    """Умножение матриц"""
    m, n, q = len(a), len(a[0]), len(b[0])
    c = [[0] * q for _ in range(m)]
    for i in range(m):
        for j in range(q):
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]
    return c


def determ_koef(y_sred, e, y):
    """Коэффициент детерминации"""

    sum_e = sum([i * i for i in e])
    sum_y = sum([(y_k - y_sred) ** 2 for y_k in y])
    return 1 - sum_e / sum_y


def calc_a(X, y):
    """a = (XT*X)^(-1)*XT*y"""
    return np.dot(np.dot(np.linalg.inv(np.dot(X.T, X)), X.T), y)


X = np.array(X)
y = np.array(y)
a = calc_a(X, y)
print('a =', a)

y_rasch = np.dot(X, a)
e = y - y_rasch  # вектор оценочных отклонений
y_rasch_sred = sum(y_rasch) / N  # расчетное среднее y
y_fact_sred = sum(y) / N  # фактическое среднее y
det_koef = determ_koef(y_rasch_sred, e, y)
print('Среднее расчетное y = {0}\nСреднее фактическое y = {1}'.format(y_rasch_sred, y_fact_sred))
print('Коэффициент детерминации = ', det_koef)

a_test = calc_a(np.array(X_test), np.array(y_test))
print('a_test:\n', a_test)

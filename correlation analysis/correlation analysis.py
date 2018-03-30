z = [] # исходные данные
N = 0 # число объектов
p = 10 # число признаков-столбцов

z_sred_lst = [] # среднее в каждом столбце
z_disp_lst = [] # дисперсия в каждом столбце
kovar_mat = [[0] * p for _ in range(p)] # ковариационная матрица
R = [[0] * p for _ in range(p)] # корреляционная матрица

t_tabl = 2.0040448 # критическое значение статистики Стьюдента с числом степеней свободы n-2 = 55, уровень значимости 0,05


def t_ras(r, n):
    return (r * (n - 2) ** 0.5) / (1 - r * r) ** 0.5


def print_matrix(mat, eps=3):
    for i in mat:
        for j in i:
            print(format(j, '.{}f'.format(eps)), end=' ')
            #print(j, end = ' ')
        print()
    print('_' * 70, '\n')


def sred(matrix, result):
    for i in range(p):
        z_sred = 0
        for k in range(N):
            z_sred += matrix[k][i]
        result.append(z_sred / N)


def disp(matrix, sred_lst, result):
    for j in range(p):
        z_disp = 0
        for k in range(0, N):
            z_disp += (matrix[k][j] - sred_lst[j]) ** 2
        result.append(z_disp / N)


# считывание данных
with open('input1.txt', 'r') as inp:
    while True:
        st = inp.readline()
        if not st:
            break
        else:
            N += 1
            z.append([float(i) for i in st.strip().split()])

print('N = {0}, p = {1}'.format(N, p))

sred(z, z_sred_lst)
disp(z, z_sred_lst, z_disp_lst)

for i in range(len(z_sred_lst)):
    print('Среднее в {} столбце = {}, дисперсия = {}'.
          format(i + 1, z_sred_lst[i], z_disp_lst[i]))
print()

# ковариационная матрица
for i in range(p):
    for j in range(p):
        sigma = 0
        for k in range(N):
            sigma += (z[k][i] - z_sred_lst[i]) * (z[k][j] - z_sred_lst[j])
        kovar_mat[i][j] = sigma / N

print('Ковариационная матрица:')
print_matrix(kovar_mat)

# Стандартизованная матрица
X = [[0] * p for i in range(N)]
for i in range(N):
    for j in range(p):
        X[i][j] = (z[i][j] - z_sred_lst[j]) / (z_disp_lst[j] ** 0.5)

# Корреляционная матрица
for i in range(p):
    for j in range(p):
        kor = 0
        for k in range(N):
            kor += X[k][i] * X[k][j]
        R[i][j] = (kor / N)

print('Корреляционная матрица:')
print_matrix(R)

# проверка статистической гипотезы
print()
for i in range(p):
    for j in range(i + 1, p):
        print('{0} и {1}: '.format(i + 1, j + 1), end='')
        t = t_ras(R[i][j], N)
        if abs(t) >= t_tabl:
            print('Связь есть', abs(t), '>=', t_tabl)
        else:
            print('Связи нет', abs(t), '<', t_tabl)

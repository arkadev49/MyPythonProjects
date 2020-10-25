def Inverse(mat, n):
    detA = Determinant(mat, n)
    if detA == 0:
        return
    new = [[0 for __ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new[i][j] = ((-1) ** (i + j)) * Determinant(Minor(mat, i, j, n), n - 1)
    return MultiplyByConstant(Transpose(new, n, n, 1), n, n, 1 / detA)


def Minor(mat, i, j, n):
    minor = []
    for r in range(n):
        if r != i:
            tmp = []
            for c in range(n):
                if c != j:
                    tmp.append(mat[r][c])
            minor.append(tmp)
    return minor


def Determinant(mat, n):
    res = 0
    if n == 1:
        return mat[0][0]
    for i in range(n):
        res += (-1) ** i * mat[0][i] * Determinant(Minor(mat, 0, i, n), n - 1)
    return res


def Transpose(mat, r, c, keyVal):
    new = [[0 for __ in range(r)] for _ in range(c)]
    for i in range(r):
        for j in range(c):
            if keyVal == 1:
                new[i][j] = mat[j][i]
            elif keyVal == 2:
                new[i][j] = mat[r - j - 1][c - i - 1]
            elif keyVal == 3:
                new[i][j] = mat[i][c - j - 1]
            else:
                new[i][j] = mat[r - i - 1][j]
    return new


def MultiplyByConstant(mat, r, c, val):
    if type(val) not in (int, float):
        try:
            val = int(val)
        except ValueError:
            val = float(val)
    new = [[0 for __ in range(r)] for _ in range(c)]
    for i in range(r):
        for j in range(c):
            new[i][j] = mat[i][j] * val
    return new


def MatrixMultiply(mat1, r1, c1, mat2, r2, c2):
    if r2 == c1:
        res = [[0 for __ in range(c2)] for _ in range(r1)]
        for i in range(r1):
            for j in range(c2):
                s = 0
                for k in range(r2):
                    s += mat1[i][k] * mat2[k][j]
                res[i][j] = s

        return res


def AddMatrices(mat1, r1, c1, mat2, r2, c2):
    if r1 == r2 and c1 == c2:
        new = [[0 for __ in range(c1)] for _ in range(r1)]
        for i in range(r1):
            for j in range(c2):
                new[i][j] = mat1[i][j] + mat2[i][j]
        return new


def ShowResult(res):
    if res:
        print('The result is:')
        for i in res:
            for j in i:
                print(j, end=' ')
            print()
    else:
        print('The operation cannot be performed.')


def TakeMatrix(message=''):
    r, c = input('Enter size of {}matrix: '.format(message)).split()
    print('Enter {}matrix:'.format(message))
    r = int(r)
    c = int(c)
    mat = [input().split() for _ in range(r)]
    for i in range(r):
        for j in range(c):
            try:
                mat[i][j] = int(mat[i][j])
            except ValueError:
                mat[i][j] = float(mat[i][j])
    return mat, r, c


while True:
    print('\n1. Add matrices')
    print('2. Multiply matrix by a constant')
    print('3. Multiply matrices')
    print('4. Transpose matrix')
    print('5. Calculate a determinant')
    print('6. Inverse matrix')
    print('0. Exit')
    choice = int(input('Your choice: '))
    if choice in (1, 3):
        m1, row1, col1 = TakeMatrix('first ')
        m2, row2, col2 = TakeMatrix('second ')
        if choice == 1:
            result = AddMatrices(m1, row1, col1, m2, row2, col2)
        else:
            result = MatrixMultiply(m1, row1, col1, m2, row2, col2)
        ShowResult(result)
    elif choice in (2, 4, 5, 6):
        if choice == 4:
            print('\n1. Main diagonal')
            print('2. Side diagonal')
            print('3. Vertical line')
            print('4. Horizontal line')
            choice2 = int(input('Your choice: '))
        m, row, col = TakeMatrix()
        if choice == 2:
            ShowResult(MultiplyByConstant(m, row, col, input('Enter constant: ')))
        elif choice == 4:
            ShowResult(Transpose(m, row, col, choice2))
        elif choice == 5:
            print('The result is:\n{}'.format(Determinant(m, len(m))))
        else:
            inv = Inverse(m, len(m))
            if inv:
                ShowResult(inv)
            else:
                print("This matrix doesn't have an inverse.")
    else:
        exit(0)
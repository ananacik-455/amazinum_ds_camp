import numpy as np


def simple_solve(A : np.array, B : np.array) -> np.array:
    '''Inversion method to find SLAE solution (X = A^-1 @ B)'''
    return np.linalg.inv(A) @ B


def gause(A: np.array, B: np.array) -> np.array:
    '''Gausing method to find SLAE solution'''
    m = len(B)
    A = np.concatenate((A, B), axis=1).astype(np.float32)
    # forward steps
    for i in range(m):
        A[i] /= A[i][i]
        for j in range(i+1, m):
            A[j] += A[i] * -A[j][i]
    # backward steps
    for i in range(m - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            A[j] += A[i] * - A[j][i]

    return A[:, m].reshape((-1, 1))


def kram(A: np.array, B: np.array) -> np.array:
    '''Kramer method to find SLAE solution'''
    m = len(B)
    det = np.linalg.det(A)
    result = np.zeros((m, 1))
    for i in range(m):
        A_copy = np.copy(A)
        A_copy[:, i] = B.T
        result[i, 0] = np.linalg.det(A_copy) / det
    return result


if __name__ == '__main__':
    A = np.array([[1, 2, 3],
                  [0, 1, 2],
                  [2, 0, 0]])
    B = np.array([[1],
                  [1],
                  [0]])

    # A = np.array([[1, 2, 3, 4],
    #               [0, 1, 2, 3],
    #               [2, 0, 0, 4],
    #               [3, 2, 2, 2]])
    # B = np.array([[1],
    #               [1],
    #               [0],
    #               [6]])

    X_i = simple_solve(A, B)
    X_k = kram(A, B)
    X_g = gause(A, B)

    print(f"Input A: \n {A}\n",
          f"Input B:\n {B}\n"
          f"Solve with inversion:\n {X_i}\n"
          f"Solve with Kramer method:\n {X_k}\n"
          f"Solve with Gause method:\n {X_g}")
import numpy as np

N = 2; M = 3

# 모든 값이 0인 NxM 배열 생성 np.zeros()
zero_mat = np.zeros((N,M))
print(zero_mat, '\n')

# 모든 값이 1인 NxM 배열 생성 np.ones()
one_mat = np.ones((N,M))
print(one_mat, '\n')

# 모든 값이 k인 NxM 배열 생성 np.full()
same_value_mat = np.full((N,M), 7)
print(same_value_mat, '\n')

# 대각선이 3이고 나머지는 0인 2차원 배열 생성 np.eye()
eye_mat = np.eye(3)
print(eye_mat, '\n')

# 임의의 값을 가지는 배열 생성 np.random.random()
random_mat = np.random.random((2,2))
print(random_mat)
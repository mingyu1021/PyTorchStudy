import numpy as np

# np.reshape() 내부 데이터 변경하지 않고 배열의 구조를 바꿈

# 0~29 배열 생성
range_vec = np.arange(30)
# 위 배열을 N행 M열 행렬로 변경
N = 5; M = 6
reshape_mat = np.array(range_vec).reshape((N,M))
print(reshape_mat)
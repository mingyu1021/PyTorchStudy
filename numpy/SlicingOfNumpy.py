import numpy as np

# ndaaray를 통한 다차원 배열은 슬라이싱 기능 지원

# 배열 생성
mat = np.array([[1,2,3],[4,5,6]])
print(mat, '\n')

# 첫번째 행 출력
slicing_mat = mat[0,:]
print(slicing_mat, '\n')

# 두번째 행 출력
slicing_mat = mat[1,:]
print(slicing_mat, '\n')

# 세번째 열 출력
slicing_mat = mat[:,2]
print(slicing_mat)

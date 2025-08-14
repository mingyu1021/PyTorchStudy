import numpy as np

# 1차원 배열 생성
vec = np.array([1,2,3,4,5])
print(vec, '\n')

# 2차원 배열 생성
mat = np.array([[10,20,30], [60,70,80]])
print(mat, '\n')

# 각 배열 타입, 축, 크기 확인
print(f'vec의 타입: {type(vec)}')
print(f'mat의 타입: {type(mat)}\n')

print(f'vec의 축의 개수: {vec.ndim}')
print(f'vec의 크기(shape): {vec.shape}\n')

print(f'mat의 축의 개수: {mat.ndim}')
print(f'mat의 크기(shape): {mat.shape}\n')

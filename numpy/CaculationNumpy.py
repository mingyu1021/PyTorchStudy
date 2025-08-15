import numpy as np

# Numpy는 배열 간 연산 손쉽게 수행 가능 
# + or np.add(), - or np.subtract(), * or np.multiply(), / or divide()
x = np.array([1,2,3])
y = np.array([4,5,6])

# result = np.add(x,y)
result = x + y
print(result)

# result = np.subtract(x,y)
result = x - y
print(result)

# result = np.multiply(result, x)
result = result * x
print(result)

# result = np.divide(result, x)
result = result / x
print(result)

# 벡터와 행렬곱 or 행렬곱 dot()
mat1 = np.array([[1,2],[3,4]])
mat2 = np.array([[5,6],[7,8]])
mat3 = np.dot(mat1, mat2)
print(mat3)

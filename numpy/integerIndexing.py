import numpy as np

# 연속적이지 않은 원소로 배열을 만들 경우 슬라이싱 X
# 이런 경우 인덱싱을 사용하여 배열 구성 가능

# 배열 생성
mat = np.array([[1,2],[4,5],[7,8]])
print(mat)

# N행 M열 원소 (0부터 카운트하므로 N+1번째 행 M+1번째 열)
# 1행 0열(2번째 행 1번째 열)
print(mat[1,0])

# mat[[2행, 1행], [0열, 1열]] -> 2행 0열, 1행 1열 두개의 원소 출력
indexing_mat = mat[[2,1],[0,1]]
print(indexing_mat)
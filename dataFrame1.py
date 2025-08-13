import pandas as pd

# DataFrame
values = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
index = ['one', 'two', 'three']
columns = ['A', 'B', 'C']

df = pd.DataFrame(values, index=index, columns=columns)
print('데이터프레임 출력 : ')
print('-'*18)
print(df)

print('-'*18)
print('Index of DataFrame: {}'.format(df.index))
print('Column name of DataFrame: {}'.format(df.columns))
print('Value of DataFrame:')
print('-'*18)
print(df.values)
print('-'*18)
import pandas as pd
# Series
sr = pd.Series([17000, 18000, 1000, 5000],
               index=["피자", "치킨", "콜라", "맥주"])
print('시리즈 출력 :')
print('-'*18)
print(sr)

print('-'*18)
print('Value of Series: {}'.format(sr.values))
print('Index of Series: {}'.format(sr.index))
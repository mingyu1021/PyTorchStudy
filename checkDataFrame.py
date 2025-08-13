import pandas as pd

# DataFrame
data = {
    '학번' : ['1000', '1001', '1002', '1003', '1004', '1005'],
    '이름' : [ 'Steve', 'James', 'Doyeon', 'Jane', 'Pilwoong', 'Tony'],
    '점수': [90.72, 78.09, 98.43, 64.19, 81.30, 99.14]
}
df = pd.DataFrame(data)
print(df)


# 앞 부분 n개만 보기 df.head(n)
print('~~~~~~~앞 부분 3개~~~~~~~~ \n{}'.format(df.head(3)))

# 뒷 부분 n개만 보기 df.tail(n)
print('~~~~~~~뒷 부분 3개~~~~~~~~ \n{}'.format(df.tail(3)))

# 해당열 확인 df['열이름']
print('~~~~~~~학번 확인~~~~~~~~ \n{}'.format(df['학번']))
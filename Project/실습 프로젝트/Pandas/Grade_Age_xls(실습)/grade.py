import pandas as pd

# excel 파일 읽기
# df1 = pd.read_excel('./Grade_Sample.xlsx', sheet_name='Sheet1')

# url에서 excel 읽기
df = pd.read_excel('https://raw.githubusercontent.com/kibua20/devDocs/master/pandas_example/Grade_Sample.xlsx')
print (type(df))
print (df)
# 출처: https://kibua20.tistory.com/200 [모바일 SW 개발자가 운영하는 블로그:티스토리]
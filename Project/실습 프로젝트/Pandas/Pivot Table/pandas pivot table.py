import pandas as pd
import numpy as np

df = pd.read_csv('cars.csv')
print(df.head())
'''
   YEAR        Make           Model   ...    RATING  (km) TIME (h)
0  2012  MITSUBISHI          i-MiEV   ...       NaN   100        7
1  2012      NISSAN            LEAF   ...       NaN   117        7
2  2013        FORD  FOCUS ELECTRIC   ...       NaN   122        4
3  2013  MITSUBISHI          i-MiEV   ...       NaN   100        7
4  2013      NISSAN            LEAF   ...       NaN   117        7
'''
print(df.columns)
'''
Index(['YEAR', 'Make', 'Model', 'Size', '(kW)', 'Unnamed: 5', 'TYPE',       
        'CITY (kWh/100 km)', 'HWY (kWh/100 km)', 'COMB (kWh/100 km)',       
        'CITY (Le/100 km)', 'HWY (Le/100 km)', 'COMB (Le/100 km)', '(g/km)',       
        'RATING', '(km)', 'TIME (h)'],      
        dtype='object')
'''
# Year와 Make를 기준으로 (kW) 컬럼의 평균값을 구한다.
# 그 다음 피벗 테이블을 만드는 데 index(행) = YEAR, column(열) = Make 로 한다.

pivot = df.pivot_table(values='(kW)', index='YEAR', columns='Make', aggfunc=np.mean)
print(pivot)
'''

Make    BMW  CHEVROLET   FORD     ...      NISSAN  SMART       TESLA
YEAR                              ...                               
2012    NaN        NaN    NaN     ...        80.0    NaN         NaN
2013    NaN        NaN  107.0     ...        80.0   35.0  280.000000
2014    NaN      104.0  107.0     ...        80.0   35.0  268.333333
2015  125.0      104.0  107.0     ...        80.0   35.0  320.666667
2016  125.0      104.0  107.0     ...        80.0   35.0  409.700000

[5 rows x 8 columns]
'''
# aggfunc를 두 개 이상 적용할 수 있다.# margin의 의미는 모든 값을 합산한 값을 보여주는 인덱스를 생성할 지를 결정하는 인자다.
pivot = df.pivot_table(values='(kW)', index='YEAR', columns='Make', aggfunc=[np.mean, np.min], margins=True)
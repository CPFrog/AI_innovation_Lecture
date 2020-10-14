import pandas as pd

dat = pd.read_excel('dict01.xlsx')
print(dat)

print(dat.info() )
print(dat.describe())
print(dat['단어'])
print(dat['뜻'])

print(dat.loc[dat['단어']=='알고리즘', :])

print(dat.loc[dat['단어']=='통계학', :])
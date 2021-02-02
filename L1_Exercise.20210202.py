#!/usr/bin/env python
# coding: utf-8

# Exercise 1 求2+4+6+8+...+100的求和!

# In[2]:


sum = 0
for i in range(0,101,2):
    sum += i 
print(sum)


# Exercise 2 统计全班的成绩
# 在语文、英语、数学中的平均成绩、最小成绩、最大成绩、方差、标准差。然后把这些人的总成绩排序，得出名次进行成绩输出!

# In[33]:


import pandas as pd
from pandas import Series, DataFrame


# In[34]:


data = {'Chinese': [68,95,98,90,80],'Math':[65,76,86,88,90],'English':[30,98,88,77,90]}
df1 = DataFrame(data)
df2 = DataFrame(data, index = ['zhangfei','guanyu','liubei','dianwei','xuchu'],columns = ['Chinese','Math','English'])
print(df2)
print(df2.mean())
print(df2.min())
print(df2.max())
print(df2.var())
print(df2.std())


# In[42]:


def custom_sum(row):
    return row.sum()
df2['SUM'] = df2.apply(custom_sum, axis =1)
sort = df2.sort_values('SUM',ascending = False)
print(sort)


# Exercise 3 对汽车质量数据进行统计

# In[43]:


import pandas as pd
from pandas import Series, DataFrame


# In[53]:


data = pd.DataFrame(pd.read_csv('car_complain.csv'))
df = data.groupby(['brand'])['id'].agg(['count']).sort_values('count',ascending=False) #品牌投诉总数，按照brand对ID进行计数，从大到小排列
df1 = data.groupby(['car_model'])['id'].agg(['count']).sort_values('count',ascending=False) #车型投诉总数
df2 = data.groupby(['brand','car_model'])['id'].agg(['count']).groupby(['brand']).mean().sort_values('count',ascending=False) #品牌的平均车型投诉
print(df)
print(df1)
print('平均车型投诉最多的品牌是',df2.iloc[0].name )


# In[ ]:





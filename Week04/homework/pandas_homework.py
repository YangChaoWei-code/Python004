# -*- coding:utf-8 -*-
"""
@author:YCW
@file:pandas_homework.py
@time:2020/10/25 22:56
"""
'''
作业背景：在数据处理的步骤中，可以使用 SQL 语句或者 pandas 加 Python 库、
函数等方式进行数据的清洗和处理工作。因此需要你能够掌握基本的 SQL 语句和 
pandas 等价的语句，利用 Python 的函数高效地做聚合等操作。
'''
import pandas as pd

df = pd.DataFrame()
# 1.SELECT * FROM data;
df
# 2.SELECT * FROM data LIMIT 10;
df.head(10)
# 3.SELECT id FROM data; // id是data表的特定一列
df['id']
# 4.SELECT COUNT(id) FROM data;
df['id'].count()
# 5.SELECT * FROM data WHERE id < 1000 AND age > 30;
df[(df['id'] < 1000) & (df['age' > 30])]
# 6.SELECT id, COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
df[['id', 'order_id']].groupby('id').count()
# 7.SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
merge(t1, t2, on='id', how='inner')
# 8.SELECT * FROM table1 UNION SELECT * FROM table2;
concat([table1, table2], axis=0, ignore_index=True).drop_duplicates()
# 9.DELETE FROM table1 WHERE id = 10;
table1.drop(table1[table1['id'] == 10].index).reset_index()
# 10.ALTER TABLE table1 DROP COLUMN column_name;
table1.drop('column_name', axis=1)
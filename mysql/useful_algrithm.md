# 一些有效的算法

>  纳税信用等级A 滚动率分析

![A的转移矩阵](Roll_Rate_Analysis.png)

> 连续纳税信用等级A年份数

![A的连续年份](sequence_years_xxx.png)
- year - ROW_NUMBER(): 这是实际的计算部分，其中我们从每个年份中减去其对应的行号。由于行号是按照年份顺序分配的，这意味着对于连续盈利的年份，它们将具有连续的行号，从而产生相同的sequence_id
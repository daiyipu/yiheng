# python 数据清洗的一些使用技巧
> shelf.fillna()使用
- value: 用于填充缺失值的标量值或字典。
- method: 指定填充方法，如 ‘ffill’ 或 ‘bfill’。
    - **待补充**
- axis: 指定填充的轴，默认为 0（按列填充），也可以设置为 1（按行填充）。
- inplace: 布尔值，如果为 True，则直接在原始对象上进行操作，不返回新对象。
- limit: 整数，如果指定，则向前或向后填充时，最多填充这么多连续的 NaN 值。

> pd.series.str.
- contains
  	```
    s = pd.Series(['foo', 'foobar', 'baz'])
	print(s.str.contains('foo'))  # 输出: [True, True, False]
    ```
- replace
	```
    s = pd.Series(['apple', 'banana', 'cherry'])
	print(s.str.replace('a', 'A'))  # 输出: ['ApplE', 'bAnAnA', 'chErry']
    ```
- .split()，.join() 
    ```
    s = pd.Series(['a_b_c', 'd_e_f', 'g_h_i'])
	split_series = s.str.split('_')
	print(split_series)  # 输出: [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
	joined_series = split_series.str.join('-')
	print(joined_series)  # 输出: ['a-b-c', 'd-e-f', 'g-h-i']
    ```
> pd.columns.isin()
- **待补充**
> pd.select_dtypes
- 参数：include，exclude
- 参数的类型： scalar or list-like
- 参数的选项： 
    - 数值型numeric：'np.number' or 'number'
    - 字符型string： 'object'
    - 时间型datetime64： 'np.datetime64','datetime','datetime64'
    - 类别型categorical：'category'
    - 判断bool：'bool'

> 分位数 pandas.Series.quantile()
- 参数：0-1的小数
- 其中numpy也有时限分位数的函数
    - quantile10 = np.quantile(score, q=0.1, method='linear')  # q取值范围[0, 1]
    - percentile10 = np.percentile(score, 10)  # 取值范围[0,100]
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

> pd.cut&pd.qcut
1. pd.cut() 函数的基本用法是将连续型数据按照指定的区间进行切分。例如，你可以使用这个函数将年龄数据分割成不同的年龄段。
    - x: 需要被分割的输入数组，必须是1维的。
    - bins: 分割的依据，可以是整数、标量序列或 IntervalIndex
        - 如果是整数，它定义了在 x 的范围内等宽的桶的数量。
        - 如果是标量序列，它定义了桶的边缘，允许非均匀的宽度
        - 如果是 IntervalIndex，它定义了要使用的确切桶。可以直接用标量序列。
    - right: 布尔值，默认为 True，表示桶是否包含右边缘。
    - labels: 数组或 False，默认为 None，指定返回桶的标签。
    - retbins: 布尔值，默认为 False，表示是否返回桶。
1. pd.qcut() 是 Pandas 库中另一个用于数据分桶的函数，但它与 pd.cut() 有所不同。pd.qcut() 根据数据的分布来划分区间，而不是根据固定的数值范围。这意味着它会根据数据的分位数来创建桶，确保每个桶中有相同数量的数据点。
    - x: 需要被分割的输入数组，必须是1维的。
    - q: 分割的数量，即分位数。这个值应该是介于 0 和 1 之间的数字，或者是一个整数表示将数据分成多少等份。
    - labels: 数组或 False，默认为 None，指定返回桶的标签。
    - retbins: 布尔值，默认为 False，表示是否返回桶的边界值。
    - precision: 整数，默认为 3，表示存储和显示分位数时的精度。
    - duplicates: {‘raise’, ‘drop’}，默认为 ‘raise’，如果分位数导致重复的边界，则如何处理。
    - 示例如下
    ``` {.line-numbers}
    import pandas as pd
    import numpy as np
    # 创建一个包含随机数值的 Series
    data = pd.Series(np.random.randn(1000))
    # 使用 pd.qcut() 将数据分为四份，每个桶中有相同数量的数据点
    quartiles = pd.qcut(data, q=4)
    # 打印结果
    print(quartiles)
    # 查看每个桶的数据点数量
    print(quartiles.value_counts())
    ```
> pd.\_\_version\_\_
  
  查看具体包的版本，这里示例为查看pd的版本
  另外还有查看的方式
  1. `!pip show pandas` 在notebook中查看
  2. `pip show pandas` 在命令行终端查看

> series.items()
  由于版本更新，items基本替代iteritems()，但是目前还兼容
  ```
    series = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
    # 使用iteritems()遍历Series
    print("Iterating over Series with iteritems():")
    for index, value in series.iteritems():
    print(f"Index: {index}, Value: {value}")
  ```
  输出
  ```
    Iterating over Series with iteritems():
    Index: a, Value: 10
    Index: b, Value: 20
    Index: c, Value: 30
    Index: d, Value: 40
    Index: e, Value: 50
  ```

> apply,applymap,map用法
  - apply适用于Series和DataFrame
  - applymap适用于DataFrame，按行（axis=1）还是按列（axis=0，默认值）
  - map 适用于Series

  ```
    df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
    })
  ``` 
  1. applymap 
  '''
  def square(x):
    return x ** 2
  df_applied = df.applymap(square)
  print(df_applied)
  '''
  2. apply
   applied_df = df.apply(lambda x: x.max() - x.min(), axis=0)

>pd.groupby()
 - pct_change()
 - mean()
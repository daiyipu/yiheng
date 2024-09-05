# pandas静态方法
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
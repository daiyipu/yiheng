# 利用matplotlib进行画图操作，操作文档
一、标题
# 这是 <h1> 一级标题
## 这是 <h2> 二级标题
### 这是 <h3> 三级标题
#### 这是 <h4> 四级标题
##### 这是 <h5> 五级标题
###### 这是 <h6> 六级标题

如果你想要给你的标题添加 id 或者 class，请在标题最后添加 {#id .class1 .class2}。例如：

# 这个标题拥有 1 个 id {#my_id}
# 这个标题有 2 个 classes {.class1 .class2}

二、强调

*这会是 斜体 的文字*
_这会是 斜体 的文字_

**这会是 粗体 的文字**
__这会是 粗体 的文字__

_你也 **组合** 这些符号_

~~这个文字将会被横线删除~~



三、列表
（一）无序列表
- Item 1
- Item 2
  - Item 2a
  - Item 2b
（二）有序列表
1. Item 1
1. Item 2
1. Item 3
   1. Item 3a
   1. Item 3b
      6. 

四、添加图片 
![GitHub Logo](/yiheng/markdown/641.webp)
Format: ![Alt Text](/yiheng/markdown/641.webp)

五、引用
正如 Kanye West 所说：

> We're living the future so
> the present is our past.

六、分割线
如下，三个或者更多的

---

连字符

***

星号

___

下划线

七、行内代码
我觉得你应该在这里使用
`<  plt.ylabel(y_label)>` 才对。

八、代码块 序号排序
``` javascript {.line-numbers} 
def plot_bar_chart_with_values(data, labels, title="Bar Chart", x_label="X-axis", y_label="Y-axis"):
    """
    绘制条形图并在每个条形图上显示具体值。

    参数:
    - data (list): 条形图中的数据值列表。
    - labels (list): 每个条形图的数据标签列表。
    - title (str, 可选): 图表的标题。默认为"Bar Chart"。
    - x_label (str, 可选): x轴的标签。默认为"X-axis"。
    - y_label (str, 可选): y轴的标签。默认为"Y-axis"。

    示例:
    plot_bar_chart_with_values([10, 20, 30], ['A', 'B', 'C'])
    """
    fig, ax = plt.subplots()
    bars = ax.bar(labels, data)
```

九、高亮具体某行代码
```javascript {highlight=3-6}
    # 在每个条形图上添加文本
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), 
                ha='center', va='bottom')

    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()
data = [10, 20, 30]
labels = ['A', 'B', 'C']
plot_bar_chart_with_values(data, labels)
```
十、高亮整体代码
``` ruby
require 'redcarpet'
markdown = Redcarpet.new("Hello World!")
puts markdown.to_html
```

十一、你可以给你的代码块设置 class。例如，添加 class1 class2 到一个 代码块：

```javascript {.class1 .class}
function add(x, y) {
  return x + y
}
```
十二、任务列表
- [x] @mentions, #refs, [links](), **formatting**, and <del>tags</del> supported
- [x] list syntax required (any unordered or ordered list supported)
- [x] this is a complete item
- [ ] this is an incomplete item

十三、表格
First Header | Second Header
------------ | -------------
Content from cell 1 | Content from cell 2
Content in the first column | Content in the second 

十四、拓展
1、上标
30^th^  X^2^
2、下表
H~2~O   CO~2~
3、脚注
Content  [^1]
[^1]: Hi! This is a footnote

4、缩略
*[HTML]: Hyper Text Markup Language
*[W3C]: World Wide Web Consortium
The HTML specification
is maintained by the W3C.

5、标记
==marked==

十五、CriticMarkup
CriticMarkup 缺省是禁用的，你可以通过插件设置来启动它。
有关 CriticMarkup 的更多信息，请查看 CriticMarkup 用户指南.

这里有 5 种基本语法：

添加 {++ ++}
删除 {-- --}
替换 {~~ ~> ~~}
注释 {>> <<}
高亮 {== ==}{>> <<}


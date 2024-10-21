### cd作用
cd专门用于切换到具体的文件目录
### 相对路径
相同文件夹内：直接""内写文件名称
./:表示文件所在目录


### python 执行
**python** "./executename.py",注意文件路径必须明确才能够执行

### 使用Switchhosts来修改host
在 C:\Windows\System32\drivers\etc 文件夹中修改host文件的权限，
![host权限](swi_op.png)
在上边的操作之后仍然是没有权限。。尝试把父包的权限也改掉，但是发现仍然不行。
在cmd中进行如下操作
```{.line-numbers}
cd C:\Windows\System32\drivers\etc
attrib -s -h -r hosts
```
![switchhosts 成功写入](sucess.png)
**github成功飞起**
---
### python虚拟环境创建和激活(anaconda版本)
- 查看当前虚拟环境
> conda env list
- 构建新的虚拟环境(anaconda环境下默认路径)
>conda create -n qwenagent python=3.10 pip -y
1. conda: 这是启动 Conda 环境管理器的命令。
2. create: 这是告诉 Conda 你想要创建一个新的环境。
3. -n qwenagent: 这是命令行选项，其中 -n 代表 “name”，用于指定新环境的名称。qwenagent 是你为这个新环境选择的名字。
4. python=3.10: 这是指定新环境中 Python 版本的部分。在这里，它指定了 Python 3.10。
5. pip: 这是在新环境中确保安装 pip 的指示。pip 是 Python 的包管理器，用于安装和管理 Python 包。
6. -y: 这个选项告诉 Conda 自动回答 “yes” 对于所有确认提示。这样，Conda 会在不需要用户交互的情况下继续创建环境。
- 激活虚拟环境
> conda activate qianwen
- 删除虚拟环境
> conda env remove --name python36



class TreeNode:  
    def __init__(self, id):  
        self.id = id  
        self.children = {}  
  
def triples_to_tree(triples):  
    # 创建节点字典  
    nodes = {}  
    for s, p, o in triples:  
        if s not in nodes:  
            nodes[s] = TreeNode(s)  
        if o not in nodes:  
            nodes[o] = TreeNode(o)  
  
    # 构建树形结构  
    root = None  
    for s, p, o in triples:  
        if root is None or s == root.id:  
            # 设置根节点  
            root = nodes[s]  
        nodes[s].children[p] = nodes[o]  
  
    return root
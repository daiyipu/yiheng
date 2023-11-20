import numpy as np
import pandas as pd

# 从树状结构转换到二元组结构
def node_trans(df):
    all_list=[]
    for i in range(df.shape[1]-1):
        for j in range(df.shape[0]):
            # print(i,j)
            h=tuple(str(i))+tuple(df.iloc[j,i:i+2])
            # print(h)
            all_list.append(h)
    set_list=list(set(all_list))
    set_list.sort(key = all_list.index)
    node_list = [i for i in set_list if np.nan not in i]
    return node_list

# 根据二元结构进行树状编号
def node_code(df,chain_code,chain_name,node_code_col='node_code',father_node_name_col='father_node_name',node_name_col='node_name'):
    chain_code=chain_code
    y=1
    for x in df.index:
        if df.loc[x,father_node_name_col]==chain_name:
            df.loc[x,node_code_col]=chain_code+'0'+str(y)
            y=y+1
#             print(node_gcjx_pd.loc[x,node_code_col])
    for x in df.index:
        for z in df.index:
            if df.loc[x,node_name_col]==df.loc[z,father_node_name_col]:
                t=t+1
                if t<10:
                    df.loc[z,node_code_col]=str(df.loc[x,node_code_col])+'0'+str(t)
                else:
                    df.loc[z,node_code_col]=str(df.loc[x,node_code_col])+str(t)
            else:
                t=0
                continue
    return df

# top50关键字匹配和集合
def top_matchkey(df,top_df,node_name_col='node_name',choice_if='if',vocabulary='vocabulary',matchkey='matchkey'):
    # df：二元组数据框
    # top_df：top50的数据框
    # node_name_col：节点名称列名
    # choice_if：top50关键字的选择状态
    # vocabulary：匹配的词汇
    # matchkey：匹配关键字S
    for  m  in df.index:
        vcb_list=[]
        for n in top_df.index:
            while top_df.loc[n,node_name_col]==df.loc[m,node_name_col] and top_df.loc[n,choice_if]==1:
                vcb_list.append(top_df.loc[n,vocabulary])
    #             print(vcb_list)
                break
        vcb_char=','.join(vcb_list)
        df.loc[m,matchkey]=vcb_char
    return df
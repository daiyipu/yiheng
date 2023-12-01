import numpy as np
import pandas as pd


# 从树状结构转换到二元组结构
def tree_to_twuple(df):
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
def node_add_code(df,chain_code,chain_name,node_code_col='node_code',father_node_name_col='father_node_name',node_name_col='node_name'):
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
def add_top_matchkey(df,top_df,node_name_col='node_name',choice_if='if',vocabulary='vocabulary',matchkey='matchkey'):
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

    # 通过一个已知父节点，循环迭代获取子节点。从而遍历出整个节点向下的图谱。
def root_chain(root_list,input_df='triple_pd',node_rank_name='node_col_rank'):
    output_df=pd.DataFrame()#初始化输出的pd
    #root_list：父节点的列表
    #input_df：三元组
    #node_rank_name：节点层级列名
    st_id_list=root_list #数字电路start_concept_id=21798,模拟电路21686,芯片根产业链21859,系统级芯片(SOC)21834，通信SOC21849
    #EDA设计工具21777,半导体材料21710,半导体设备21748；芯片封装21781，芯片测试21782；封装测试21780，芯片IP核设计21778
    for x in range(20):
        en_id_list=st_id_list
        st_id_list=[]
        for m in en_id_list:
            for n in input_df.index:
                if  input_df.loc[n,1]==m:
                    # print(origin_rlt_pd.loc[n,1])   
                    output_df=pd.concat([output_df,input_df[input_df.index==n]])
                    output_df.loc[n,node_rank_name]=x+1
                    st_id_list.append(input_df.loc[n,2])
    return output_df

def triple_to_tree(root_id,input_relation_df='origin_rlt_pd',input_node_df='target_node_chain_pd',node_rank_name='node_col_rank'):
    # 计算三元组形式的树形结构最大层级
    jcdl_level=max(input_node_df[node_rank_name])
    # 计算最大层级
    nodes=set(input_relation_df[1])|set(input_relation_df[2])
    # 三元组转pd树
    z=input_relation_df
    #获取层级列表
    columns=[]
    for j in range(int(jcdl_level+1)):
        t='level'+str(j)
        columns.append(t)
    output_df=pd.DataFrame(columns=columns)
    idx=0#新树pd的行号，
    for i in range(int(jcdl_level+1)):
        if i==0:
            output_df.loc[idx,'level'+str(i)]=root_id
        else:
            for idx in output_df.index:
                for node in nodes:
                    if z[1][z[2]==node].values.size>0 and z[1][z[2]==node].values==output_df.loc[idx,'level'+str(i-1)]:
                        new_row = output_df[output_df.index==idx]#该行值保存
                        output_df=pd.concat([output_df,new_row],ignore_index=True)
                        # output_df=output_df.append(new_row, ignore_index=True)
                        output_df.loc[output_df.index[-1], 'level'+str(i)]=node
                        if np.isnan(output_df.loc[idx,'level'+str(i)]):
                            output_df.loc[idx,'level'+str(i)]=node
                            output_df.drop(output_df.index[-1],inplace=True)
    output_df.sort_values(by=columns,inplace=True)
    output_df.reset_index(drop=True,inplace=True)
    return output_df
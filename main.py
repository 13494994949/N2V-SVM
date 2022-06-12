"""
该过程是对生物网络进行预处理，将网络中第一列和第二列数据都映射为int型，Drug ID随机映射，gene ID 映射为entrez_id
test.csv 存储的整个数据集中基因ID之间对应的关系
./network/DG-Miner_miner-disease-gene.tsv  存储的是一个药物-基因网络数据，第一列是drug ID（可能是字符串），第二列是gene ID（uniprot_id）
./preprocessing/DG-Miner_miner-disease-gene.tsv  用来存储预处理的结果
处理数据的思路如下：
1.Drug ID 直接把字符映射为数字
2.gene ID 通过找对应关系转化为entrez ID
"""
import pandas as pd
import numpy as np

df1 = pd.read_csv('test.csv')
df2 = pd.read_csv('./network/DG-Miner_miner-disease-gene.tsv',sep = '\t')

# # drug转化为int型
df1['entrez_id'] = df1['entrez_id'].fillna(0)
df2['# Disease(MESH)'] = df2['# Disease(MESH)'].str.replace('MESH:D','84')
df2['# Disease(MESH)'] = df2['# Disease(MESH)'].str.replace('MESH:C','83')
df2['# Disease(MESH)'] = df2['# Disease(MESH)'].str.replace('OMIM:','85')

# # #连接两张表
merge = pd.merge(df2,df1,how = 'inner',left_on = 'Gene',right_on ='uniprot_ids' )
# merge = pd.merge(merge,df1,how = 'inner',left_on = 'Protein',right_on ='ensembl_gene_id' )
result = merge[['# Disease(MESH)','entrez_id']].astype('int64')
#
# # #输出
result.to_csv('./preprocessing/DG-Miner_miner-disease-gene.tsv',index = False,sep='\t')




# 下面是一些废弃但可能有用的代码


# 逐行遍历
# print(df2.to_string())
# print(merge[['#Drug','entrez_id']])
# for index,row in df2.iterrows():
#     mask = df1['uniprot_ids'] == row['Gene']
#     row['Gene'] = df1[mask]
#     print(df2[mask].to_string())

# 可能有用
# print(df.loc[df['entrez_id'] == 'foo'])
# print(df.to_string())

#打印表行数
# data = pd.read_csv('all.emb',sep='\t',header = None)
# print(len(data))
# 废弃代码
# data.to_csv('./result/ChG-Miner_miner-chem-gene.tsv',index =False,sep='\t')

# G-G文件加入表头（#gene1，gene2）
# data = pd.read_csv('./result/GG-bio-neuron_top.tsv',sep='\t')
# data.rename(columns={'gene1':'#gene1'}, inplace=True)
# data.to_csv('./result/bio-neuron_top.tsv',index = False,sep='\t')


# 拆分大文件
# 将文件内数据设置为每200,000行迭代一次
# reader = pd.read_table('./preprocessing/bio-neuron_top.tsv',
#                        sep='\t', chunksize=40000000)
# 循环保存文件
# i = 0
# for chunk in reader:
#     file_name ='D:\\lab\\project1\\preprocessing\\GG'+str(i)+'.tsv'
#     print('正在保存第{}个⽂件...'.format(i))
#     chunk.to_csv ( file_name ,index =False,sep='\t')
#     i += 1
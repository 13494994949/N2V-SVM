# N2V-SVM


程序：

all.py   连接所有生物网络

main.py  生物网络数据预处理（节点转化为int）

processData.py得到生物网络中帕金森病相关基因，从而得到正样本

txt文件：

test.csv   是整个数据集中基因 ID 之间的对应关系，用来统一基因ID

all.emb  存储的是10个生物网络连接后的特征（第一列是all_gene)

clinvar_result.txt 存储的是与帕金森相关的基因（只有基因name,需要查GeneID_Name.txt找到对应的ID）

GeneID_Name.txt存储 基因的ID和name的对应关系

文件夹：

abandon  丢弃的生物网络

attributes  node2vec提取的基因特征

GG-NE  多个gene-gene网络（选取其中bio-neuron_top作为代表）

join   10个网络特征合并后的结果

network 多个生物网络数据集

processing 生物网络预处理（node类型转化为int）的结果

#coding=utf-8
"""
该过程是使用4种机器学习方法对疾病基因进行预测，并把评分画成柱状图
处理过程如下
1.筛选正负样本
2.构造模型输出五折交叉验证结果
3.画柱状图
"""
from sklearn import metrics
import numpy as np
import random
import os
import warnings
import matplotlib.pyplot as plt

from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.model_selection import ShuffleSplit
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

# 五折交叉验证得到准确率（accuracy）、精确率（precision）、召回率（recall）、F1_SCORE、AUC
def muti_score(model):
	warnings.filterwarnings('ignore')
	cv = ShuffleSplit(n_splits=5, test_size=0.3, random_state=2018)
	accuracy = cross_val_score(model, x, y, scoring='accuracy', cv=cv)
	precision = cross_val_score(model, x, y, scoring='precision', cv=cv)
	recall = cross_val_score(model, x, y, scoring='recall', cv=cv)
	f1 = cross_val_score(model, x, y, scoring='f1', cv=cv)
	roc_auc = cross_val_score(model, x, y, scoring='roc_auc', cv=cv)
	#画柱状图时的y轴
	model_score.extend((accuracy.mean(),precision.mean(),recall.mean(),f1.mean(),roc_auc.mean()))
	# print(model_score)
	# tree_score.append(precision.mean())
	# forest_score.append(recall.mean())
	# lr_score.append(f1.mean())

	# print("第{}次".format(t+1))
	print("accuracy:", "%.4f"%accuracy.mean())
	print("precision:","%.4f"%precision.mean())
	print("recall:","%.4f"%recall.mean())
	print("f1:", "%.4f"%f1.mean())
	print("roc_auc:", "%.4f"%roc_auc.mean())


model_score = []  #所有模型得分，切割后得到各个模型得分
svm_score = []    # svm得分 （5个指标）
tree_score = []   # 决策树得分 （5个指标）
forest_score = [] # 随机森林得分 （5个指标）
lr_score = []     # 逻辑回归得分 （5个指标）

#先选取正负样本
all_gene=set()
for lines in open(r"all.emb","r",encoding="utf_8_sig"):
    line=lines.strip().split(" ")
    all_gene.add(line[0])
    # all_gene.add(line[1])
positive=set()
for lines in open(r"parkinson_gene.txt","r"):
	line=lines.strip().split("\t")
	positive.add(line[0])


all_negtive=all_gene-positive

all_negtive=list(all_negtive)

# final=[]
# final_clf = []
# final_accuracy = []
# final_precision = []
# final_recall = []
# final_f1= []
# final_roc_auc= []

# for t in range(20):
random.shuffle(all_negtive)
negtive=all_negtive[:len(positive)]



dict_emb={}
for lines in open("all.emb","r",encoding="utf_8_sig"):
	line=lines.strip().split(" ")
	list1=[]
	for l in line[1:]:
		list1.append(float(l))
	dict_emb[line[0]]=list1


positive_emb=[]
for p in positive:
	positive_emb.append(dict_emb[p])


negtive_emb=[]
for n in negtive:
	negtive_emb.append(dict_emb[n])

emb=positive_emb+negtive_emb
emb=np.array(emb)

postive_label=[]
negtive_label=[]
for i in range(len(positive)):
	postive_label.append(1)
	negtive_label.append(0)

label=postive_label+negtive_label
label=np.array(label)

y = label
x = emb
#构建模型
lr = LogisticRegression()

tree = DecisionTreeClassifier()

svm = SVC(probability=True, gamma="auto")

forest = RandomForestClassifier(n_estimators=100)
# clf = svm.SVC(probability=True, gamma="auto")


model_name = ["svm", "tree", "forest", "lr"]
for name in model_name:
	outcome = eval(name)
	print(name)
	muti_score(outcome)




# 下面是对评分画柱状图

# size = 5
# 返回size个0-1的随机数
# a = np.random.random(size)
# b = np.random.random(size)
# c = np.random.random(size)
svm_score = model_score[0:5]
# print (svm_score)# svm得分 （5个指标）
tree_score = model_score[5:10]
forest_score = model_score[10:15]
lr_score = model_score[15:20]

## 各个模型的auc，f1值
# 	accuracy_score.append(accuracy)
# 	precision_score.append(precision)
# 	recall_score.append(recall)
# 	f1_score.append(f1)
# 	roc_auc_score.append(roc_auc)
## x轴标签
x_label = ["accuracy", "precision", "recall", "f1", "roc_auc"]
# x轴刻标
x = np.arange(len(x_label))
# 有4种类型的数据，n设置为4
total_width, n = 0.8, 4
# 每种类型的柱状图宽度
width = total_width / 4

# 重新设置x轴的坐标
x = x - (total_width - width) / 2
print(x)

# 画柱状图
plt.bar(x,svm_score, width=width, label="svm")
plt.bar(x + width, tree_score, width=width, label="tree")
plt.bar(x + 2*width, forest_score, width=width, label="forest")
plt.bar(x + 3*width, lr_score, width=width, label="lr")
#显示具体数值
for i, j in zip(x, svm_score):
    plt.text(i, j + 0.01, "%.4f" % j, ha="center", va="bottom", fontsize=7)
# for i, j in zip(x + width, tree_score):
#     plt.text(i, j + 0.01, "%.4f" % j, ha="center", va="bottom", fontsize=7)
# for i, j in zip(x + 2 * width, forest_score):
#     plt.text(i, j + 0.01, "%.4f" % j, ha="center", va="bottom", fontsize=7)
# for i, j in zip(x + 2 * width, lr_score):
#     plt.text(i, j + 0.01, "%.4f" % j, ha="center", va="bottom", fontsize=7)
#显示x轴标签
plt.xticks(x + 0.3, x_label)
# 显示图例
plt.legend(bbox_to_anchor=(0.95,1.12), ncol=4)
# 显示柱状图
plt.show()
# plt.savefig(fname="./model.png", dpi=100)












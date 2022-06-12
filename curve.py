import os

# 消融实验，去掉某个网络并把剩余网络融合，用各个融合网络的AUC值画出柱状图（这里是画图代码，融合网络的方式是用all.py手动删除一个网络并把剩余的网络融合）

import matplotlib.pyplot as plt
import numpy as np
# 改变绘图风格
import seaborn as sns

sns.set(color_codes=True)

cell = ['all','DG-AssocMiner','DG-Miner','GF-Miner','GG-EnhancedTissue','GP-Miner','PP-Decagon','PP-Pathways','ChG-InterDecagon','ChG-Miner','ChG-TargetDecagon',]
pvalue = [0.943444621901216,0.9357394304917918,0.9690554602506255,0.9319883369882153,0.9541650291693502,0.8718624424736576,0.9380053042817174,0.9693077968963479,0.9762571021310492,0.9483230675656671,0.9070324037461557]

width = 0.60
index = np.arange(len(cell))

p1 = np.arange(-0.5, len(cell), 0.01)
p2 = 0.943444621901216 + p1 * 0
#
# q1 = np.arange(0, len(cell), 0.01)
# q2 = 0.1 + p1 * 0

# figsize = (10, 8)  # 调整绘制图片的比例
plt.plot(p1, p2, color='red', label='all scores')  # 绘制直线
# plt.plot(q1, q2, color='yellow', label='10% significance level')  # 绘制直线
# 若是不想显示直线，可以直接将上面两行注释掉
plt.bar(index, pvalue, width, color="#87CEFA")  # 绘制柱状图
# plt.xlabel('cell type') #x轴
plt.ylabel('AUC')  # y轴
for i, j in zip(index, pvalue):
    plt.text(i, j + 0.01, "%.4f" % j, ha="center", va="bottom")
# plt.title('多元生物网络疾病预测评分')  # 图像的名称
plt.xticks(index, cell)  # 将横坐标用cell替换,fontsize用来调整字体的大小
plt.legend()  # 显示label
plt.show()
# plt.savefig('test.png', dpi=400)  # 保存图像，dpi可以调整图像的像素大小
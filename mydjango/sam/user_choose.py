import numpy


import numpy as np

# 余弦相似度计算
def cos_sim(vector_a, vector_b):

    vector_a = np.mat(vector_a)
    vector_b = np.mat(vector_b)
    num = float(vector_a * vector_b.T)
    denom = np.linalg.norm(vector_a) * np.linalg.norm(vector_b)
    cos = num / denom
    sim = 0.5 + 0.5 * cos
    return sim

# 用户特征向量计算
def user_vec(mat,name_dic,spot_names):
    v=numpy.zeros(len(mat[0]))
    for name in spot_names:
        i=name_dic[name]
        v+=mat[i]
    v=v/[len(spot_names)]
    return v                  # 返回用户特征向量

# 生成用户兴趣景点
# 景点特征矩阵，用户特征，数量
def user_spot(mat,user_v,n):
    i_sim= {}                     # 景点索引余弦相似度计算
    for i in range(len(mat)):
        s=cos_sim(mat[i],user_v)
        i_sim[i]=s

    si_sim=dict(sorted(i_sim.items(), key=lambda item: item[1], reverse=True))
    spos=[]
    for key,value in si_sim.items():
        spos.append(key)
        if(len(spos)==n):
            break
    return spos                     # 返回用户兴趣景点
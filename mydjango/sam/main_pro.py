from .data_process import *
from .lda import *
from .tfidf import *
from .load_spot import *
from .user_choose import *
from .load_routes import *


# 旅游推荐算法主体
def tra_rec(in_spots,n):
    print("This is project belong to sam")

    ##########第一部分，用户兴趣景点产生###############

    # 载入数据并训练
    # all_wd=all_words('北京数据\\北京景点评论总.txt')
    # wdic,weight_mat=tfidf_vc(all_wd)
    # #训练lda模型
    # lda_model(weight_mat)

    # 加载lda模型
    docres = load_lda_doc()

    # 载入景点信息
    name, adre, score, ltd = load_sp()
    # 景点与索引对应的词典
    name_dic = {k: v for v, k in enumerate(name)}
    # 对输入景点列表进行处理
    v = user_vec(docres, name_dic, in_spots)

    # 输出景点列表
    out_spots_i = user_spot(docres, v, n)

 
    #############第二部分，推荐路线产生#########################

    # 加载旅游路线
    route = load_route('mydjango/sam/北京数据/北京旅游路线.txt')
    order_mat = spot_mat(name,route)                      # 路线次序矩阵
    # 建立景点得分字典并排序
    spot_score = {}
    for i in out_spots_i:
        spot_score[i] = score[i]
    sspot_score=dict(sorted(spot_score.items(), key=lambda item: item[1], reverse=True))
    # 对景点进行处理
    sp_over = {}               # 景点是否已经处理完成过
    for spot_i in out_spots_i:
        sp_over[spot_i] = False
    out_route_i = list()                                                # 输出路线列表
    out_route_i.append(list(sspot_score.items())[0][0])             # 第一个景点取评分最高的
    sp_over[list(sspot_score.items())[0][0]] = True               # 第一个景点标记为处理过
    # 处理其余景点
    for d in range(n-1):
        now_i = out_route_i[-1]
        route_score = {}
        for spot_i in out_spots_i:
            if sp_over[spot_i]:
                route_score[spot_i] = 0
            else:
                route_score[spot_i] = order_mat[now_i][spot_i] * 0.9 + float(spot_score[spot_i]) * 0.1           #得分计算
        sroute_score = dict(sorted(route_score.items(), key=lambda item: item[1], reverse=True))
        res_i = list(sroute_score.items())[0][0]               # 取评分最高的
        out_route_i.append(res_i)
        sp_over[res_i] = True
  
    print (out_spots_i)
    print (out_route_i)
    # 返回景点路线及地址经纬度
    out_routes =[]
    out_routes_addr = []
    out_routes_ltd = []
    for i in out_route_i:
        out_routes.append(name[i])
        out_routes_addr.append(adre[i])
        out_routes_ltd.append(ltd[i])

    return out_routes,out_routes_addr,out_routes_ltd


if __name__ == '__main__':
    tra_rec(['北京杜莎夫人蜡像馆','戒台寺','北京西山国家森林公园'],20)
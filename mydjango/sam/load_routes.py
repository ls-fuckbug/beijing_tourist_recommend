#加载收集了旅游路线信息

# 加载景点信息
# 输入路径
def load_route(path):
    #打开待处理文件
    file=open(path, 'r', encoding='utf-8', errors='ignore')         ##############
    route=[]
    for line in file:
        r=[]
        r=line.split()
        route.append(r)
    file.close()

    return route                          #景点序列


#根据景点名和路线建立景点先后矩阵
# 输入景点名和路线
def spot_mat(name,routes):
    name_dic={k: v for v, k in enumerate(name)}
    
    n = len(name)
    order_mat=[]                       #景点先后矩阵   order_mat[i][j] 表示i景点之后去j景点有多少次
    for i in range(n):
        order_mat.append([])
        for j in range(n):
            order_mat[i].append(0)
    
    for r in routes:
        for i in range( len(r)-1 ):
            if(r[i] in name_dic and r[i+1] in name_dic ):
                order_mat[ name_dic[r[i]] ][ name_dic[r[i+1]] ] += 1
    
    return order_mat           #返回景点先后矩阵
    
    
if __name__ == '__main__':
    route = load_route('mydjango/sam/北京数据/北京旅游路线.txt')
    



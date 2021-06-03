#加载景点信息

# 返回景点名，景点地址，景点得分，经纬度信息列表
def load_sp():
    s_file=open('mydjango/sam/北京数据/北京景点名称.txt', 'r', encoding='utf-8', errors='ignore')
    a_file=open('mydjango/sam/北京数据/北京景点地址.txt', 'r', encoding='utf-8', errors='ignore')
    c_file=open('mydjango/sam/北京数据/北京景点评分.txt', 'r', encoding='utf-8', errors='ignore')
    l_file=open('mydjango/sam/北京数据/北京景点经纬度信息.txt', 'r', encoding='utf-8', errors='ignore')
    name=[]
    adre=[]
    score=[]
    ltd=[]

    for line in s_file:
        line=line.strip()
        name.append(line)
    for line in a_file:
        line=line.strip()
        adre.append(line)
    for line in c_file:
        line=line.strip()
        line=line.rstrip(' 分')
        score.append(line)
    for line in l_file:
        line = line.strip()
        lat_lon = line.split()
        ltd.append(lat_lon)

    return name,adre,score,ltd             #景点名，景点地址，景点得分 经纬度信息


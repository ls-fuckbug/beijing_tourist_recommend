# 数据处理
import jieba

stpwrdpath = "stop_words.txt"  # 停用词


# 判断汉字
def is_chinese(uchar):
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return True
    else:
        return False


# 保留汉字
def chinese_str(content):
    chin_str = ''
    for w in content:
        if is_chinese(w):
            chin_str += w
    return chin_str


# 文本分词
def cut(content):
    split_words = list(jieba.cut(content, cut_all=False))
    return split_words


# 去除停用词
def drop_stopwords(content, path=stpwrdpath):
    # 从文件导入停用词表

    stpwrd_dic = open(stpwrdpath, 'r', encoding='utf-8')
    stpwrd_content = stpwrd_dic.read()
    stpwrd_dic.close()
    # 将停用词表转换为list
    stpwrdlst = stpwrd_content.splitlines()

    # 去掉停用词
    content_clean = []
    for wd in content:
        if wd in stpwrdlst:
            continue
        content_clean.append(wd)
    return content_clean


# 句子处理
def data_word(content):
    chinese = chinese_str(content)  # 取出汉字
    words = cut(chinese)  # 分词
    clean_words = drop_stopwords(words)  # 去停用词
    return clean_words


# 打开总评论集    返回评论集合
def all_words(path):
    print('开始处理数据')
    com_set = open(path, 'r', encoding='utf-8', errors='ignore')
    all_wd = []

    ls_str = ''
    str = ''
    for line in com_set:
        line = line.strip()  # 去除空行
        s_com = line.split(',', 1)

        if (len(s_com) < 2):
            continue
        if (s_com[0] == ls_str):
            str += ' ' + s_com[1]
        else:
            if (str != ''):
                all_wd.append(data_word(str))
            str = s_com[1]
            ls_str = s_com[0]
    # 添加最后一个
    all_wd.append(data_word(str))
    print("景点数目为：", len(all_wd))
    print('数据处理完成')
    return all_wd





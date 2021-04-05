from sklearn import feature_extraction  
from sklearn.feature_extraction.text import TfidfTransformer  
from sklearn.feature_extraction.text import CountVectorizer  


#生成tf-idf向量
def tfidf_vc(data_words):
    print('开始生成tf_idf向量')
    #转换以便利用
    corpus=[]
    for data in data_words:
        str=''
        for word in data:
            str=str+word+' '
        corpus.append(str)
    #print(corpus)
    #生成tf_idf向量
    vectorizer=CountVectorizer()#该类会将文本中的词语转换为词频矩阵，矩阵元素a[i][j] 表示j词在i类文本下的词频  
    transformer=TfidfTransformer()#该类会统计每个词语的tf-idf权值  
    tfidf=transformer.fit_transform(vectorizer.fit_transform(corpus))#第一个fit_transform是计算tf-idf，第二个fit_transform是将文本转为词频矩阵  
    word=vectorizer.get_feature_names()#获取词袋模型中的所有词语  
    weight=tfidf.toarray()#将tf-idf矩阵抽取出来，元素a[i][j]表示j词在i类文本中的tf-idf权重  
    print('成功生成tf-idf向量')
    return word,weight               #词典以及tf-idf矩阵




import pytesseract
#from PIL import Image
from PIL import ImageGrab
import os
import win32api
from bs4 import BeautifulSoup
import requests
import re
#from PIL import ImageEnhance
import jieba
import jieba.analyse
import numpy as np
import time
region_q=(25,120,600,250)#西瓜问题区域  冲顶25,150,600,250芝士25,120,600,220
region_a=(50,250,500,415)#西瓜答案区域50,300,400,620   冲顶50,250,500,415知识25,220,500,430
counts=["","",""]#搜索统计数量

# start=time.time()
question=""
question_better=""
answer=[]
search_url_b="http://www.baidu.com/s?wd="
search_url_s="http://www.sogou.com/web?query="
question_list=[]#问题分词提取
# end=time.time()
# print(str(end))
def orc_q(img):
    text = pytesseract.image_to_string(img,lang="chi_sim")
    if text != "":
        t=text.split("\n")
        while "" in t:
            t.remove("")
        for k in range(len(t)):
            t[k]=t[k].replace(" ","")
        global question
        if len(t)==1:
            question=t[0]
        else:
            question=t[0]+t[1]
        question=question[2:-1]
        try:
            question.remove(".")
        except:
            pass

def orc_a(img):
    text=pytesseract.image_to_string(img,lang="chi_sim")
    global answer
    if text!="":
        try:
            t=text.split("\n")
        except:
            pass
        while "" in t:
            t.remove("")
        for k in range(3):
            t[k]=t[k].replace(" ","")
            answer.append(t[k])

def search_url(url,answer):
    answer[0]="<em><!--red_beg-->"+answer[0]+"<!--red_end--></em>"
    answer[1] = "<em><!--red_beg-->" + answer[1] + "<!--red_end--></em>"
    answer[2] = "<em><!--red_beg-->" + answer[2] + "<!--red_end--></em>"

    count=np.array([0,0,0])
    index=["A","B","C"]
    r=requests.get(url)
    content=r.text
    # print(content)
    soup=BeautifulSoup(content,"lxml")
    content_em=soup.select("em")
    content_em=str(content_em)
    content_str="".join(content_em)
    counts_result=len(content_em)
    print(answer)
    # print(content_em)

    if counts_result==0:
        counts_result=1
    # print(re.findall("<em>" + answer[0] + "</em>", content_str))
    count[0]=len(re.findall(answer[0],content_str))
    count[1]=len(re.findall(answer[1],content_str))
    count[2]=len(re.findall(answer[2],content_str))
    print("A:%d\nB:%d\nC:%d" % (count[0],count[1],count[2]))
    max_index=np.argmax(count)
    min_index=np.argmin(count)
    print("""首选答案:%s,%s\n备选答案:%s,%s""" % (index[max_index],answer[max_index],index[min_index],answer[min_index]))
    return count
def question_better(question):
    # if "《" in question:
    #     a=re.findall(r"\u300a[\u4e00-\u9fa5]\u300b",question)
    if len(question)<10:
        num=3
    elif len(question)<20:
        num=4
    else:
        num=5
    seg_list=jieba.analyse.extract_tags(question,topK=num,withWeight=False,allowPOS=())
    try:
        seg_list.remove("下列")

    except:
        pass

    return seg_list

# def answer_better(answer):
#     for i in np.arange(3):
#         seg_list=jieba.analyse.extract_tags(question,topK=2)
#     print(seg_list)
#     return seg_list

# start=time.time()
test=input("输入enter开始")
img_q=ImageGrab.grab(region_q)
img_a=ImageGrab.grab(region_a)
#img_q.show()
#img_a.show()

orc_q(img_q)
orc_a(img_a)
# end=time.time()
# print(end)
question_list=question_better(question)
# answer=answer_better(answer)
#win32api.ShellExecute(0, "open", "http://www.baidu.com/s?wd=" +question,"","",1)
print(question_list,answer)
question_seacher="%20".join(question_list)
answer_seacher="%20".join(answer)
print(search_url_b+question_seacher+"%20"+answer_seacher)
win32api.ShellExecute(0, "open", search_url_s+question_seacher+"%20"+answer_seacher, "", "", 1)

# start=time.time()
search_url(search_url_s+question_seacher+"%20"+answer_seacher,answer)
# end=time.time()
# print(end)

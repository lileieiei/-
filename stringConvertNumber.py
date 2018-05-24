import re
import sys

url=r"C:\Users\Administrator\Desktop\mission\理财通鉴\理财通鉴摘录.txt"
chs_arabic_map = {'零':0, '一':1, '二':2, '三':3, '四':4,'五':5, '六':6, '七':7, '八':8, '九':9,'十':10, '百':100, '千':10 ** 3, '万':10 ** 4,'〇':0, '壹':1, '贰':2, '叁':3, '肆':4,'伍':5, '陆':6, '柒':7, '捌':8, '玖':9,'拾':10, '佰':100, '仟':10 ** 3, '萬':10 ** 4,'亿':10 ** 8, '億':10 ** 8, '幺': 1,'０':0, '１':1, '２':2, '３':3, '４':4,'５':5, '６':6, '７':7, '８':8, '９':9}
def openfile(url):
    f=open(url)
    str=f.read()
    f.close()
    return str

def findNum(str):
    pos=[]
    chineseNum=[]
    numpattern=re.compile(r"[一二三四五六七八九零十百千万]{3,}")
    numA=numpattern.search(str,0)
    print(numA)
    while numA is not None:
        chineseNum.append(numA.group())
        pos.append([numA.start(),numA.end()])
        numA=numpattern.search(str,pos[-1][-1])
    return (chineseNum,pos)
#整体思路：strUnit表示输入的中文数字字段
#将整个分析分成三部分，以万
def chinese2alb(strUnit):
    result=[0,0,0]

    tmp=0
    for count in range(len(strUnit)):
        curr_char=strUnit[count]
        current_digital=chs_arabic_map.get(curr_char,None)

        if current_digital<=9:
            tmp=current_digital


        elif current_digital<10**4 and current_digital>9:
            result[0]=result[0]+current_digital*tmp
            tmp=0
        elif current_digital>=10**4 and current_digital<10**8:
            result[1]=result[0]+tmp
            result[0]=0
            tmp=0
        else:
            result[2]=result[0]
            result[0]=0
            tmp=0
        print(current_digital, result)
    end=result[0]+result[1]*10000+result[2]*10**8+tmp
    return end

result=[]
text=openfile(url)
(chineseNum,position)=findNum(text)
for i in range(len(chineseNum)):
    result.append(chinese2alb(chineseNum[i]))
print(findNum(text))
text_list=list(text)
for j in range(len(position)-1,0,-1):
    print(len(position))
    print(position[856])
    text_list.insert(position[j][1],"("+str(result[j])+")")
text2="".join(text_list)
doc=open('out.txt','w')
print(text2,file=doc)
doc.close()










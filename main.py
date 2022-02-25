#--coding:UTF-8--
from tkinter import *
from tkinter import ttk
from tkinter import filedialog,messagebox
from tkinter.ttk import Scrollbar,Checkbutton,Label,Button
import cx_Oracle
import os
import sys
import xml.etree.ElementTree as ET
import re
import time
import xlrd
import copy

os.environ['NLS_LANG']='SIMPLIFIED CHINESE_CHINA.UTF8'

class information:
    def __init__(self,input):
        self.input=input
        self.output=None

    def get_result(self):
        return self.output
    
class get_xml(information):
    def __init__(self,bms_url,bms_port,bms_name,bms_user,bms_pass,sql):
        super().__init__(bms_url)
        self.bms_url=bms_url
        self.bms_user=bms_user
        self.bms_pass=bms_pass
        self.bms_port=bms_port
        self.bms_name=bms_name
        self.sql=sql
        self.output=None
        #self.get_xml_info()
        self.get_test_output()



    def get_xml_info(self):
        tns=cx_Oracle.makedsn(self.bms_url,self.bms_port,service_name=self.bms_name)
        db=cx_Oracle.connect(self.bms_user,self.bms_pass,tns)
        try:
            cr=db.cursor()
            cr.execute(self.sql)
            self.output=cr.fetchall()
            for i in self.output:
                
                if i[-1]!=None:
                    tmp_list_tuple=list(i)
                    
                    tmp_list_tuple[-1]=i[-1].read()
                    index=self.output.index(i)
                    self.output[index]=tuple(tmp_list_tuple)
                    #print(i)
            
        except Exception as e:
            print(e)
        finally:
            db.close()
            if self.output==None:
                print("cant find any data")
            #print(self.output)
            
    def get_test_output(self):
        self.output=[('20220224172101', '00000000000000073460', '100001000000002202202241020699189', 'CIM.004.002', '{H:00110000100000010000110000120220224172100CIM.004.002         00000000000000073461                    D3N000029145E336785E8B5619DAA46C569CC1CA5DE6DE30A243D1CFD7ABA9296A556A0E5BF         }\r\n<?xml version="1.0" encoding="UTF-8"?><Document><MainBody><MsgId><Id>100001000000002202202241020699189</Id><CreDtTm>2022-02-24T17:21:00</CreDtTm></MsgId><OrgnlMsgId><Id>100001000000002202201201020697266</Id><CreDtTm>2022-01-20T10:26:02</CreDtTm></OrgnlMsgId><SgnPsnInf><AppBrId>100001</AppBrId><NoDrtPtcptInf><Name>必蚊凄捷鞑吮徙舶乓忘嘴易</Name><SocCode>92399703726078958W</SocCode><DistTp>DT02</DistTp><BrAcctInf><AcctName>必蚊凄捷鞑吮徙舶乓忘嘴易</AcctName><Acct>0200000319201967739</Acct><OpenBrId>000000002</OpenBrId></BrAcctInf></NoDrtPtcptInf></SgnPsnInf><SgntrMk><PrxySgntr>PS01</PrxySgntr><PtcptSgntr>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</PtcptSgntr></SgntrMk><SgnUpInf><Dt>2022-02-24<
 /Dt><SgnUpMk>SU00</SgnUpMk><SgnUpCode>CP06</SgnUpCode><OtherInf>123</OtherInf></SgnUpInf></MainBody><PtcptSgntr>MEUCIQC3Eb+oWhndoU9ZzK0WTv4diOOBVU7gjTaBDgziy6OBAwIgF8mHYcmMxhsBg89kGDKJN1DxM+wlgckioLed0PZSzbU=</PtcptSgntr></Document>', None), ('20220222102903', '00000000000000073202', '100001000000002202202221020699060', 'CIM.004.002', '{H:00110000100000010000110000120220222102903CIM.004.002         00000000000000073203                    D3N00002884965A0E06862063978C98D90D0A4137DECAC21383AB9DDBCD4E1B2FE6BFD8C16D         }\r\n<?xml version="1.0" encoding="UTF-8"?><Document><MainBody><MsgId><Id>100001000000002202202221020699060</Id><CreDtTm>2022-02-22T10:29:03</CreDtTm></MsgId><OrgnlMsgId><Id>100001000000002202201201020697266</Id><CreDtTm>2022-01-20T10:26:02</CreDtTm></OrgnlMsgId><SgnPsnInf><AppBrId>100001</AppBrId><NoDrtPtcptInf><Name>必蚊凄捷鞑吮徙舶乓忘嘴易</Name><SocCode>92399703726078958W</SocCode><DistTp>DT02</DistTp><BrAcctInf><AcctName>必蚊凄捷鞑吮徙舶乓�
 � �嘴易</AcctName><Acct>0200000319201967739</Acct><OpenBrId>000000002</OpenBrId></BrAcctInf></NoDrtPtcptInf></SgnPsnInf><SgntrMk><PrxySgntr>PS01</PrxySgntr><PtcptSgntr>MIIGEgYJKoZIhvcNAQcCoIIGAzCCBf8CAQExCzAJBgUrDgMCGgUAMIIB6AYJKoZI\nhvcNAQcBoIIB2QSCAdUxMTAwMDAwMDA0NTcyMTAwMDAwMDAzODI8P3htbCB2ZXJz\naW9uPSIxLjAiIGVuY29kaW5nPSJnYjIzMTIiPz48VHJhZGVEYXRhPjxmaWVsZCBu\nYW1lPSLX3LHKyv0iIHZhbHVlPSIxIiBEaXNwbGF5T25TY3JlZW49IlRSVUUiLz48\nZmllbGQgbmFtZT0i19y98LbuIiB2YWx1ZT0iMiwzMDIuMDDUqiIgRGlzcGxheU9u\nU2NyZWVuPSJUUlVFIi8+PGZpZWxkIG5hbWU9IrXHwrxJRCIgdmFsdWU9IjY1MS5j\nLjAyMDAiIERpc3BsYXlPblNjcmVlbj0iVFJVRSIvPjxmaWVsZCBuYW1lPSKy2df3\nyrG85CIgdmFsdWU9IjIwMjIwMjIyMTAyMzMzOTYyNjMzMDE2MjIiIERpc3BsYXlP\nblNjcmVlbj0iVFJVRSIvPjxmaWVsZCBuYW1lPSKy2df3IiB2YWx1ZT0ivty++CIg\nRGlzcGxheU9uU2NyZWVuPSJUUlVFIi8+PC9UcmFkZURhdGE+MjIwMDAwMDAwMDM5\n19yxysr9o7oxo6zX3L3wtu6jujIsMzAyLjAw1KoouaTJzNL40NApMjMwMDAwMDAw\nMDAwoIIDDjCCAwowggHyoAMCAQICChuSyhAlVgADNQowDQYJKoZIhvcNAQEFBQAw\nOzEfMB0GA1UEAxMWSUNCQyBUZXN0IENvc
 nBvc mF0ZSBDQTEYMBYGA1UEChMPdGVz\ndGljYmMuY29tLmNuMB4XDTIyMDEwNjA5MDMwOVoXDTI3MDEwNjA5MDMwOVowPjET\nMBEGA1UEAwwKNjUxLmMuMDIwMDENMAsGA1UECwwEMDIwMDEYMBYGA1UECgwPdGVz\ndGljYmMuY29tLmNuMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQD3w8yiYQOw\n64tAPMcICO5BTOYPHMfCPnHhe5kGM01U7GN+HzaC3Iiwcd5Hrbjg021E0fvkvqj4\nySpdlD7mnJALLW/ugtCu+Q8EKyzIs6bf9kcY1+i08cdf5QCbypTVzhwUzq8L/eZ2\nhvNKF/YY+dmlncU3pSHmqKTsW1vJTt2JOQIDAQABo4GQMIGNMB8GA1UdIwQYMBaA\nFER9t5AsN6TZ7WzipIdXZwq18E0UMEsGA1UdHwREMEIwQKA+oDykOjA4MQ4wDAYD\nVQQDDAVjcmw0MzEMMAoGA1UECwwDY3JsMRgwFgYDVQQKDA90ZXN0aWNiYy5jb20u\nY24wHQYDVR0OBBYEFJmqzK3zku4F1k7Btti3zD+P3dkKMA0GCSqGSIb3DQEBBQUA\nA4IBAQBcWLtH6eO+XGv1B744bMgHZFzYfAzAD6jv+kMfrIXoDHtvo/BmRFTYAncq\nSb9oe9gJub5eB1/b82CZN5m+rM7bxoa8t0pz+q9zmyBV4ctGHYUE9lbtcCSepsX5\nR/h71VCEfx6Sw1rjDPzDM/c7kzPDX31M3gr3E6MfFJvKKaIPFbZWX7XA+qRCGZGF\nBMQMAK2uZ1DzOv6poJTc+TG3Vn+HMkwSA4y1gflisBbvC41stUwXbn9c6AUbbjcR\nqymHrvFZR7L5kuy9mx92MLhRdJJA6gXSPnheYP9b4b/hX67fgBXMg1V6JCli/Seu\nlWPBBLHZGJIudYXu5MD3KujkQzH1MYHuMIHrAgE
 BMEkw OzEfMB0GA1UEAxMWSUNC\nQyBUZXN0IENvcnBvcmF0ZSBDQTEYMBYGA1UEChMPdGVzdGljYmMuY29tLmNuAgob\nksoQJVYAAzUKMAkGBSsOAwIaBQAwDQYJKoZIhvcNAQEBBQAEgYCx9y6RaCFyxV9W\nigupgc3uPupBseY3gPdW</PtcptSgntr></SgntrMk><SgnUpInf><Dt>2022-02-22</Dt><SgnUpMk>SU01</SgnUpMk><SgnUpCode>CP06</SgnUpCode><OtherInf>123</OtherInf></SgnUpInf></MainBody><PtcptSgntr>MEUCIQCD6b1ZwbG4WCd22VpCEzH/8bZaB+zu3mjHygqZVCNjQQIgOOgX7oB+QzS5lYnCuH6D/ZSPdZel/S5koZJOtKrec3k=</PtcptSgntr></Document>', None), ('20220222100641', '00000000000000073108', '100001000000002202202221020699013', 'CIM.004.002', '{H:00110000100000010000110000120220222100640CIM.004.002         00000000000000073109                    D3N000028848F81D2CEC0AC69EEF19A3A0D40256BAD2E84FEBC1596D57E745EFF72E94CE50F         }\r\n<?xml version="1.0" encoding="UTF-8"?><Document><MainBody><MsgId><Id>100001000000002202202221020699013</Id><CreDtTm>2022-02-22T10:06:40</CreDtTm></MsgId><OrgnlMsgId><Id>100001000000002202201201020697266</Id><CreDtTm>2022-01-20T10:26:02</C
 reDtTm ></OrgnlMsgId><SgnPsnInf><AppBrId>100001</AppBrId><NoDrtPtcptInf><Name>必蚊凄捷鞑吮徙舶乓忘嘴易</Name><SocCode>92399703726078958W</SocCode><DistTp>DT02</DistTp><BrAcctInf><AcctName>必蚊凄捷鞑吮徙舶乓忘嘴易</AcctName><Acct>0200000319201967739</Acct><OpenBrId>000000002</OpenBrId></BrAcctInf></NoDrtPtcptInf></SgnPsnInf><SgntrMk><PrxySgntr>PS01</PrxySgntr><PtcptSgntr>MIIGEgYJKoZIhvcNAQcCoIIGAzCCBf8CAQExCzAJBgUrDgMCGgUAMIIB6AYJKoZI\nhvcNAQcBoIIB2QSCAdUxMTAwMDAwMDA0NTcyMTAwMDAwMDAzODI8P3htbCB2ZXJz\naW9uPSIxLjAiIGVuY29kaW5nPSJnYjIzMTIiPz48VHJhZGVEYXRhPjxmaWVsZCBu\nYW1lPSLX3LHKyv0iIHZhbHVlPSIxIiBEaXNwbGF5T25TY3JlZW49IlRSVUUiLz48\nZmllbGQgbmFtZT0i19y98LbuIiB2YWx1ZT0iMiwzMDIuMDDUqiIgRGlzcGxheU9u\nU2NyZWVuPSJUUlVFIi8+PGZpZWxkIG5hbWU9IrXHwrxJRCIgdmFsdWU9IjY1MS5j\nLjAyMDAiIERpc3BsYXlPblNjcmVlbj0iVFJVRSIvPjxmaWVsZCBuYW1lPSKy2df3\nyrG85CIgdmFsdWU9IjIwMjIwMjIyMDk1OTEyNDMxMjYyMTY3NzEiIERpc3BsYXlP\nblNjcmVlbj0iVFJVRSIvPjxmaWVsZCBuYW1lPSKy2df3IiB2YWx1ZT0ivty++CIg\nRGlzcG
 xheU9uU 2NyZWVuPSJUUlVFIi8+PC9UcmFkZURhdGE+MjIwMDAwMDAwMDM5\n19yxysr9o7oxo6zX3L3wtu6jujIsMzAyLjAw1KoouaTJzNL40NApMjMwMDAwMDAw\nMDAwoIIDDjCCAwowggHyoAMCAQICChuSyhAlVgADNQowDQYJKoZIhvcNAQEFBQAw\nOzEfMB0GA1UEAxMWSUNCQyBUZXN0IENvcnBvcmF0ZSBDQTEYMBYGA1UEChMPdGVz\ndGljYmMuY29tLmNuMB4XDTIyMDEwNjA5MDMwOVoXDTI3MDEwNjA5MDMwOVowPjET\nMBEGA1UEAwwKNjUxLmMuMDIwMDENMAsGA1UECwwEMDIwMDEYMBYGA1UECgwPdGVz\ndGljYmMuY29tLmNuMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQD3w8yiYQOw\n64tAPMcICO5BTOYPHMfCPnHhe5kGM01U7GN+HzaC3Iiwcd5Hrbjg021E0fvkvqj4\nySpdlD7mnJALLW/ugtCu+Q8EKyzIs6bf9kcY1+i08cdf5QCbypTVzhwUzq8L/eZ2\nhvNKF/YY+dmlncU3pSHmqKTsW1vJTt2JOQIDAQABo4GQMIGNMB8GA1UdIwQYMBaA\nFER9t5AsN6TZ7WzipIdXZwq18E0UMEsGA1UdHwREMEIwQKA+oDykOjA4MQ4wDAYD\nVQQDDAVjcmw0MzEMMAoGA1UECwwDY3JsMRgwFgYDVQQKDA90ZXN0aWNiYy5jb20u\nY24wHQYDVR0OBBYEFJmqzK3zku4F1k7Btti3zD+P3dkKMA0GCSqGSIb3DQEBBQUA\nA4IBAQBcWLtH6eO+XGv1B744bMgHZFzYfAzAD6jv+kMfrIXoDHtvo/BmRFTYAncq\nSb9oe9gJub5eB1/b82CZN5m+rM7bxoa8t0pz+q9zmyBV4ctGHYUE9lbtcCSepsX5\nR/h71VCEfx6S
 w1rjDPzD M/c7kzPDX31M3gr3E6MfFJvKKaIPFbZWX7XA+qRCGZGF\nBMQMAK2uZ1DzOv6poJTc+TG3Vn+HMkwSA4y1gflisBbvC41stUwXbn9c6AUbbjcR\nqymHrvFZR7L5kuy9mx92MLhRdJJA6gXSPnheYP9b4b/hX67fgBXMg1V6JCli/Seu\nlWPBBLHZGJIudYXu5MD3KujkQzH1MYHuMIHrAgEBMEkwOzEfMB0GA1UEAxMWSUNC\nQyBUZXN0IENvcnBvcmF0ZSBDQTEYMBYGA1UEChMPdGVzdGljYmMuY29tLmNuAgob\nksoQJVYAAzUKMAkGBSsOAwIaBQAwDQYJKoZIhvcNAQEBBQAEgYC8ZGjzR3r73pk6\nTsOLkUJlrWvLjcAfFFr4</PtcptSgntr></SgntrMk><SgnUpInf><Dt>2022-02-22</Dt><SgnUpMk>SU01</SgnUpMk><SgnUpCode>CP06</SgnUpCode><OtherInf>123</OtherInf></SgnUpInf></MainBody><PtcptSgntr>MEQCIARvNpliLdP14KuXXyL30TlLeQQaRVk76+IbSIalnDjOAiAUofGG6FIlCHSShJ9gZo0p+WhPblmdTkxc6o54wsbg7g==</PtcptSgntr></Document>', None),  ]

        
        #print(self.output)
        return self.output

#获取字典原始数据
class get_dict_meaning(information):    
    def __init__(self, dir_case):
        super().__init__(dir_case)
        self.def_data=self.get_data(dir_case)      
        #self.tree=self.build_tree(self.def_data)
        #self.tree2dic(self.tree,self.mean_dict)
        #self.mean_dict_all.append(self.mean_dict)

# 根据地址dir_case获取表中内容，返回一个字典{sheet名：{行名，行内容}}
    def get_data(self,dir_case):
        result={}
        data = xlrd.open_workbook(dir_case)
        dictionary={}
        tmp=[]
        for i in data.sheets():
            # table = data.sheets()[sheetnum]
            nor = i.nrows
            nol = i.ncols
            print(nor,nol)
            
            for k in range(1, nor):
                for j in range(nol):
                    title = i.cell_value(0, j)
                    value = i.cell_value(k, j)
                    
                    dictionary[title] = value
                #print(tmp)
                tmp.append(dictionary)
                dictionary={}
                #print(tmp)
            #print(tmp)
    # yield dict
            pop_index=[]
            for m in range(len(tmp)):
                if tmp[m]['序号']!="":
                    cur=m
                if tmp[m]['序号']=="":
                    tmp[m-1]['备注']=tmp[m-1]['备注']+'\n'+tmp[m]['备注']
                    pop_index.append(m)
            for k in reversed(pop_index):        
                tmp.pop(k)
            result[i.name]=tmp
            tmp=[]
            dictionary={}
            
        #print(result)
        return result



    def ret_last_elem(self,root_dic):
        # print(root_dic)
        if len(root_dic['children'])>0:
            ret_last_elem(root_dic['children'][-1])
        else:
            return root_dic
    def build_children(self,node,cur_node,root):
        if cur_node['要素名称'].count("--")>node['要素名称'].count("--")-1:
    # if ret_last_elem(root[-1])['要素名称'].count("--")>=node['要素名称'].count("--"):
            # print("if条件",cur_node['要素名称'].count("--"),node['要素名称'].count("--"))
            
            self.build_children(node,cur_node['parent'],root)
        elif cur_node['要素名称'].count("--")==node['要素名称'].count("--")-1 :
            node['parent']=cur_node
    # print(node,"\n",cur_node)
            cur_node['children'].append(node)
        elif len(cur_node['children'])>0:
            # print(cur_node)
            self.build_children(node,cur_node['children'][-1],root)

# 建立一个树形构成，输入是字典，输出
    def build_tree(self,data):
        root=list()
        idx=0
    # while idx<len(data):
        #print(data)
        for a,b in data.items():
            for i in b:
                if i['要素名称'].count("--")==0:
                    i['parent']=""
                    i['children']=[]
                    root.append(i)              
                else:
        # print("build_tree",i,ret_last_elem(root[-1]))
                    i['parent']=[]
                    i['children']=[]
                    #print(a,b,i,root)
                    self.build_children(i,root[-1],root)
                for j in root:
                    if j['序号']=="":
                        root.remove(j)
                res[h]=root
        #print(res)
        return res    
        

class xml_parser(information):
    def __init__(self,input):
        super().__init__(input)

    def read_standize(self):
        pass

    def get_result(self):
        tree = ET.parse(self.input)
        root = tree.getroot()
        self.output=root
        return self.output

class NotePad(Tk):
    
    def __init__(self):
        #存储原报文
        self.orgin_id=set()
        #存储查询结果res={'202201011221':['time','id',]}
        self.mesg_mean={'MEM.001.002':'业务办理渠道信息通知报文','MEM.002.002':'机构参与者信息通知报文','MEM.003.002':'机构参与者交易员信息通知报文','MEM.004.002':'机构参与者新原关系通知报文','MEM.005.002':'创建修改机构参与者通知报文','MEM.006.001':'机构参与者信息维护申请报文','MEM.007.001':'企业参与者信息维护申请','MEM.008.001':'业务参与者信息查询申请','MEM.009.001':'业务参与者信息查询应答','MEM.010.001':'业务参与者承接关系变更申请报文','MEM.011.001':'业务参与者支付信用查询申请报文','MEM.012.001':'业务参与者支付信用查询应答报文','PAM.001.001':'主动管理申请报文','PAM.002.001':'主动管理维护申请报文','PAM.003.001':'主动管理权限维护申请报文','PAM.004.001':'主动管理通知报文','NCP.001.002':'承兑信息登记申请报文','NCP.002.002':'承兑保证信息登记申请报文','NCP.003.002':'质押信�
 �登记申请报文','NCP.004.002':'质押解除信息登记申请报文','NCP.005.002':'贴现信息登记申请报文','NCP.006.002':'结清信息登记申请报文','NCP.007.002':'止付信息登记申请报文','NCP.008.002':'止付解除登记申请报文','NCP.009.002':'止付及止付解除登记通知报文','NCP.010.002':'信息登记类撤回申请报文','NCP.011.002':'纸票登记信息查询申请报文','NCP.012.002':'纸票登记信息查询应答报文','NCP.013.002':'库存变更申请报文','NCP.014.002':'库存变更通知报文','NCP.015.002':'保证增信申请报文','NCP.016.002':'付款确认申请报文','NCP.017.002':'付款确认结果通知报文','CPR.011.002':'追偿结清登记申请报文','NES.001.001':'出票信息登记申请报文','NES.002.001':'提示承兑申请报文','NES.003.001':'提示收票申请报文','NES.004.001':'保证申请','NES.005.001':'增信及增信状态维护申请','NES.006.001':'背书转让申请报文','NES.007.001':'�
 ��现申请报文','NES.008.001':'回购式贴现赎回申请','NES.009.001':'质押申请','NES.010.001':'质押解除申请','NES.011.001':'提示付款申请报文','NES.012.001':'追索通知','NES.013.001':'追索同意清偿申请','NES.014.001':'撤票申请','NES.015.001':'不得转让标记撤销申请','CPR.010.002':'线下追偿登记申请报文','CPR.014.002':'电票转入通知报文','CPR.015.002':'非交易过户申请报文','CPR.016.002':'提前和逾期赎回申请报文','CPR.018.002':'供应链票据映射关系查询申请','CPR.019.002':'供应链票据映射关系查询应答','CPR.020.002':'供应链票据信息查询申请报文','CPR.021.002':'供应链票据信息查询应答报文','CES.001.002':'转贴现对话报价发送修改申请报文','CES.002.002':'转贴现对话报价转发报文','CES.003.002':'转贴现成交通知报文','CES.004.002':'质押式回购对话报价发送修改申请报文','CES.005.002':'质押式回购对话报价转发报�
 �','CES.006.002':'质押式回购成交通知报文','CES.007.002':'买断式回购对话报价发送修改申请报文','CES.008.002':'买断式回购对话报价转发报文','CES.009.002':'买断式回购成交通知报文','CES.010.002':'交易业务确认报文','CES.011.002':'对话报价成交/终止应答报文','CES.012.002':'对话报价终止通知报文','CES.013.002':'转贴现意向询价发送修改申请报文','CES.014.002':'转贴现意向询价转发报文','CES.015.002':'质押式回购意向询价发送修改申请报文','CES.016.002':'质押式回购意向询价转发报文','CES.017.002':'买断式回购意向询价发送修改申请报文','CES.018.002':'买断式回购意向询价转发报文','CES.019.002':'意向询价撤销报文','CES.020.002':'再贴现质押式回购发送修改申请报文','CES.021.002':'再贴现质押式回购成交通知报文','CES.022.002':'再贴现买断发送修改申请报文','CES.023.002':'再贴现买断成交通知报�
 �','CES.024.002':'再贴现审批结果通知报文','CES.025.002':'再贴现作废申请报文','CES.026.002':'再贴现授信通知报文','CES.027.002':'再贴现受理关系通知报文','CES.028.002':'转贴现点击成交发送申请报文','CES.029.002':'转贴现点击成交转发报文','CES.030.002':'转贴现点击成交应答报文','CES.031.002':'点击成交报价撤销申请报文','CES.032.002':'点击成交状态更新通知报文','CES.033.002':'质押式回购匿名点击发送申请报文','CES.034.002':'质押式回购匿名点击匹配成功通知报文','CES.035.002':'质押式回购匿名点击票据提交申请报文','CES.036.002':'匿名点击报价撤销申请报文','CES.037.002':'匿名点击状态更新通知报文','CES.038.002':'授信信息维护申请报文','CAS.001.002':'票据业务结算结果通知报文','CAS.002.002':'票据业务资金清算排队通知报文','CAS.003.002':'票据业务结算状态查询申请报文','CAS.004.002':'票据�
 ��务结算状态查询应答报文','CAS.005.002':'票交所资金账户清算排队查询申请报文','CAS.006.002':'票交所资金账户清算排队查询应答报文','CAS.007.002':'票交所资金账户清算排队管理申请报文','CAS.008.002':'票交所资金账户状态变更通知报文','CAS.009.002':'票交所资金账户信息查询申请报文','CAS.010.002':'票交所资金账户信息查询应答报文','CAS.011.002':'票交所资金账户出金申请报文','CAS.012.002':'资金账户余额变动通知报文','CAS.014.001':'批量清算明细通知报文','CAS.015.001':'资金清算行扣款确认申请报文','CIM.001.002':'通用业务确认报文','CIM.002.002':'通用业务撤销报文','CIM.003.002':'通用业务转发报文','CIM.004.002':'通用业务应答报文','CIM.006.002':'影像上传申请报文','CIM.008.002':'影像查询申请报文','CIM.009.002':'影像查询应答报文','CIM.012.002':'附件上传申请报文','CIM.014.002':'附件查询申
 请报文','CIM.015.002':'附件查询应答报文','CIM.017.002':'再贴现补充登记/修改申请报文','CIM.018.001':'通用业务通知','CIM.019.001':'通用票据状态变更通知','CIM.023.001':'票据信息维护申请','CIM.024.001':'票据信息查询申请','CIM.025.001':'票据详细信息下发','CIM.027.001':'票据查验申请','CIM.031.001':'贸易信息登记申请报文','CIM.032.001':'贸易信息查询申请报文','CIM.033.001':'贸易信息查询应答报文','CCM.001.002':'营业日调整通知报文','CCM.002.002':'基础数据变更通知报文','CCM.003.002':'支付系统行名行号变更通知报文','CCM.004.002':'系统状态变更通知报文','CCM.005.002':'登录/退出申请报文','CCM.006.002':'登录/退出应答报文','CCM.007.002':'强制退出登录通知报文','CCM.008.002':'自由格式信息报文','CCM.009.002':'业务查询报文','CCM.010.002':'业务查复报文','CCM.011.002':'报文核对明细申请报文','CCM.012.002':'报文
 核对明细应答报文','CCM.013.002':'数字证书绑定通知报文','CCM.014.002':'故障通知报文','SDN.001.002':'票据存托信息转发报文','SDN.002.002':'票据存托应答申请报文','SDN.003.002':'票据存托退票申请报文','SDN.004.002':'存托退票通知报文','SDN.005.002':'产品创设结果通知报文','SDN.006.002':'票据存托申请报文','CPP.001.002':'贴现申请人信息登记维护申请报文','CPP.002.002':'贴现申请人登记解除申请报文','CPP.003.001':'贴现委托信息登记申请报文','CPP.004.001':'贴现委托解除登记申请报文','CPP.005.001':'贴现委托失效通知报文','CPP.006.002':'贴现申请人信息查询申请报文','CPP.007.002':'贴现申请人信息查询应答报文','CPP.008.001':'贴现委托信息查询申请报文','CPP.009.001':'贴现委托信息查询应答报文','CPP.010.002':'贴现对话报价发送修改申请报文','CPP.011.002':'贴现对话报价转发报文','CPP.012.002':'贴现对
 话报价应答报文','CPP.014.002':'贴现挂牌询价发送申请报文','CPP.015.002':'贴现挂牌询价转发报文','CPP.016.002':'贴现摘牌通知报文','CPP.017.002':'贴现挂牌询价撤销报文','CPP.018.002':'贴现挂牌询价应答报文','CPP.019.002':'贴现业务状态更新通知报文','CPP.020.002':'贴现意向成交通知报文','CPP.021.002':'贴现业务交易确认报文','CPP.022.002':'贴现结算结果通知报文','CPP.023.001':'贴现申请人在线签约需求通知报文','CPP.024.001':'贴现申请人在线签约申请报文','CPP.025.001':'贴现申请人在线签约应答报文','CPP.026.001':'在线签约状态查询申请报文','CPP.027.001':'在线签约状态查询应答报文','CPP.028.001':'在线签约状态通知报文','CPP.029.001':'贴现通专用转发报文','CPP.030.002':'贴现意向询价发送修改申请报文','CPP.031.002':'贴现意向询价转发报文','CPP.032.002':'贴现意向询价应答报文','CPP.033.002':'贴现
 意向询价撤销报文','PAY.001.001':'企业信息签约/解约申请报文','PAY.002.001':'线上票据支付发起申请报文','PAY.003.001':'线上票据支付发起应答报文','PAY.004.001':'线上票据支付流水通知报文','PAY.005.001':'线上票据支付跳转申请报文','PAY.006.001':'线上票据支付跳转应答报文','PAY.007.001':'线上票据锁定/解锁申请报文','PAY.008.001':'线上票据支付结果通知报文','PAY.009.001':'线上票据支付流水查询申请报文','PAY.010.001':'线上票据支付流水更新申请报文','PAY.011.001':'线上票据支付状态查询申请报文','PAY.012.001':'线上票据支付状态查询应答报文','PAY.013.001':'订单附加信息上传申请报文','CHS.001.002':'票据有偿服务费信息通知报文','CHS.002.002':'票据有偿服务费扣收结果通知报文','CHS.003.002':'票据有偿服务费扣费状态查询申请报文','CHS.004.002':'票据有偿服务费扣费状态查询应答报文',}
        self.xml_filed_mean={'CD000001':'99.9999','CD000002':'0','CD000003':'365','CD000004':'365','CD000005':'ACT/360','CD000006':'200','CD000007':'100','CD000008':'5','CD000009':'-5','CD000010':'30','CD000011':'1000','CD000012':'1000000','CD000013':'1000','CD000014':'99.9999','CD000015':'0','CD000016':'0.01','CD000001':'0.333333333333333','CD000002':'0.875','CD000003':'0.354166666666667','CD000004':'0.875','CD000005':'0.375','CD000006':'0.5','CD000007':'0.5625','CD000008':'0.6875','CD000009':'0.375','CD000010':'0.5','CD000011':'0.5625','CD000012':'0.6875','CD000013':'0.375','CD000014':'0.5','CD000015':'0.5625','CD000016':'0.6875','CD000017':'0.375','CD000018':'0.5','CD000019':'0.5625','CD000020':'0.791666666666667','CD000021':'0.375','CD000022':'0.5','CD000023':'0.5625','CD000024':'0.791666666666667','CD000025':'0.375','CD000026':'0.5','CD000027':'0.5625','CD000028':'0.791666666666667','CD000029':'0.333333333333333','CD000030':'0.875','CD000031':'0.375','CD000032':'0.70833333333333
 3','CD000033':'0.333333333333333','CD000034':'0.875','CD000035':'0.333333333333333','CD000036':'0.875','CD000037':'0.694444444444445','CD000039':'0.707638888888889','CD000040':'0.375','CD000041':'0.9375','CD000042':'0.6875','CD000043':'0.6875','CD000044':'0.6875','CD000045':'0.6875','CD000046':'0.6875','CD000047':'0.6875','CD000048':'0.6875','CD000049':'0.6875','CD000050':'0.6875','CD000051':'0.6875','CD000052':'0.375','CD000053':'0.5','CD000054':'0.5','CD000055':'0.697916666666667','CD000056':'0.375','CD000057':'0.5','CD000058':'0.5','CD000059':'0.697916666666667','CD000060':'0.375','CD000061':'0.5','CD000062':'0.5625','CD000063':'0.697916666666667','CD000064':'0.375','CD000065':'0.5','CD000066':'0.5625','CD000067':'0.677083333333333','CD000068':'0.333333333333333','CD000069':'0.875','CD000070':'0.333333333333333','CD000071':'0.833333333333333','CD000072':'0.6875','CD000073':'0.6875','CD000074':'0.6875','CD000075':'0.6875','CD000076':'0.6875','CD000079':'0.6875','CD000080':'0.6875'
 ,'CD000081':'0.718055555555556','CD000082':'0.718055555555556','CD000083':'0.718055555555556','CD000084':'0.826388888888889','CD000085':'0.718055555555556','CD000086':'0.826388888888889','CD000087':'0.718055555555556','CD000088':'0.826388888888889','CD000089':'0.718055555555556','CD000090':'0.826388888888889','CD000091':'0.718055555555556','CD000092':'0.826388888888889','11':'北京','12':'天津','31':'上海','50':'重庆','13':'河北','14':'山西','21':'辽宁','22':'吉林','23':'黑龙江','32':'江苏','33':'浙江','34':'安徽','35':'福建','36':'江西','37':'山东','41':'河南','42':'湖北','43':'湖南','44':'广东','46':'海南','51':'四川','52':'贵州','53':'云南','61':'陕西','62':'甘肃','63':'青海','15':'内蒙古','45':'广西','54':'西藏','64':'宁夏','65':'新疆','81':'香港','82':'澳门','71':'台湾','1':'中央银行','2':'银行业机构','3':'非银行金融机构','4':'非法人产品','5':'虚拟资管参与者','6':'非金融机构','
 7':'存托类非法人产品','8':'存托类虚拟系统参与者','101':'中国人民银行','201':'政策性银行','202':'国有商业银行','203':'股份制商业银行','204':'外资银行','205':'城市商业银行','206':'农商行和农合行','207':'村镇银行','208':'农村信用社','209':'民营银行','301':'财务公司','302':'信托投资公司','303':'保险公司','304':'证券公司','305':'基金公司','306':'金融资产管理公司','307':'私募基金公司','308':'汽车金融公司','309':'保险公司的资产管理公司','310':'证券公司的资产管理公司','311':'基金公司的资产管理公司','401':'商业银行理财产品','402':'证券公司的资产管理产品','403':'信托公司金融产品','404':'保险公司的保险产品','405':'保险资产管理公司的资管产品','406':'基金','407':'私募基金','408':'基金公司的特定客户资产管理业务','409':'社保基金','410':'其他基金','411':'其他非法人产品',
 '412':'证券资管公司的资管产品','413':'基金资管公司的资管产品','501':'商业银行资管','502':'证券公司资管','503':'基金公司资管','504':'基金子公司资管','505':'私募基金公司资管','506':'信托资管','507':'保险公司资管','508':'保险资管公司资管','509':'社保基金资管','510':'其他资管','511':'证券资管公司资管','601':'社保基金理事会','602':'公积金中心','603':'小额贷款公司','604':'融资租赁公司','605':'其他非金融机构','701':'国有商业银行存托产品','702':'股份制商业银行存托产品','703':'外资银行存托产品','704':'城市商业银行存托产品','705':'民营银行存托产品','706':'农商行和农合行存托产品','707':'其他农村金融机构存托产品','708':'证券公司存托产品','709':'其他存托产品','801':'国有商业银行存托','802':'股份制商业银行存托','803':'外资银行存托','804':'城市商业银行存托','805':'
 民营银行存托','806':'农商行和农合行存托','807':'其他农村金融机构存托','808':'证券公司存托','809':'其他存托','CD000001':'101|1','CD000002':'201|2','CD000003':'202|2','CD000004':'203|2','CD000005':'204|2','CD000006':'205|2','CD000007':'206|2','CD000008':'207|2','CD000009':'208|2','CD000068':'209|2','CD000010':'301|3','CD000011':'302|3','CD000012':'303|3','CD000013':'304|3','CD000014':'305|3','CD000015':'306|3','CD000016':'307|3','CD000017':'308|3','CD000018':'309|3','CD000019':'310|3','CD000020':'311|3','CD000021':'401|4','CD000022':'402|4','CD000023':'403|4','CD000024':'404|4','CD000025':'405|4','CD000026':'406|4','CD000027':'407|4','CD000028':'408|4','CD000029':'409|4','CD000030':'410|4','CD000031':'411|4','CD000032':'412|4','CD000033':'413|4','CD000034':'501|5','CD000035':'502|5','CD000036':'503|5','CD000037':'504|5','CD000038':'505|5','CD000039':'506|5','CD000040':'507|5','CD000041':'508|5','CD000042':'509|5','CD000043':'510|5','CD000044':'511|5'
 ,'CD000045':'601|6','CD000046':'602|6','CD000047':'603|6','CD000048':'604|6','CD000049':'605|6','CD000050':'701|7','CD000051':'702|7','CD000052':'703|7','CD000053':'704|7','CD000054':'705|7','CD000055':'706|7','CD000056':'707|7','CD000057':'708|7','CD000058':'709|7','CD000059':'801|8','CD000060':'802|8','CD000061':'803|8','CD000062':'804|8','CD000063':'805|8','CD000064':'806|8','CD000065':'807|8','CD000066':'808|8','CD000067':'809|8','1':'201','2':'202','3':'205','4':'203','5':'204','6':'206','7':'207','8':'208','9':'301','CD000001':'10','CD000002':'10','CD000003':'200','CD000008':'300','CD000009':'300','CD000010':'300','CD000004':'200','CD000005':'200','CD000006':'200','CD000007':'200','CD000011':'100','CD000012':'1000000000','CD000001':'2.25','CD000002':'2.25','CD000003':'2.25','CD000004':'2.25','CD000005':'2.25','CD000006':'2.25','CD000007':'2.25','CD000008':'2.25','CD000009':'2.25','CD000010':'2.25','CD000011':'2.25','CD000012':'2.25','CD000013':'2.25','CD000014':'2.25','CD00001
 5':'2.25','CD000016':'2.25','201':'ST01','202':'ST01','203':'ST01','204':'ST01','205':'ST01','206':'ST01','207':'ST01','208':'ST01','301':'ST01','TM001':'ST01','TM007':'ST01','TM014':'ST01','TM030':'ST01','TM090':'ST01','TM180':'ST01','TM270':'ST01','TM360':'ST01','CD000001':'0','CD000002':'99.9999','CD000003':'0.0001','MT01':'银行','MT02':'非银行','MT03':'资管类','MT04':'存托类','MT05':'供应链平台','MT06':'B2B平台','BC01':'出票信息登记','BC02':'提示承兑申请','BC03':'提示收票申请','BC04':'保证申请','BC05':'保贴增信','BC06':'保兑增信','BC07':'转让背书申请','BC08':'买断式贴现','BC09':'回购式贴现','BC10':'贴现回购赎回申请','BC11':'质押申请','BC12':'质押解除申请','BC13':'提示付款','BC14':'拒付追索','BC15':'非拒付追索','BC16':'追索同意清偿申请','BC17':'冻结（解除）登记','BC18':'不得转让撤销','BC19':'撤票申请','BC20':'票据查验','BC21':'存托','BC22':'保证增信�
 �请','BC23':'ECDS电票迁移','BC24':'转贴现','BC25':'质押式回购首期','BC26':'质押式回购提前赎回','BC27':'质押式回购到期赎回','BC28':'质押式回购逾期赎回','BC29':'买断式回购首期','BC30':'买断式回购赎回','BC31':'再贴现质押式回购首期','BC32':'再贴现质押式回购提前赎回','BC33':'再贴现质押式回购到期赎回','BC34':'再贴现质押式回购逾期赎回','BC35':'非交易过户','BC36':'承兑信息登记','BC37':'贴现信息登记','BC38':'保证信息登记','BC39':'质押信息登记','BC40':'质押解除信息登记','BC41':'止付（解除）登记','BC42':'转托管（票据账户）','BC43':'再贴现买断','NT01':'自动提示付款发起   ','NT02':'自动影像付款确认发起','NT03':'自动库存退票申请  ','NT04':'自动付款确认应答  ','NT05':'自动提示付款应答   ','NT06':'到期清退','NT07':'日终清退','NT08':'票据结束清退','NT09':'提前赎回申请场务审核�
 ��绝结果','NT10':'供应链平台业务通知','NT11':'资金清算行处理结果','NT12':'贴入行办理通知','AR01':'票据作废       ','AR02':'未用退回       ','AR03':'票据权利已逾失效日      ','AR04':'票据追偿清偿结果     ','AR05':'增加保证人     ','AR06':'票据不得转让撤销     ','AR07':'票据或有追偿      ','AR09':'票据冻结/冻结解除登记    ','AR10':'场务状态变更       ','AR11':'回购式贴现已逾赎回截止日','AR12':'场务权属变更','AR13':'票付通票据锁定','AR14':'贴现通票据锁定','AR15':'贴现通权属过户','ET01':'承兑','ET02':'保证','ET03':'质押','ET04':'质押解除','ET05':'转让背书','ET06':'止付/冻结','ET07':'解除止付/冻结','ET08':'保证增信','ET09':'提示付款','ET10':'追索','ET11':'电票转入','ET12':'转托管','ET13':'买断式回购','ET14':'回购式贴现','ET15':'回购式贴现赎回','ET17':'买断式回购赎回','ET18':'权属初始登记','ET1
 9':'质押式回购','ET20':'质押式回购赎回','ET21':'再贴现质押式回购','ET22':'再贴现质押式回购赎回','CD000001':'BC02|ET01','CD000001':'BC36|ET01','CD000001':'BC04|ET02','CD000001':'BC38|ET02','CD000001':'BC11|ET03','CD000001':'BC39|ET03','CD000001':'BC25|ET19','CD000001':'BC31|ET21','CD000001':'BC12|ET04','CD000001':'BC26|ET20','CD000001':'BC27|ET20','CD000001':'BC28|ET20','CD000001':'BC32|ET22','CD000001':'BC33|ET22','CD000001':'BC34|ET22','CD000001':'BC40|ET04','CD000001':'BC07|ET05','CD000001':'BC08|ET05','CD000001':'BC35|ET05','CD000001':'BC37|ET05','CD000001':'BC21|ET05','CD000001':'BC24|ET05','CD000001':'BC43|ET05','CD000001':'BC17|ET06','CD000001':'BC41|ET07','CD000001':'BC03|ET18','CD000001':'BC22|ET08','CD000001':'BC23|ET11','CD000001':'BC29|ET13','CD000001':'BC13|ET09','CD000001':'BC14|ET10','CD000001':'BC15|ET10','CD000001':'BC16|ET10','CD000001':'BC09|ET14','CD000001':'BC10|ET15','CD000001':'BC30|ET17','CD000001':'BC42|ET12','T10002':'出金','T
 10003':'入金','T10006':'收息','T10008':'收费','T80000':'来账手工核对','T90000':'人工调账','RE1011':'转贴现','RE1021':'质押式回购首期','RE1022':'质押式回购到期','RE1023':'质押式回购提前赎回','RE1024':'质押式回购逾期赎回','RE1031':'买断式回购首期','RE1032':'买断式回购到期','RE2011':'托收','RE2021':'追索','RE3011':'再贴现买断','RE3021':'再贴现质押式回购首期','RE3022':'再贴现质押式回购到期','RE3023':'再贴现质押式回购提前赎回','RE3024':'再贴现质押式回购逾期赎回','RE4011':'买断式贴现','RE6011':'标准化票据存托','RE7011':'批量清算','RE4021':'回购式贴现','RE4022':'回购式贴现赎回','RE4032':'逾期托收','RE4061':'央行卖票','CD000001':'ST00','1100':'有限责任公司','1200':'股份有限公司','2100':'有限责任公司分公司','2200':'股份有限公司分公司','3100':'全民所有制','3200':'集体所有制','3300':'股份制','3400':'
 股份合作制','3500':'联营','4100':'事业单位营业','4200':'社团法人营业','4300':'内资企业法人分支机构(非法人)','4400':'经营单位(非法人)','4500':'非公司私营企业','4600':'联营','4700':'股份制企业(非法人)','5100':'有限责任公司（外商投资）','5200':'股份有限公司（外商投资）','5300':'非公司（外商投资）','5400':'外商投资合伙企业','5800':'外商投资企业分支机构','6100':'有限责任公司（台、港、澳资）','6200':'股份有限公司(台港澳与境内合资)','6300':'非公司（台、港、澳资）','6400':'港、澳、台投资合伙企业','6800':'台、港、澳投资企业分支机构','7100':'外国（地区）公司分支机构','7200':'外国(地区)企业常驻代表机构','7300':'外国(地区)企业在中国境内从事经营活动','8100':'内资集团','8500':'外资集团','9100':'农民专业合作经济组织','9200':'农民专业合作社分支机构','9500':'个�
 �工商户','9600':'自然人','9900':'其他','001':'0.416666666666667','002':'0.5','003':'0.583333333333333','001':'','002':'','003':'','001':'','002':'','003':'','001':'RE2011','002':'RE2011','003':'RE2011','001':'ST00','002':'ST00','003':'ST00'}
        self.res={}
        super().__init__()
        self.db_content=[]
        self.set_window()
        self.create_canvas()
        
        
       


    def set_window(self):
        self.title(r"数据精度")
        max_width,max_height=self.maxsize()
        align_center="1200x800+%d+%d"%((max_width-1200)/2,(max_height-900)/2)
        self.geometry(align_center)

    def create_canvas(self):
        canvas=Canvas(self,scrollregion=(-1520,-22200,1520,22200),bg='white') #创建canvas
        canvas.pack(side=LEFT, fill=BOTH, ipadx=2, ipady=2, expand=1) #    放置canvas的位置

        frame_send=Frame(canvas,background='yellow')
        frame_send.pack(side=TOP,fill=NONE,expand=0)

        frame_res=Frame(canvas,background='green') #把frame放在canvas里
        frame_res.pack(side=TOP, fill=NONE, expand=NO) #frame的长宽，和canvas差不多的

        


        vbar=Scrollbar(canvas,orient=VERTICAL) #竖直滚动条
        vbar.pack(side=RIGHT, fill=Y, ipadx=2, ipady=2, expand=0)
        vbar.configure(command=canvas.yview)
        hbar=Scrollbar(canvas,orient=HORIZONTAL)#水平滚动条
        hbar.pack(side=BOTTOM, fill=X, ipadx=2, ipady=2, expand=0)
        hbar.configure(command=canvas.xview)
        canvas.config(xscrollcommand=hbar.set,yscrollcommand=vbar.set) #设置  
        canvas.create_window((120,240), window=frame_res)  #create_window

        self.create_frame_send(frame_send,frame_res)
        
        self.after(1000,print(""))






#参数配置区域函数
    def create_frame_send(self,frame_send,frame_res):
        Label(frame_send,text='bms地址',font=('Arial',10)).pack(side=LEFT, fill=NONE, ipadx=2, ipady=2, expand=0)
        bms_address=Entry(frame_send,width=10)
        bms_address.pack(side=LEFT, fill=NONE, ipadx=2, ipady=2, expand=0)
        Label(frame_send,text='端口',font=('Arial',10)).pack(side=LEFT, fill=NONE, ipadx=2, ipady=2, expand=0)
        bms_port=Entry(frame_send,width=10)
        bms_port.pack(side=LEFT, fill=NONE, ipadx=2, ipady=2, expand=0)
        Label(frame_send,text='名称',font=('Arial',10)).pack(side=LEFT, fill=NONE, ipadx=2, ipady=2, expand=0)
        bms_name=Entry(frame_send,width=10)
        bms_name.pack(side=LEFT, fill=NONE, ipadx=2, ipady=2, expand=0)
        Label(frame_send,text='用户名',font=('Arial',10)).pack(side=LEFT, fill=NONE, ipadx=2, ipady=2, expand=0)
        bms_username=Entry(frame_send,width=10)
        bms_username.pack(side=LEFT, fill=NONE, ipadx=2, ipady=2, expand=0)
        Label(frame_send,text='密码',font=('Arial',10)).pack(side=LEFT, fill=NONE, ipadx=2, ipady=2, expand=0)
        bms_password=Entry(frame_send,width=10)
        bms_password.pack(side=LEFT, fill=NONE, ipadx=2, ipady=2, expand=0)
        Label(frame_send,text='语句',font=('Arial',10)).pack(side=LEFT, fill=NONE, ipadx=2, ipady=2, expand=0)
        bms_sql=Text(frame_send,width=70,height=6)
        bms_sql.pack(side=LEFT, fill=NONE, ipadx=2, ipady=2, expand=0)


       
        bms_address.insert(END,'73.16.177.215')
        bms_port.insert(END,'1521')
        bms_name.insert(END,'bmsgsdb')
        bms_username.insert(END,'query')
        bms_password.insert(END,'query123')
        bms_sql.insert(END,"select t.create_time,t.mesg_id,t.msg_id,t.mesg_type,t.task_param_var,t.task_param from bms.pm_inf_msg_detail t  where work_date='2022-02-25' and  instr(msg_id,'000000000000000202202255001283239')>0 ")


                       
        button_run=Button(frame_send,text='执行',command=lambda :self.run(bms_address.get(),bms_port.get(),bms_name.get(),bms_username.get(),bms_password.get(),bms_sql.get("0.0","end"),frame_res))
        button_run.pack(side=TOP, fill=NONE, ipadx=2, ipady=2, expand=0)
        button_clear=Button(frame_send,text='清空',command=lambda :self.clear_frame(frame_res))
        button_clear.pack(side=BOTTOM, fill=NONE, ipadx=2, ipady=2, expand=0)
        B = Button(frame_send, text ="点我", command = lambda : self.create_frame(frame_res))
        B.pack(side=BOTTOM, fill=NONE, ipadx=2, ipady=2, expand=0)

#不停获取新的关联id
    def get_orgin_id(self,content):
        tmp=re.findall(r'(?<=\<Id\>)\d*',content)
        if tmp!=[]:
            for i in tmp:
                self.orgin_id.add(i)
        else:
            pass
#显示最终的查询结果
    def print_res(self,frame_res,res):
        res_order=sorted(res.items(),key=lambda x:x[0],reverse=True)
        r=[]
        #print(res_order[0])
        for h,i in res_order:
            r.append(self.create_frame(frame_res))
        
            r[-1]['time'].insert(END,i[0])
            r[-1]['origin_id'].insert(END,i[1])
            r[-1]['id'].insert(END,i[2])
            r[-1]['msg_type'].insert(END,i[3])
            r[-1]['msg_type'].insert(END,self.mesg_mean[i[3]])
            
            
            
            if i[4]=="":
                org_xml=re.search(r'\<\?xml[\s\S]*',i[5]).group()
                r[-1]['origin_msg'].insert(END,org_xml)
                self.get_orgin_id(i[5])
            else:
                
                org_xml=re.search(r'\<\?xml[\s\S]*',i[4]).group()
                r[-1]['origin_msg'].insert(END,org_xml)
                self.get_orgin_id(i[4])
                
            tmp_origin_msg=ET.fromstring(r[-1]['origin_msg'].get(1.0,END))
            #print(tmp_origin_msg)
            #print(self.indent(tmp_origin_msg, level=0))
            self.indent(tmp_origin_msg, level=0)
            
            #print(tmp_origin_msg)
            r[-1]['parser_msg'].insert(END,ET.tostring(tmp_origin_msg,encoding='UTF-8',method='xml').decode('UTF-8'))
            print(tmp_origin_msg)
            self.show_line_num(r[-1]['parser_msg'],r[-1]['parser_line_num'])
            
        
# 获得数据填入对应空格中

    def get_orgin_content(self,bms_address,bms_port,bms_name,bms_username,bms_password,frame_res):
        copy_orgin_id=list(self.orgin_id)
        for i in copy_orgin_id[:]:
            sql="select t.create_time,t.mesg_id,t.msg_id,t.mesg_type,t.task_param_var,t.task_param from bms.pm_inf_msg_detail t  where work_date>'2022-01-01' and (instr(task_param_var,'%s')>0 or instr(task_param,'%s')>0) "%("<Id>"+str(i),"<Id>"+str(i))
            print(sql)
            #print(i)
            self.run_sql_bms(bms_address,bms_port,bms_name,bms_username,bms_password,sql)
            
        
        
    def run(self,bms_address,bms_port,bms_name,bms_username,bms_password,sql,frame_res):

        self.run_sql_bms(bms_address,bms_port,bms_name,bms_username,bms_password,sql)
        
        self.get_orgin_content(bms_address,bms_port,bms_name,bms_username,bms_password,frame_res)
        
        self.print_res(frame_res,self.res)

    def run_sql_bms(self,bms_address,bms_port,bms_name,bms_username,bms_password,bms_sql):
        
        
        #res={'202201011221':['time','id',]}
        bms_content=get_xml(bms_address,bms_port,bms_name,bms_username,bms_password,bms_sql)
        self.db_content=bms_content.get_result()
        print(len(self.db_content))
        print()
        for i in self.db_content:
            
            self.res[i[0]]=[]
            self.res[i[0]].append(i[0])
            self.res[i[0]].append(i[1])
            self.res[i[0]].append(i[2])
            self.res[i[0]].append(i[3])
            if i[4]==None:
                #print(i)
                org_xml=re.search(r'\<\?xml[\s\S]*',str(i[5])).group()
                
                self.res[i[0]].append(org_xml)
                self.get_orgin_id(org_xml)
            elif i[4]!=None:
                print(type(i[4]))
                org_xml=re.search(r'\<\?xml[\s\S]*',i[4]).group()
                self.res[i[0]].append(org_xml)
                self.get_orgin_id(org_xml)
            else:
                pass
            
                
        

            
#报文回显区域新增函数
    def create_frame(self,frame):
        frame_child=Frame(frame)
        frame_child.pack(side=TOP, fill=BOTH, ipadx=2, ipady=2, expand=1,anchor=N)
        frame_child2=Frame(frame_child)
        frame_child2.pack(side=LEFT, fill=BOTH, ipadx=2, ipady=2, expand=1,anchor=N)

        frame_child3=Frame(frame_child)
        frame_child3.pack(side=RIGHT, fill=BOTH, ipadx=2, ipady=2, expand=1,anchor=N)




        
        Label(frame_child2,text='时间',font=('Arial',10)).pack(side=TOP, fill=NONE, ipadx=0, ipady=0, expand=0)
        time=Entry(frame_child2)
        time.pack(side=TOP, fill=NONE, ipadx=0, ipady=0, expand=0)

        
        Label(frame_child2,text='原id',font=('Arial',10)).pack(side=TOP, fill=NONE, ipadx=0, ipady=0, expand=0)
        origin_id=Entry(frame_child2)
        origin_id.pack(side=TOP, fill=NONE, ipadx=0, ipady=0, expand=0)
        
        Label(frame_child2,text='id',font=('Arial',10)).pack(side=TOP, fill=NONE, ipadx=0, ipady=0, expand=0)
        id=Entry(frame_child2,width=30)
        id.pack(side=TOP, fill=NONE, ipadx=0, ipady=0, expand=0)
        
        Label(frame_child2,text='报文类型',font=('Arial',10)).pack(side=TOP, fill=NONE, ipadx=0, ipady=0, expand=0)
        msg_type=Entry(frame_child2,width=26)
        msg_type.pack(side=TOP, fill=NONE, ipadx=0, ipady=0, expand=0)

        Label(frame_child3,text='行数',font=('Arial',10)).pack(side=LEFT, fill=NONE, ipadx=0, ipady=0, expand=0)
        origin_line_num=Text(frame_child3,width=3,height=20)
        origin_line_num.pack(side=LEFT, fill=NONE, ipadx=0, ipady=0, expand=0)

        Label(frame_child3,text='原报文',font=('Arial',10)).pack(side=LEFT, fill=NONE, ipadx=0, ipady=0, expand=0)
        origin_msg=Text(frame_child3,width=30,height=20)
        origin_msg.pack(side=LEFT, fill=NONE)
        # origin_msg.insert("end", "Pythofdsafa"+"\n")
        self.show_line_num(origin_msg,origin_line_num)
        



        Label(frame_child3,text='行数',font=('Arial',10)).pack(side=LEFT, fill=NONE, ipadx=2, ipady=2, expand=0)
        parser_line_num=Text(frame_child3,width=3,height=20)
        parser_line_num.pack(side=LEFT, fill=NONE, ipadx=2, ipady=2, expand=0)
        


        Label(frame_child3,text='格式化后报文',font=('Arial',10)).pack(side=LEFT, fill=NONE, ipadx=2, ipady=2, expand=0)
        parser_msg=Text(frame_child3,width=50,height=20)
        parser_msg.pack(side=LEFT, fill=NONE, ipadx=2, ipady=2, expand=0)


        Label(frame_child3,text='释义',font=('Arial',10)).pack(side=LEFT, fill=NONE, ipadx=2, ipady=2, expand=0)
        parser_meaning=Text(frame_child3,width=10,height=20)
        parser_meaning.pack(side=LEFT, fill=NONE, ipadx=2, ipady=2, expand=0)

        
        
#滚动条控制多个控件
        def ScrollCommand(*xx):#在滚动条上点击、拖动等动作
            print(*xx)
            origin_msg.yview(*xx)
            parser_msg.yview(*xx)
            parser_meaning.yview(*xx)
            origin_line_num.yview(*xx)
            parser_line_num.yview(*xx)


        origin_msg_bar=Scrollbar(frame_child3,orient=VERTICAL,command=ScrollCommand)
        origin_msg_bar.pack(side=RIGHT, fill=Y, ipadx=2, ipady=2, expand=0)
        origin_msg.configure(yscrollcommand=origin_msg_bar.set)
        
        self.update()
        print("aa")
        return {'time':time,'origin_id':origin_id,'id':id,'msg_type':msg_type,'origin_line_num':origin_line_num,'origin_msg':origin_msg,'parser_line_num':parser_line_num,'parser_msg':parser_msg,'parser_meaning':parser_meaning}
        # return frame_child

#清空传入的frame中的所有控件
    def clear_frame(self,frame):
        for widget in frame.winfo_children():
            widget.destroy()

    def create_line(self):
        pass

#一个滚动条控制多个控件滚动
    def Wheel(self,event,*text):#鼠标滚轮动作
        print(str(-1*(event.delta/120)))#windows系统需要除以120
        for i in text:
            i.yview_scroll(int(-1*(event.delta/120)),'units')
        # text2.yview_scroll(int(-1*(event.delta/120)), "units")
        # text1.yview_scroll(int(-1*(event.delta/120)), "units")
        return "break" 
#显示行号
    def show_line_num(self,text,line_num_bar):
        content=text.get("1.0",END)
        txt_arr = content.split("\n")
        if len(txt_arr) == 1:
            line_num_bar.insert("1.1", " 1")
        else:
            for i in range(1, len(txt_arr) + 1):
                line_num_bar.insert("end", " " + str(i))
                if i != len(txt_arr):
                    line_num_bar.insert("end", "\n")
#解析xml
    def indent(self,elem,level=0):
        i = "\n" + level*"  "
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "  "
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for elem in elem:
                self.indent(elem, level+1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i
        # return elem




get_dict_meaning("D:\MyProject\copilot\业务主体分册.xls")

app=NotePad()
app.mainloop()

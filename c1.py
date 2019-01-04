# 使用原生爬虫爬取电子书信息， 每一本书的信息都需要爬取，
# 包括书名、作者、内容简介...等。
# 参考地址：http://d81fb43e-d.parkone.cn/
import re
from urllib import request
#这个类的主要作用是返回一个存有所有书的详细信息二级页面的列表
class Spider():
    url = 'http://d81fb43e-d.parkone.cn'
    #所有a链接到书的详细信息的父页面
    root_patternn = '<div class="cover">([\s\S]*?)</div>'
    #所有a链接到书的详细信息的后缀
    root_pattern1 = '<a href="([\s\S]*?)" data-toggle="modal" data-target="#bookDetailsModal"'
    
    
    def fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        htmls = str(htmls,encoding='utf-8')
        return htmls
        
    
    
    def analysis(self, htmls1):
        root = re.findall(Spider.root_patternn,htmls1)
        #把遍历出来符合要求的数据存放的列表
        arr = []
        #要传出的二级页面的列表
        arr1 = []
        i = 0 
        for html in root:
            a = re.findall(Spider.root_pattern1,html)
            arr.append(a)
            #二级页面的url
            url1 = Spider.url+arr[i][0]
            arr1.append(url1)
            i = i + 1
        return arr1   
          
    def go(self):
        htmls = self.fetch_content()
        a = self.analysis(htmls)  
        return a   
       
        
           
            
class Spider1():
    #得到上面类返回的二级页面列表为a
    spider = Spider()
    a = spider.go()
    b = len(a)
    #书的正则
    bname = '<h2>([\s\S]*?)</h2>'
    #作者正则
    root_pattern1 = '<a href="/author/.*"([\s\S]*?)</a>'
    #出版社正则
    root_pattern2 = '<span>出版社:([\s\S]*?)</span>'
    #出版日期正则
    root_pattern3 = '<p>出版日期([\s\S]*?)</p>'
    #简介正则
    root_pattern4 = '<p class="description">([\s\S]*?)</p>'

    
    def fetch_content(self):
        for i in range(Spider1.b):
            r = request.urlopen(Spider1.a[i])
            htmls = r.read()
            htmls = str(htmls,encoding='utf-8')
            root1 = re.findall(Spider1.bname,htmls) #书名
            root2 = re.findall(Spider1.root_pattern1,htmls) #作者
            root3 = re.findall(Spider1.root_pattern2,htmls) #出版社
            root4 = re.findall(Spider1.root_pattern3,htmls) #日期
            root5 = re.findall(Spider1.root_pattern4,htmls) #简介
            print(root1,root2,root3,root4,root5)
            
s = Spider1()            
s.fetch_content()             
            
             
    

    
            


           
            
    
   
        

        

        


        
        
    
    
        
       
        
       
        
    

        
        
        
    
            

    
            
        
        

        

       
        
        
            



        
        
       
        
        



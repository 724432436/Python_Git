from urllib import request
import urllib.parse
import string,re
from bs4 import BeautifulSoup
class Item(object):
    name = None
    link = None
    time = None
    number = None
    source = None
class GetSourceInfo(object):
    def __init__(self, url, number):
        self.url = url
        self.data = number
        self.pageNum = int(number/30 + 1)
        self.urls = self.geturls(self.pageNum, self.data)
        self.items = self.spider(self.urls)
        self.pipeline(self.items)
    def spider(self,urls):
        items = []
        for url in urls:
            htmlcontent = self.getresponse(url)
            soup = BeautifulSoup(htmlcontent, 'lxml')
            tagsli = soup.find_all('div', attrs={'class': 'main-x'})
            #print(tagsli)
            for tag in tagsli:
                item = Item()
                item.name = tag.find('a',attrs={'target': '_blank'}).get_text().strip()
                li = tag.find_all('a',attrs={'target': '_blank'})
                link = re.split('[=]',str(li))[1]
                results = re.findall("(?isu)(http\://[a-zA-Z0-9\.\?/&\=\:]+)", link)  # 获取链接保存起来
                item.link = ''.join(results)
                item.time = tag.find('li', attrs={'class': 'x-left-li li-sj'}).get_text().strip()
                item.number = tag.find('li', attrs={'class': 'x-left-li li-cs'}).get_text().strip()
                item.source = tag.find('p', attrs={'class': 'x-right-p'}).get_text().strip()
                items.append(item)
                print('获取标题%s数据成功' % item.name)
            return items

    def getresponse(self, url):
        try:
            #print(url)
            urls = urllib.parse.quote(url, safe=string.printable)
            response = urllib.request.urlopen(urls)
        except:
            print('Python 返回URL:%s 数据出错' % url)
        else:
            return response.read().decode('utf-8')

    def geturls(self,pagenum,data):
        urls = []
        pns = [str(i) for i in range(pagenum)]
        ul = re.split('[-]',self.url)
        for pn in pns:
            ul[-1] = pn
            url = '-'.join(ul)
            url = url + '.html'
            urls.append(url)
        print('获取url成功,共获取到%d数据\t共%d页数据'%(data, pagenum))
        #print(urls)
        return urls

    def pipeline(self,items):
        filename = u'资源文件.txt'
        with open(filename,'a+',encoding='utf-8') as fp:
            for item in items:
                fp.write('文件名:%s \t 下载链接:%s \t %s \t %s \t %s\n\n'\
                        % (item.name.ljust(40), item.link.ljust(55), item.time.ljust(20),
                                           item.number.ljust(20), item.source.ljust(20)))
        print('写入成功。')

if __name__ == '__main__':
    key = input("请输入你想要搜索的关键字: ")
    url = "http://www.soyunpan.com/search/" + str(key) + "-0-全部-1.html"
    urls = urllib.parse.quote(url, safe=string.printable)
    response = urllib.request.urlopen(urls)
    soup = BeautifulSoup(response,'lxml')
    num = soup.find_all('h2',attrs={'class': "resource-h2"})
    num = re.findall(r'\d+',str(num))[-2]
    GetSourceInfo(url,int(num))
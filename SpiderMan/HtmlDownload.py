import requests
class HtmlDownload(object):
    def download(self,url):
        if url is None:
            return None
        user_agent = 'Mozilla/4.0 (compatible;MSIE 5.5;Windows NT)'
        header = {'User_Agent':user_agent}
        r = requests.get(url,headers=header)
        if r.status_code == 200:
            r.encoding = 'utf-8'
            return r.text()
        return None
import requests

def getHTMLText(url):
    try:
        kv = {'User-Agent':'Mozilla/5.0'}
        imp= {'q':'python'}
        r = requests.get(url,params=imp,headers=kv)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return '产生异常'

if __name__ == '__main__':
    url = 'http://www.so.com/s'
    print(getHTMLText(url))
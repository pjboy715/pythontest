import requests

def getHTMLText(url):
    try:
        kv = {'user-agent':'Mozilla/5.0'}
        r = requests.get(url,headers=kv)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return '产生异常'

if __name__ == '__main__':
    url = 'https://www.amazon.cn/dp/B01MXW6SF6'
    print(getHTMLText(url))
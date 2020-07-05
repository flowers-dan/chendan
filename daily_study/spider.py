import  requests,bs4
res=requests.get("http://www.wangpeili1112.cn")
res.encoding='utf-8'
res.raise_for_status()
b=bs4.BeautifulSoup(res.text,features="lxml")
print(b.select('ul>li>a')[0].getText())
from pyquery import PyQuery as pq
import requests
import re

res = requests.get('https://pic.netbian.com/4kdongman/index.html')
res.encoding = 'gbk'
qq = pq(res.text)
qqq = qq('div.slist')

pattern = '<img[^>]*>'
result1 = re.findall(pattern, str(qqq))

for i in result1:
  print(re.search('src="(.*?)"', i).group(1))
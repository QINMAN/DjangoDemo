#coding:utf-8

import urllib
query={"a":"1","b":"2"}
base_url="http://www.baidu.com/"
print  base_url+"?"+urllib.urlencode(query)





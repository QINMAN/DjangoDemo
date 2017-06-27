#coding:utf-8

a="周"
print  a,type(a),len(a)

b=u"周"
print  b,type(b),len(b)

c=b.encode("utf-8")
print c,type(c)

import re
print re.match(r"^.$","周")
print re.match(r"^.$",u"周")
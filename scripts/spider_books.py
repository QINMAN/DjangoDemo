#coding:utf-8

import urllib2
import pyquery
import sqlConn

url_list = ['http://www.xxsy.net/search?s_wd=&s_type=2&sort=9&pn=' + str(i) for i in range(1,100)]

base_url = 'http://www.xxsy.net/'

href_list = []

for url in url_list:

    html_str = urllib2.urlopen(url).read().decode('utf-8')
    title_list = pyquery.PyQuery(html_str)('.title a')

    for i in title_list:
        title_doc = pyquery.PyQuery(i)
        url = base_url + title_doc.attr('href')
        href_list.append(url)

for i in href_list:
    detail_url = urllib2.urlopen(i).read().decode('utf-8')
    title = pyquery.PyQuery(detail_url)('#detail_title h1').text()
    context = pyquery.PyQuery(detail_url)('#summary1').text()

    conn = sqlConn.SqlConn()
    conn.insert_data('article',{'title':title, 'context':context})

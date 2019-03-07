#-*- coding:utf-8 -*-
# from datetime import datetime,timezone,timedelta
# now = datetime.now()
# print(now)
# print(type(now))
#
# dt=datetime(2015,4,19,12,20)
# print(dt)
#
# print(dt.timestamp())
# #
# t = 1429417200.0
# print(datetime.fromtimestamp(t))
# print(datetime.utcfromtimestamp(t))
#
#
# cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
# print(cday)
# zt_utc_8 = timezone(timedelta(hours=8))
# now = datetime.now
# print(now)
# print(now.replace(tzinfo=zt_utc_8))

#from urllib import request
# with request.urlopen('https://www.163.com/') as f:
#     data=f.read()
#     print('Status:',f.status,f.reason)
#     for k,v in f.getheaders():
#         print('%s:%s'%(k,v))
#     print('Data:', data.decode('utf-8','ignore'))

# from urllib import request,parse
# import json
# import jsonpath
#
# req = request.Request('http://www.douban.com/')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# with request.urlopen(req) as f:
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))



#模拟微博登陆
# from urllib import request,parse
# import json
# import jsonpath
# print('Login to weibo.cn...')
# email = input('Email:')
# passwd = input('Password:')
# login_data = parse.urlencode([
#     ('username',email),
#     ('password',passwd),
#     ('entry', 'mweibo'),
#     ('client_id', ''),
#     ('savestate', '1'),
#     ('ec', ''),
#     ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
# ])
#
# req =request.Request('https://passport.weibo.cn/sso/login')
# req.add_header('Origin', 'https://passport.weibo.cn')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')
#
# with request.urlopen(req,data=login_data.encode('utf-8')) as f:
#     print('Status:', f.status, f.reason)
#     for k,v in f.getheaders():
#         print('%s: %s' % (k, v))
#
#     #取出json文件里的内容，返回的格式是字符串
#     info = f.read().decode('utf-8')
#     #将json格式的字符串转换成python形式的unicode
#     jsonLoads = json.loads(info)
#
#     msgstr = jsonpath.jsonpath(jsonLoads,"$..msg")
#
#     for i in msgstr:
#         print(i)
#
#     array = json.dumps(msgstr,ensure_ascii=False)
#
#     with open('result.json',"w") as t:
#         t.write(array.encode("tf-8"))
#
#
# from PIL import Image
# im = Image.open('C:\\Users\\Administrator\\Desktop\\babycar.jpg')
# w,h = im.size
# print('Original image size: %sx%s' % (w, h))
# im.thumbnail((w//2,h//2))
#
# print('Resize image to: %sx%s' % (w//2, h//2))
# im.save('thumbnail.jpg', 'jpeg')

from urllib import request,parse
params = parse.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
url= "http://www.musi-cal.com/cgi-bin/query?%s" % params
with request.urlopen(url) as f:
    print(f.read().decode('utf-8'))
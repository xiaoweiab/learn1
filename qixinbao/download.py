# encoding=utf8
import requests
import re
import random
import time

class download:
       def __init__(self):
                self.iplist = [] ##初始化一个list用来存放我们获取到的IP
                html1 = requests.get("http://haoip.cc/tiqu.htm")  ##不解释咯
                iplistn = re.findall(r'r/>(.*?)<b', html1.text, re.S)  ##表示从html.text中获取所有r/><b中的内容，re.S的意思是包括匹配包括换行符，findall返回的是个list哦！
                for ip in iplistn:
                    i = re.sub('\n', '', ip)  ##re.sub 是re模块替换的方法，这儿表示将\n替换为空
                    self.iplist.append(i.strip()) ##添加到我们上面初始化的list里面
                    # print(i.strip())
                self.user_agent_list = [
                     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
                     "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
                     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
                     "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
                     "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
                     "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
                     "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
                     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
                     "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
                     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
                     "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
                     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
                     "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
                     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
                     "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
                     "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
                     "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
                     "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
                      ]
       def get(self,url,timeout,proxy=None,num_retries = 6):
           # type: (object, object, object, object) -> object
           UA = random.choice(self.user_agent_list)
           headers = {'User-Agent':UA}
           #如果代理为空时，不使用代理获取response
           if proxy == None :
               try:
                   return requests.get(url,headers = headers,timeout=timeout)
               except:
                   if num_retries > 0 :
                       time.sleep(10)
                       print(u'获取网页出错，10秒后将获取倒数第：',num_retries,u'次')
                       return self.get(url,timeout,num_retries-1)
                   else:
                       print(u'开始使用代理')
                       time.sleep(10)
                       IP = ''.join(str(random.choice(self.iplist)).strip())
                       proxy = {'http':IP}
                       return self.get(url,timeout,proxy)
           #代理不为空
           else:
               try:
                   IP = ''.join(str(random.choice(self.iplist)).strip())
                   proxy = {'http':IP}
                   return requests.get(url,headers=headers,proxies=proxy,timeout=timeout)
               except:
                   if num_retries > 0:
                       time.sleep(10)
                       IP = ''.join(str(random.choice(self.iplist)).strip())
                       proxy = {'http':IP}
                       print(u'正在更换代理，10s后重新获取倒数第',num_retries,u'次')
                       print (u'当前代理是：',proxy)
                       return self.get(url,timeout,proxy,num_retries-1)
                   else:
                       print(u'代理不好用，取消代理')
                       return self.get(url,3)

request = download()

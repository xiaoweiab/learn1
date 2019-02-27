from selenium import webdriver
# from selenium.webdriver import PhantomJS as driver
from multiprocessing import Pool
import os
from bs4 import BeautifulSoup
import time

class Catagory():

  catagory = ""
  catagorylist = ""
  driver = webdriver.PhantomJS()


  def __init__(self,catagory,catagorylist):
      self.catagory = catagory
      self.catagorylist = catagorylist

  def get_resoure(self,url):
      self.driver.get(url)
      self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe"))
      content = self.driver.page_source
      return content

# 解析歌单列表
  def parse_play_list(slef,content):
    num = 0
    start = time.time()
    soup = BeautifulSoup(content,"lxml")
    play_lists = soup.find_all('p',class_="dec")
    print("共有 "+str(len(play_lists))+" 张歌单")
    for play_list in play_lists:
        num = num+1
        play_list_name = play_list.get_text()
        print("---------------------------------------------------------------------")
        print("开始爬取第 "+str(num)+" 个歌单 "+play_list_name )

        play_list_url = "http://music.163.com/#"+play_list.a['href']
        # print(song_list_name+"  "+song_list_url)
        content = slef.get_resoure(play_list_url)
        slef.parse_music_list(content)
    end = time.time()
    use = end - start
    print("解析歌单列表所花时间"+str(use))


# 解析歌曲列表
  def parse_music_list(self,content):
    pool = Pool(3)
    start_time = time.time()
    soup = BeautifulSoup(content,"lxml")
    music_list = soup.find_all('span',class_='txt')
    print("该歌单有 "+str(len(music_list))+" 首歌")
    hrefs = []
    for music in music_list:
      name = music.get_text()
      name = name.split()[0]
      # print(name)
      # 判断歌词是否存在
      if self.isExists(name):
          print(name+":已经存在")
          continue
      else:
          # 多进程获取歌词页面content
          href = "http://music.163.com/#" + music.a['href']
          # content = pool.apply(func=get, args=(href,))
          hrefs.append(href)
    contents =  pool.map(self.get_resoure,hrefs)
    pool.close()
    pool.join()
    end_time = time.time()
    use_time = end_time - start_time
    print("content采集完成,一共花取时间" + str(use_time))
    for content in contents:
        self.parse_lyric(content)
    print("歌单解析完成")
# 解析歌词
  def parse_lyric(self,content):
    # try:
      soup = BeautifulSoup(content,"lxml")
      name = soup.find('div',class_="tit").get_text()
      lyrics = soup.find('div',id='lyric-content').get_text()
      self.save_lyrics(name,lyrics)
    # except Exception:
        # pass


  def isExists(self,name):
    path = 'E:\\yunyinyue\\'+self.catagory +"\\"+ name + '.txt'
    isExists = os.path.exists(path)
    if isExists:
        # print(name+"  ：已经存在")
        return True
    else:
        return False

  def mkdir(self,path):
    path = path.strip()
    isExists = os.path.exists(os.path.join("E:\\yunyinyue\\", path))
    if not isExists:
        print("建了一个名字叫做  " + path + "  的文件夹！")
        os.makedirs(os.path.join("E:\\yunyinyue\\", path))
        return True
    else:
        print("名字叫做  " + path + "  的文件夹已经存在了！")
        return False

  def save_lyrics(self,name,content):
    name = name.split()[0]
    file_path ='E:\\yunyinyue\\'+self.catagory+'\\'+ name + '.txt'
    try:
      f =open(file_path, 'w',encoding='utf-8')
      f.write(content)
      f.close()
      print(name+"保存完成")
    except Exception:
        print("写入错误")


if __name__ =='__main__':
    catagorys = ['孤独','感动','兴奋','快乐','安静','思念','性感']
    catagorys_urls = [
                 'http://music.163.com/#/discover/playlist/?cat=%E5%AD%A4%E7%8B%AC',
                 'http://music.163.com/#/discover/playlist/?cat=%E6%84%9F%E5%8A%A8',
                 'http://music.163.com/#/discover/playlist/?cat=%E5%85%B4%E5%A5%8B',
                 'http://music.163.com/#/discover/playlist/?cat=%E5%BF%AB%E4%B9%90',
                 'http://music.163.com/#/discover/playlist/?cat=%E5%AE%89%E9%9D%99',
                 'http://music.163.com/#/discover/playlist/?cat=%E6%80%9D%E5%BF%B5',
                  "http://music.163.com/#/discover/playlist/?cat=%E6%80%A7%E6%84%9F"
                 ]
    for i in range(0,10):
        cata = Catagory(catagorys[i],catagorys_urls[i])
        print("开始采集 "+catagorys[i]+" 分类")
        cata.mkdir(catagorys[i])
        # print("创建了一个"+catagorys[i]+"文件夹")
        content = cata.get_resoure(catagorys_urls[i])
        cata.parse_play_list(content=content)
        print(catagorys[0]+"采集完成")




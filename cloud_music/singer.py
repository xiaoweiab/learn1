from selenium import webdriver
from multiprocessing import Pool
import os
from bs4 import BeautifulSoup
import time

class Singer():

  singerName = ""
  albumUrl = ""
  driver = webdriver.PhantomJS()


  def __init__(self,singerName):
      self.singerName = singerName
      # self.albumUrl = albumUrl


  def get_resoure(self,albumUrl):
      # self.singerName = singerName
      self.albumUrl = albumUrl
      self.driver.get(albumUrl)
      self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe"))
      content = self.driver.page_source
      return content

  def parse_album(self,url):
      num = 0
      content=self.get_resoure(url)
      soup = BeautifulSoup(content,"lxml")
      album_list = soup.find_all('a',class_="tit s-fc0")
      print("一共有"+str(len(album_list))+"张专辑")
      for album in album_list:
          num = num+1
          album_name = album.get_text()
          album_url = "http://music.163.com/#/"+album['href']
          print("开始爬取第"+str(num)+"张专辑  "+album_name)
          content = self.get_resoure(album_url)
          self.parse_music_list(content)

# 解析歌曲列表
  def parse_music_list(self,content):
    pool = Pool(2)
    start_time = time.time()
    soup = BeautifulSoup(content,"lxml")
    music_list = soup.find_all('span',class_='txt')
    # print(music_list)
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
          content= self.get_resoure(href)
          self.parse_lyric(content)
          # print(name+href)
          # hrefs.append(href)
    # contents =  pool.map(self.get_resoure,hrefs)
    # contents = pool.apply_async(self.get_resoure,hrefs)
    # pool.close()
    # pool.join()
    end_time = time.time()
    use_time = end_time - start_time
    print("content采集完成,一共花取时间" + str(use_time))
    # for content in contents:
    #     self.parse_lyric(content)
    print("歌单解析完成")
# 解析歌词
  def parse_lyric(self,content):
      soup = BeautifulSoup(content,"lxml")
      name = soup.find('div',class_="tit").get_text()
      lyrics = soup.find('div',id='lyric-content').get_text()
      self.save_lyrics(name,lyrics)



  def isExists(self,name):
    path = 'E:\\yunyinyue\\'+self.singerName +"\\"+ name + '.txt'
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
    file_path ='E:\\yunyinyue\\'+self.singerName+'\\'+ name + '.txt'
    try:
      f =open(file_path, 'w',encoding='utf-8')
      f.write(content)
      f.close()
      print(name+"保存完成")
    except Exception:
        print("写入错误")


if __name__ =='__main__':
    singer= ["薛之谦","邓紫棋"]
    urls= ["http://music.163.com/#/artist/album?id=5781&limit=24",
           "http://music.163.com/#/artist/album?id=7763&limit=36"]
    # for i in range(0,2):
    singer = Singer("邓紫棋")
    singer.mkdir("邓紫棋")
    singer.parse_album("http://music.163.com/#/artist/album?id=7763&limit=36")






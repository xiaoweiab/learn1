# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium import webdriver

# firfoxdriver 为 你的firefox安装路径
# firfoxd
# binary = FirefoxBinary(firfoxdriver)
# executable_path = 'F:\program\webdriver'
browser = webdriver.PhantomJS()
page = browser.get("https://baidu.com")
print(page)

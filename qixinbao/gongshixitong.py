from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import PIL.Image as image
# from pymouse import PyMouse

driver = webdriver.Firefox()
driver.get("http://bj.gsxt.gov.cn/sydq/loginSydqAction!sydq.dhtml")
shuru = driver.find_element_by_css_selector('#keyword_qycx')
shuru.send_keys("小米")
driver.find_element_by_css_selector('#popup-submit').click()
time.sleep(2)
driver.find_element_by_css_selector('.gt_cut_fullbg').screenshot("foo1.png")
kk = driver.find_element_by_css_selector('.gt_slider_knob')
kk.click()
time.sleep(3)
driver.find_element_by_css_selector('.gt_cut_fullbg').screenshot("foo2.png")

image1 = image.open('foo1.png')
image2 = image.open('foo2.png')
a =[]
for i in range(0,325):
    for j in range(0,145):
        pix1 = image1.getpixel((i,j))
        pix2 = image2.getpixel((i, j))
        for c in range(0,3):
            if abs(pix1[c]-pix2[c])>=50:
               if i not in a:
                   a.append(i)
# a.sort()
# print(a)


location = kk.location
y = location['y']
x = location['x']

# m = pymouse.PyMouse()
# m.click()
# print(str(x)+"  "+str(y))
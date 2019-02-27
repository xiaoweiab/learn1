from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
class Qinxinbao():

    driver = webdriver.Firefox()
    action = ActionChains(driver)
    # def __init__(self):
    def login(self):
        self.driver.get('http://www.qixin.com/login')
        time.sleep(1)
        self.driver.maximize_window()
        phone = self.driver.find_element_by_css_selector('div.user-box:nth-child(1) > input:nth-child(2)')
        phone.send_keys("15902065168")
        password = self.driver.find_element_by_css_selector('div.user-box:nth-child(3) > input:nth-child(2)')
        password.send_keys("XIAOwei123")
        mov_sider =self.driver.find_element_by_css_selector('.gt_guide_tip')
        mov_sider.click()
        time.sleep(0.5)
        self.driver.find_element_by_class_name('gt_box_holder').screenshot('poo3.png')
        print("成功截图3")
        mov_btn = self.driver.find_element_by_css_selector('.gt_slider_knob')
        self.action.click_and_hold(mov_btn).perform()
        mov_btn.click()
        self.driver.find_element_by_class_name('gt_box_holder').screenshot('poo4.png')
        print("成功截图4")
        # queren = self.driver.find_element_by_css_selector('#btnLogin')
        # queren.click()



if __name__ =='__main__':
    qxb = Qinxinbao()
    qxb.login()

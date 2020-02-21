from selenium import webdriver
import urllib.request
import time
#基于selenium实现在google浏览器中自动刷新页面下单
# def doGet(url):
#     response = urllib.request.urlopen(url)
#     print(response.read())

# doGet('loginUrl')

def doLogin(driver,url,username,password):
    driver.get(url)
    ele1 = driver.find_element_by_id("userCode")
    ele2 = driver.find_element_by_id("passWord")
    ele1.send_keys(username)
    ele2.send_keys(password)
    ele3 = driver.find_element_by_class_name("lognewbtn")
    ele3.click()

driver = webdriver.Chrome(r'C:\Python36\chromedriver.exe')
loginUrl = 'url'
username = "username"
password = "password"
addCart = 'url'
settlement = 'hurl'
order = 'url'

#登录
doLogin(driver,loginUrl,username,password)
#添加购物车
driver.get(addCart)
#进入结算页面
driver.get(settlement)
ele4 = None
try:
 ele4 = driver.find_element_by_id("settlement")
except Exception as e:
    print("settlement")
while ele4 is None:
   try:
     driver.get(settlement)
     time.sleep(1)
     ele4 = driver.find_element_by_id("settlement")
   except Exception as e:
       print("settlement")
ele4.click()
#进入下单页面
ele5 = None
try:
 ele5 = driver.find_element_by_id("submitBtn")
except Exception as e:
    print("submitBtn")
while ele5 is None:
    try:
        driver.get(order)
        time.sleep(1)
        ele5 = driver.find_element_by_id("submitBtn")
    except Exception as e:
        print("submitBtn")
ele5.click()
pass

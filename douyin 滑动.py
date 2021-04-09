from appium  import webdriver
import time

# appium服务的地址
server = r"http://localhost:4723/wd/hub"

# 给5大参数
desider ={
  "platformName": "Android",
  "platformVersion": "7.1.2",
  "deviceName": "127.0.0.1:62001",
  "appPackage": "com.ss.android.ugc.aweme",
  "appActivity": "com.ss.android.ugc.aweme.splash.SplashActivity",
    "unicodeKeyborad":True
}

driver = webdriver.Remote(server,desider)

time.sleep(15)
driver.find_element_by_id("com.ss.android.ugc.aweme:id/bfd").click()

time.sleep(7)

driver.swipe(200,600,200,31,2000)
time.sleep(7)
driver.swipe(660,1250,660,1225,500)
time.sleep(5)
driver.find_element_by_id("com.ss.android.ugc.aweme:id/fnb").click()
driver.find_element_by_id("com.ss.android.ugc.aweme:id/gsk").send_keys("18518739793")
driver.find_element_by_id("com.ss.android.ugc.aweme:id/gpp").send_keys("zlh19981024")
driver.find_element_by_id("com.ss.android.ugc.aweme:id/had").click()
time.sleep(2)
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.LinearLayout").click()
time.sleep(6)
driver.find_element_by_id("com.ss.android.ugc.aweme:id/iq5").click()
time.sleep(7)
for time in range(15):

  driver.swipe(100,600,100,30,2000)


driver.quit()
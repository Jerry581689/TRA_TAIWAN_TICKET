import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# 指定 Chrome 浏览器的路径
chrome_path = "C:\\Users\\User\\Desktop\\chrome-win64\\chrome-win64\\chrome.exe"


# 创建 ChromeOptions 对象，设置浏览器路径
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = chrome_path

# 创建 Chrome WebDriver 对象，并指定 Chrome 浏览器和 Chrome WebDriver 的路径
driver = webdriver.Chrome(options=chrome_options)


# 開啟網站
driver.get("https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip123/query")

# 做你的測試
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "XPath"))).click()

account = driver.find_element(by=By.XPATH, value="//*[@id=\"pid\"]") #身分證
account.clear()
account.send_keys("L125512387")
driver.find_element(by=By.XPATH, value="//*[@id=\"queryForm\"]/div[1]/div[3]/div[2]/label[2]").click()

driver.find_element(by=By.CLASS_NAME,value="startStation").send_keys("0990")
driver.find_element(by=By.CLASS_NAME,value="endStation").send_keys("3230")


date =  driver.find_element(by=By.XPATH, value="//*[@id=\"rideDate1\"]")
date.clear()
date.send_keys("20240403")
       
# 選擇出發時間
time_S = driver.find_element(By.ID, "startTime1")
select  = Select(time_S)
select.select_by_value("18:30")

# 選擇票種
driver.execute_script("document.getElementById('ticketOrderParamList0.trainTypeList1').click()")
driver.execute_script("document.getElementById('ticketOrderParamList0.trainTypeList2').click()")
driver.execute_script("document.getElementById('ticketOrderParamList0.trainTypeList3').click()")
driver.execute_script("document.getElementById('ticketOrderParamList0.trainTypeList4').click()")
driver.execute_script("document.getElementById('ticketOrderParamList0.trainTypeList5').click()")
driver.execute_script("document.getElementById('ticketOrderParamList0.trainTypeList6').click()")

# driver.find_element(by=By.XPATH, value="//*[@id=\"recaptcha-anchor\"]/div[1]").click()

driver.find_element(by=By.CLASS_NAME,value="btn-3d").click()

text  = driver.find_element(by=By.CSS_SELECTOR,value="h2.icon-fa.warning")
print(text)
time.sleep(100)  # 暫停 10 秒，您可以根據需要調整等待的時間

# 關閉瀏覽器
driver.quit()

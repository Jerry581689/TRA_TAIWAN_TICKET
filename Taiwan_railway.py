import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains




# 指定 Chrome 浏览器的路径
chrome_path = "C:\\Users\\User\\OneDrive\\桌面\\chrome-win64\\chrome.exe"

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

driver.find_element(by=By.XPATH, value="//*[@id=\"queryForm\"]/div[1]/div[3]/div[2]/label[2]").click() # 依時段




driver.find_element(by=By.CLASS_NAME,value="icon-list").click()
driver.find_element(by=By.XPATH,value="//*[@id=\"cityHot\"]/ul/li[4]/button").click()
driver.find_element(by=By.CLASS_NAME,value="endStation").send_keys("豐原")



input_element = driver.find_element(By.ID, "rideDate1")
input_element.clear()
input_element.send_keys("20240403")


select_element = driver.find_element(by=By.ID,value="startTime1")
select = Select(select_element)
select.select_by_value("18:30")
select_element = driver.find_element(by=By.ID,value="endTime1")
select = Select(select_element)
select.select_by_value("23:59")


driver.find_element(by=By.CSS_SELECTOR,value='label[for="ticketOrderParamList0.trainTypeList1"]').click()
driver.find_element(by=By.CSS_SELECTOR,value='label[for="ticketOrderParamList0.trainTypeList2"]').click()
driver.find_element(by=By.CSS_SELECTOR,value='label[for="ticketOrderParamList0.trainTypeList3"]').click()
driver.find_element(by=By.CSS_SELECTOR,value='label[for="ticketOrderParamList0.trainTypeList4"]').click()
driver.find_element(by=By.CSS_SELECTOR,value='label[for="ticketOrderParamList0.trainTypeList5"]').click()
driver.find_element(by=By.CSS_SELECTOR,value='label[for="ticketOrderParamList0.trainTypeList6"]').click()


driver.find_element(by=By.CLASS_NAME,value="btn-3d").click()




h2_element = driver.find_element(by=By.CSS_SELECTOR,value='h2.icon-fa.warning')
text = h2_element.text
print(text)

#while True:
for i in range(5):
    if text == "系統依您所設定的訂票內容查詢，目前查無可售座位，請您調整訂票內容後再重新查詢！":    
        reset_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='reset']")))
        driver.execute_script("arguments[0].click();", reset_button)
        time.sleep(1)
        
        # 再次點擊按鈕
        driver.find_element(by=By.CLASS_NAME, value="btn-3d").click()
        
        # 等待新的 h2 元素出現
        WebDriverWait(driver, 10).until(EC.staleness_of(h2_element))
        h2_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'h2.icon-fa.warning')))
        text = h2_element.text
    else:
        break
        
    
    


time.sleep(100)  # 暫停 10 秒，您可以根據需要調整等待的時間

# 關閉瀏覽器
driver.quit()

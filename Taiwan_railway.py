import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains





chrome_path = "C:\\Users\\User\\OneDrive\\桌面\\chrome-win64\\chrome.exe"   # 指定 Chrome 浏览器的路径
chrome_options = webdriver.ChromeOptions()  # 创建 ChromeOptions 对象，设置浏览器路径
chrome_options.binary_location = chrome_path
driver = webdriver.Chrome(options=chrome_options)# 创建 Chrome WebDriver 对象，并指定 Chrome 浏览器和 Chrome WebDriver 的路径
# driver.maximize_window() # 將視窗最大化
screen_width = driver.execute_script("return window.screen.width;")
screen_height = driver.execute_script("return window.screen.height;")
# 將視窗調整為左半邊
driver.set_window_position(0, 0)
driver.set_window_size(screen_width // 2, screen_height)

driver.get("https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip123/query")


# 填入參數
ID           = "A139325062"
STARTSTATION = "松山"
ENDSTATION   = "豐原"
DATE         = "20240404"
TIME1        = "18:30"
TIME2        = "23:59"

account = driver.find_element(by=By.XPATH, value="//*[@id=\"pid\"]") #身分證
account.clear()
account.send_keys(ID)

driver.find_element(by=By.XPATH, value="//*[@id=\"queryForm\"]/div[1]/div[3]/div[2]/label[2]").click() # 依時段

# driver.find_element(by=By.CLASS_NAME,value="icon-list").click()  舊
# driver.find_element(by=By.XPATH,value="//*[@id=\"cityHot\"]/ul/li[4]/button").click()

driver.find_element(by=By.CLASS_NAME,value="startStation").send_keys(STARTSTATION)
driver.find_element(by=By.CLASS_NAME,value="endStation").send_keys(ENDSTATION)

input_element = driver.find_element(By.ID, "rideDate1")
input_element.clear()
input_element.send_keys(DATE)


select_element = driver.find_element(by=By.ID,value="startTime1")
select = Select(select_element)
select.select_by_value(TIME1)
select_element = driver.find_element(by=By.ID,value="endTime1")
select = Select(select_element)
select.select_by_value(TIME2)


driver.find_element(by=By.CSS_SELECTOR,value='label[for="ticketOrderParamList0.trainTypeList1"]').click()
driver.find_element(by=By.CSS_SELECTOR,value='label[for="ticketOrderParamList0.trainTypeList2"]').click()
driver.find_element(by=By.CSS_SELECTOR,value='label[for="ticketOrderParamList0.trainTypeList3"]').click()
driver.find_element(by=By.CSS_SELECTOR,value='label[for="ticketOrderParamList0.trainTypeList4"]').click()
driver.find_element(by=By.CSS_SELECTOR,value='label[for="ticketOrderParamList0.trainTypeList5"]').click()
driver.find_element(by=By.CSS_SELECTOR,value='label[for="ticketOrderParamList0.trainTypeList6"]').click()


driver.find_element(by=By.CLASS_NAME,value="btn-3d").click()



try:
    h2_element = driver.find_element(by=By.CSS_SELECTOR,value='h2.icon-fa.warning')
    text = h2_element.text
    print(text)
except Exception:
      text = ""
      print("找不到元素，有車票喔喔喔")

#while True:
for i in range(1):
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

        link_element = driver.find_element(By.XPATH, '//a[contains(text(), "自強(3000)")]')
        print(link_element)
        tr_element = link_element.find_element(By.XPATH, './ancestor::tr[@class="trip-column"]')
        label_element = tr_element.find_element(By.CSS_SELECTOR, 'label[for]')
        label_element.click()    

        input("請手動處理 reCAPTCHA，按下回車繼續...")

        driver.find_element(By.XPATH, value="//*[@id=\"queryForm\"]/div[2]/button[2]").click()
        
    
    


time.sleep(1000)  # 暫停 10 秒，您可以根據需要調整等待的時間

# 關閉瀏覽器
driver.quit()

import datetime
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException



HOUR = 22
MIN = 55
SEC = 0
URL = "https://kktix.com/events/a8249618-01afw/registrations/new" ##網址   https://kktix.com/events/della-2024-hk/registrations/new
EMAIL = "Jerry581689@gmail.com"
PASSWORD = "J25354634"
TARGET_PRICE = "3880"
TICKET_NUMBER = 2  ##張數
SEAT_CHOOSE = "COMPUTER"  ## SELF , COMPUTER ,NONE  ## 自己選位,電腦選位,下一步


# 計算時間差
def calculate_time_difference():
    now = datetime.datetime.now()
    target_time = now.replace(hour=HOUR, minute=MIN, second=SEC, microsecond=0)
    if now > target_time:
        target_time += datetime.timedelta(days=1)
    time_difference =  (target_time - now).total_seconds()
    if time_difference > 0:
        print("倒數", time_difference, "秒")
        time.sleep(time_difference)

## chrome環境設定
def chromedriver_setting():
    chrome_path = "C:\\Users\\User\\Desktop\\chrome-win64\\chrome-win64\\chrome.exe" #HOME
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = chrome_path
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window() # 將視窗最大化
    driver.get(URL)
    return driver

##登入
def login(driver):
    wait = WebDriverWait(driver, 100)
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/users/sign_in')]")))
    login_button.click()
    # Email
    Email_input = driver.find_element(By.ID, "user_login")
    Email_input.send_keys(EMAIL)
    Password_input = driver.find_element(By.ID, "user_password")
    Password_input.send_keys(PASSWORD)
    login_button = driver.find_element(By.NAME, "commit")
    login_button.click()

##選擇票數票價
def ticket(driver):  
    while True:
        try:      
            wait = WebDriverWait(driver, 15)  # 最長等待15秒
            wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'ticket-unit')]")))            
            tickets = driver.find_elements(By.XPATH, "//div[contains(@class, 'ticket-unit')]")

            if not tickets:
                print("没找到票，刷新页面并重试...")
                driver.refresh()
                time.sleep(5)  # 等待页面刷新完成
                continue

            for ticket in tickets:
                try:
                    # 嘗試找到票價元素
                    price_element = ticket.find_element(By.XPATH, ".//span[contains(@class, 'ticket-price')]//span[contains(@class, 'ng-binding')]")
                    price_text = price_element.text.strip()

                    if TARGET_PRICE in price_text.replace('$', '').replace(',', '').replace('.', ''): 
                        print("有找到票!!!!!") 
                        plus_button = ticket.find_elements(By.XPATH, ".//button[contains(@class, 'plus')]")        
                        sold_out_element = ticket.find_elements(By.XPATH, "//span[contains(@class, 'ticket-quantity')]")

                        if not plus_button:
                            print("有相對應票，但是已售完!!><")
                            driver.refresh()
                            time.sleep(100)
                            continue
                        else:
                            for _ in range(TICKET_NUMBER):
                                plus_button.click()
                            # 服務條款 check
                            checkbox = driver.find_element(By.ID, "person_agree_terms")
                            checkbox.click()
                            return  # 停止循環，任務完成
                    else:
                        print("沒找到相對應的票價><><")

                except StaleElementReferenceException:
                    print("元素變得無效，重試查找該元素...")
                    driver.refresh()
                    time.sleep(100)
                    continue

        except NoSuchElementException:           
            print("发生异常，刷新页面并重试...")
            driver.refresh()
            time.sleep(5)





## 是下一步 OR 配位
def seat(driver,SEAT_CHOOSE):
    if(SEAT_CHOOSE == "COMPUTER"):
        ## 電腦配位
        print("電腦配位")
        wait = WebDriverWait(driver, 10)  # 最長等待 10 秒
        button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn-primary') and contains(@class, 'btn-lg')]")))
        button.click()    
    elif(SEAT_CHOOSE == "NONE"):
        print("下一步")
        next_step_button = driver.find_element(By.XPATH, "//button[contains(@class, 'btn-primary') and contains(@class, 'btn-lg') and contains(@ng-click, 'challenge')]")
        next_step_button.click()
    else:
        print("待補123")



# 主程序
driver = chromedriver_setting()
login(driver)
calculate_time_difference()
driver.refresh()
ticket(driver)
seat(driver, SEAT_CHOOSE)


# 關閉瀏覽器
input("請按Enter結束刷票...")
driver.quit()

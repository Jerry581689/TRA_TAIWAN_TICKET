import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# 指定您安裝的較舊版本的 Chrome 的路徑
chrome_path = "C:\\Users\\User\\OneDrive\\桌面\\chrome-win64\\chrome.exe"

# 構建 Chrome 選項
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = chrome_path

# 建立 Chrome 瀏覽器物件
driver = webdriver.Chrome(options=chrome_options)

# 開啟網站
driver.get("https://kktix.com/users/sign_in?back_to=https%3A%2F%2Fkktix.com%2F")

# 做你的測試
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "XPath"))).click()
account = driver.find_element(by=By.XPATH, value="//*[@id=\"user_login\"]")
account.clear()
account.send_keys("Jerry581689@gmail.com")

password = driver.find_element(by=By.XPATH, value="//*[@id=\"user_password\"]")
password.clear()
password.send_keys("J25354634")
driver.find_element(by=By.XPATH, value="//*[@id=\"new_user\"]/input[3]").click()
driver.find_element(by=By.XPATH, value="//*[@id=\"events-tab-0\"]/ul/li[8]/a/div/span[2]").click()
driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div[2]/div[2]/ul/li[1]/div/a").click()
# nextStepBtn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "XPath")))
# nextStepBtn.click()
time.sleep(50)  # 暫停 10 秒，您可以根據需要調整等待的時間

# 關閉瀏覽器
driver.quit()

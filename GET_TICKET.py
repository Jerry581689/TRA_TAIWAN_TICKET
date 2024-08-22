from requests_html import HTMLSession
import os

# 設定 Chromium 瀏覽器的執行檔路徑
os.environ['PYPPETEER_CHROMIUM_EXECUTABLE'] = r'C:\Users\00048628\Desktop\chrome-win64\chrome.exe'

def fetch_dynamic_value():
    session = HTMLSession()
    url = 'https://kktix.com/events/della-2024-hk/registrations/new'
    response = session.get(url)

    # 執行 JavaScript 來渲染頁面
    response.html.render(timeout=20)

    # 查找 class='ticket-list ng-scope' 的元素
    ticket_list = response.html.find('.ticket-list.ng-scope', first=True)

    if ticket_list:
        # 查找所有 class='display-table-row' 的元素
        rows = ticket_list.find('.display-table-row')
        
        for row in rows:
            ticket_name = row.find('.ticket-name', first=True).text
            ticket_price = row.find('.ticket-price', first=True).text
            ticket_quantity = row.find('.ticket-quantity', first=True).text

            # 打印每個元素的內容
            print("票種:", ticket_name)
            print("票價:", ticket_price)
            print("票數:", ticket_quantity)
            print("-" * 40)
    else:
        print("沒有找到符合條件的元素")

fetch_dynamic_value()

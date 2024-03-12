import requests

# 設定請求的URL
url = 'https://tip.railway.gov.tw/tra-tip-web/tip/tip001/tip123/queryTrain'

# 設定要傳送的資料
data = {
    '_csrf': '32579c8d-c61d-4cde-8760-91725036060e',
    'custIdTypeEnum': 'PERSON_ID',
    'pid': 'A139325062',
    'tripType': 'ONEWAY',
    'orderType': 'BY_TIME',
    'ticketOrderParamList[0].tripNo': 'TRIP1',
    'ticketOrderParamList[0].startStation': '0990-松山',
    'ticketOrderParamList[0].endStation': '3230-豐原',
    'ticketOrderParamList[0].rideDate': '2024/04/04',
    'ticketOrderParamList[0].startOrEndTime': 'true',
    'ticketOrderParamList[0].startTime': '16:30',
    'ticketOrderParamList[0].endTime': '23:59',
    'ticketOrderParamList[0].normalQty': '1',
    'ticketOrderParamList[0].wheelChairQty': '0',
    'ticketOrderParamList[0].parentChildQty': '0',
    'ticketOrderParamList[0].trainTypeList': '11',
    '_ticketOrderParamList[0].trainTypeList': 'on',
    'ticketOrderParamList[0].trainTypeList': '1',
    '_ticketOrderParamList[0].trainTypeList': 'on',
    'ticketOrderParamList[0].trainTypeList': '2',
    '_ticketOrderParamList[0].trainTypeList': 'on',
    'ticketOrderParamList[0].trainTypeList': '3',
    '_ticketOrderParamList[0].trainTypeList': 'on',
    '_ticketOrderParamList[0].trainTypeList': 'on',
    '_ticketOrderParamList[0].trainTypeList': 'on',
    'ticketOrderParamList[0].chgSeat': 'true',
    '_ticketOrderParamList[0].chgSeat': 'on',
    'ticketOrderParamList[0].seatPref': 'NONE',
    'completeToken': 'zMox8klUG9s65AE1LYOA8Q=='
}

# 發送POST請求
response = requests.post(url, data=data)

# 輸出伺服器的回應
print(response.text)

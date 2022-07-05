import requests
import urllib3
import utils
import regCode
import time
# import xml.dom.minidom //xml pretty
urllib3.disable_warnings()

global Output

print("")
print("법정동코드 조회 시작")
print("ex)~동, ~동1가")
Dong_Name = input("조회할 동: ")

Dong_Code = regCode.get_regCode(Dong_Name)
if Dong_Code == "":
    print('동이름이 잘못되었습니다.')
    exit()
print(Dong_Code)


_LAWD_CD = input("법정동코드를 입력하세요 (앞5자리만 입력) : ")
if len(_LAWD_CD) != 5:
    print("법정동코드가 5자리가 아닙니다")
    exit()

_DEAL_YMD = input("조회년월(YYYYMM): ")
if len(_DEAL_YMD) != 6:
    print("조회년월이 6자리가 아닙니다")
    exit()
    
_serviceKey = input("본인 인증키(없다면 내부인증키로 진행됨): ")

if _serviceKey == "":
    _serviceKey = 'xCw4bm05sPJY3RgsvQ7EcFrchgg0Nejb4gEfWVYogx6zS8PjqzUODdjEF1o+yyiuF3oawjb2upn/4c/agXUFig==',

try:    
    url = 'http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTrade'
    params ={'serviceKey' : _serviceKey ,'LAWD_CD' : _LAWD_CD, 'DEAL_YMD' : _DEAL_YMD }

    result = requests.get(url, params=params, verify=False)
    Output = result.text
    # Xml_Output= xml.dom.minidom.parseString(Output)
    # Last_Output = Xml_Output.toprettyxml()
    # print(Last_Output)
            
except Exception as e:
    print("Exception: {}".format(e))
    
resultCode = utils.StrGrab(Output, '<resultCode>', '</resultCode>', 1)
if resultCode != "00":
    print("조회실패 resultCode: {}".format(resultCode))
    exit()

aindex = 1
Result_List = list()

print('조회중...')
start = time.process_time()

while True:    
    Result_dict = dict(
        price = utils.StrGrab(Output, '<거래금액>', '</거래금액>', aindex).strip(),
        name = utils.StrGrab(Output, '<아파트>', '</아파트>', aindex).strip(),
        floor = utils.StrGrab(Output, '<층>', '</층>', aindex).strip()
    )    
    Result_List.append(Result_dict)
    if Result_dict.get('price') == "" or Result_dict.get('name') == "" or Result_dict.get('floor') == "":
        break
    aindex+=1

end = time.process_time()

print(Result_List)

print('조회완료...')
print('소요시간: {}'.format(end-start))
    
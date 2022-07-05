import requests
import urllib3
import utils

urllib3.disable_warnings()

global Output

def get_regCode(ainput):
    if ainput == "":
        return "input is Null"
    try:
        url = "https://www.code.go.kr/stdcode/regCodeL.do"
        header={'Content-Type': 'application/x-www-form-urlencoded; Content-Length:268','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/103.0.0.0'}

        data = {
            "cPage":"1",
            "regionCd_pk":"",
            "chkWantCnt":"0",
            "reqSggCd":"*",
            "reqUmdCd":"*",
            "reqRiCd":"*",
            "searchOk":"0",
            "codeseId":"00002",
            "pageSize":"10",
            "regionCd":"",
            "locataddNm": ainput,
            "sidoCd":"*",
            "sggCd":"*",
            "umdCd":"*",
            "riCd":"*",
            "disuseAt":"0",
            "stdate":"",
            "enddate":""
        }

    
        result = requests.post(url, headers=header, data=data, verify=False)
        Output = result.text
    except Exception as e:
        print("Exception: {}".format(e))
        return e

    i = 1

    Result_List = list()

    while True:
        if utils.StrGrab(Output, '<td class="table_left">', '</td>', i) == "":
            break
        else:
            Result_dict = dict(
                법정동코드 = utils.StrGrab(Output, '<td class="table_left">', '</td>', i),
                주소지 = utils.StrGrab(Output, '<td class="table_center01">', '</td>', i)
            )
            Result_List.append(Result_dict)
        
        i+=1
    
    return Result_List

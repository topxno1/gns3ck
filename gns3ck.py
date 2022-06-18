import requests
import string
import time

def http_error_log(code):
    f=open('log.txt','a')
    f.write(time.ctime()+" HTTP Error "+str(code)+"\n")
    f.close()        

def except_log(e):
    f=open('log.txt','a')
    f.write(time.ctime()+" "+str(e)+"\n")
    f.close()

def http_check(url):
    try:
        r = requests.get(url, timeout=5)
        if r.status_code==200:
            return "有回應"
        else:
            http_error_log(r.status_code)
            return "無回應"
    except Exception as e:
        http_error_log(e)
        return "無連通"





print(http_check(url))


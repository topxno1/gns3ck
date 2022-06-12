import requests
import string
import time

url = "http://120.125.82.173"
#url = "http://120.125.82.155"
#url = "https://docs.python.org/zh-tw/3/library/tisdfsdf"

try:
    r = requests.get(url, timeout=5)
    if r.status_code==200:
        print("有連通")
    else:
        print("無回應")
        f=open('log.txt','a')
        f.write(time.ctime()+" HTTP Error "+str(r.status_code)+"\n")
        f.close()
except Exception as e:
    print("無連通")
    f=open('log.txt','a')
    f.write(time.ctime()+" "+str(e)+"\n")
    f.close()
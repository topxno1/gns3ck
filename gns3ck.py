import requests

try:
    r = requests.get("http://120.125.82.173", timeout=5)
    if r.status_code==200:
        print("有連通")
    else:
        print("無回應")
except:
    print("無回應")
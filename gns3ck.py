import requests
url = ""

try:
    r = requests.get(url, timeout=5)
    if r.status_code==200:
        print("有連通")
    else:
        print("無回應")
except:
    print("無回應")
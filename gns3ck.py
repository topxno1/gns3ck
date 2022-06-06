import requests

try:
    r = requests.get("http://120.125.82.173", timeout=5)
    if r.status_code==200:
        print("Response OK!")
    else:
        print("Response Error!")
except:
    print("No Response")
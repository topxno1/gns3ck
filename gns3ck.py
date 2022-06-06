import requests

r = requests.get("http://120.125.82.173", timeout=5)

print(r.status_code)
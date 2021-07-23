import requests
from requests.auth import HTTPBasicAuth

user = 'thor8.dahal@gmail.com'
password = "password"
#ip = sys.argv[1]
url = "https://cgifederal.secure.force.com/ApplicantHome"
res=requests.get(url , auth=HTTPBasicAuth(user, password))
print(res.text)

import math
import os
import mymodule
import requests

print(math.sqrt(16))

print(mymodule.add(3,7))
mymodule.hello()

r = requests.get("http://www.google.com")
print(r.text)

response = requests.get("https://api.github.com")
print(response.status_code)
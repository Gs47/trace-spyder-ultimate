import urllib.request, json
print(json.loads(urllib.request.urlopen("https://ipapi.co/json/").read()))
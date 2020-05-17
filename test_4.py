#!/usr/bin/python3.7

# 4. Количество открытых и закрытых issues ​ на заданном периоде времени по дате
# создания issue 

import requests

import ApiBase

url = f"https://api.github.com/search/issues?q=type:issue+repo:{ApiBase.userName}/{ApiBase.repoName}+" +\
      f"state:open+state:closed+created:{ApiBase.dateStart}..{ApiBase.dateStop}"

payload = {}
headers = {
  'Accept': 'application/vnd.github.v3+json',
  'Authorization': f'token {ApiBase.token}'
}

response = requests.request("GET", url, headers=headers, data = payload)

print( "total issuses count (opened + closed):", response.json()[ "total_count" ] )

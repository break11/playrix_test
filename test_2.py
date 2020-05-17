#!/usr/bin/python3.7

# 2. Количество открытых и закрытых pull requests ​ на заданном периоде времени по
# дате создания PR и заданной ветке, являющейся базовой для этого PR .

import requests

import ApiBase

url = f"https://api.github.com/search/issues?q=type:pr+repo:{ApiBase.userName}/{ApiBase.repoName}+" +\
      f"state:open+state:closed+created:{ApiBase.dateStart}..{ApiBase.dateStop}+base:\"{ApiBase.branchName}\"&sort=created&order=asc"

payload = {}
headers = {
  'Accept': 'application/vnd.github.v3+json',
  'Authorization': f'token {ApiBase.token}'
}

response = requests.request("GET", url, headers=headers, data = payload)

print( "total pull request count (opened + closed):", response.json()[ "total_count" ] )


#!/usr/bin/python3.7

# 5. Количество “старых” issues ​ на заданном периоде времени по дате создания issue.
# Issue считается старым, если он не закрывается в течение 14 дней.

import requests
import datetime

import ApiBase

url = f"https://api.github.com/search/issues?q=type:pr+repo:{ApiBase.userName}/{ApiBase.repoName}+" +\
      f"is:open+created:{ApiBase.dateStart}..{ApiBase.dateStop}+base:\"{ApiBase.branchName}\""

url = f"https://api.github.com/search/issues?q=type:issue+repo:{ApiBase.userName}/{ApiBase.repoName}+" +\
      f"is:open+created:{ApiBase.dateStart}..{ApiBase.dateStop}"

payload = {}
headers = {
  'Accept': 'application/vnd.github.v3+json',
  'Authorization': F'token {ApiBase.token}'
}

response = requests.request("GET", url, headers=headers, data = payload)
pageCount = response.json()["total_count"] // 30

for page in range( 1, pageCount+1 ):
    pagedUrl = url + f"&page={page}"

    response = requests.request("GET", pagedUrl, headers=headers, data = payload)
    # У айтемов есть поле created_at(прим. "created_at": "2019-12-26T05:35:56Z"), нужно удалить issues младше 14 дней
    for i in response.json()["items"]:
        sDate = i["created_at"].split( "T" )[0]
        date = datetime.date.fromisoformat( sDate )
        if (datetime.datetime.now().date() - date).days > 14:
            print( i )

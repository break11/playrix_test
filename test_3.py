#!/usr/bin/python3.7

# Количество “старых” pull requests ​ на заданном периоде времени по дате создания
# PR и заданной ветке, являющейся базовой для этого PR. Pull request считается
# старым, если он не закрывается в течение 30 дней и до сих пор открыт.

import requests
import datetime

import ApiBase

url = f"https://api.github.com/search/issues?q=type:pr+repo:{ApiBase.userName}/{ApiBase.repoName}+" +\
      f"is:open+created:{ApiBase.dateStart}..{ApiBase.dateStop}+base:\"{ApiBase.branchName}\""

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
    # У айтемов есть поле created_at(прим. "created_at": "2018-11-16T23:37:31Z"), нужно удалить реквесты младше 30 дней
    for i in response.json()["items"]:
        sDate = i["created_at"].split( "T" )[0]
        date = datetime.date.fromisoformat( sDate )
        if (datetime.datetime.now().date() - date).days > 30:
            print( i )

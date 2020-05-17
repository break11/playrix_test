#!/usr/bin/python3.7

# 1. Самые активные участники. Таблица из 2 столбцов: login автора, количество его
# коммитов. Таблица отсортирована по количеству коммитов по убыванию. Не
# более 30 строк. ​ Анализ производится на заданном периоде времени и заданной
# ветке.

import requests
import json

import ApiBase

url = f"https://api.github.com/repos/{ApiBase.userName}/{ApiBase.repoName}/commits?since={ApiBase.dateStart}&until={ApiBase.dateStop}&sha={ApiBase.branchName}"

payload = {}
headers = {
  'Accept': 'application/vnd.github.v3+json',
  'Authorization': f'token {ApiBase.token} '
}

response = requests.request("GET", url, headers=headers, data = payload)

# print(response.text.encode('utf8'))
print( response.text )

l = json.loads( response.text )
print( "111111111111111111111111111111111111111111111111111111111" )

for i in l:
  print( i )

# print( d )

# ```

# {{USER_NAME}} - имя владельца проекта

# {{REPO_NAME}} - имя проекта

# {{API-TOKEN}}

# {{DATE_AFTER}} YYYY-MM-DD - начало временного диапазона

# {{DATE_BEFORE}} YYYY-MM-DD - конец временного диапазона

# {{BRANCH_NAME}} - имя ветки


# Как обработать:
# У айметов есть поле author - это JSON, в нём есть поле login
# Нужно посчитать количество коммитов для каждого login и отсортировать по убыванию

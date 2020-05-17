#!/usr/bin/python3.7

# 1. Самые активные участники. Таблица из 2 столбцов: login автора, количество его
# коммитов. Таблица отсортирована по количеству коммитов по убыванию. Не
# более 30 строк. ​ Анализ производится на заданном периоде времени и заданной
# ветке.

import requests

import ApiBase

url = f"https://api.github.com/repos/{ApiBase.userName}/{ApiBase.repoName}/" +\
      f"commits?since={ApiBase.dateStart}&until={ApiBase.dateStop}&sha={ApiBase.branchName}"

payload = {}
headers = {
  'Accept': 'application/vnd.github.v3+json',
  'Authorization': f'token {ApiBase.token} '
}

response = requests.request("GET", url, headers=headers, data = payload)

resultDict = {}
# У айметов есть поле author - это JSON, в нём есть поле login
# Нужно посчитать количество коммитов для каждого login и отсортировать по убыванию

for item in response.json():
  commitAuthorName = item["author"]["login"]
  if resultDict.get( commitAuthorName ):
    resultDict[ commitAuthorName ] += 1
  else:
    resultDict[ commitAuthorName ] = 1

for i in sorted( resultDict.items(), reverse=True ):
  print( i )

##########################################################################################
#### response sample for debug - one commit item
##########################################################################################

{'sha': '6a3d7bf24713d08a2380bb3570ac38a678a7ce4f', 
'node_id': 'MDY6Q29tbWl0MjY0MjU5ODc4OjZhM2Q3YmYyNDcxM2QwOGEyMzgwYmIzNTcwYWMzOGE2NzhhN2NlNGY=', 
'commit': {'author': {'name': 'break1-Home', 'email': 'break1@yandex.ru', 'date': '2020-05-17T02:06:36Z'},
           'committer': {'name': 'break1-Home', 'email': 'break1@yandex.ru', 'date': '2020-05-17T02:06:36Z'},
           'message': 'test 1 start work', 'tree': {'sha': '46476a8800fdeeb18015447f23b34ea7b4bb8c0f', 
                                                    'url': 'https://api.github.com/repos/break11/playrix_test/git/trees/46476a8800fdeeb18015447f23b34ea7b4bb8c0f'
                                                   },
           'url': 'https://api.github.com/repos/break11/playrix_test/git/commits/6a3d7bf24713d08a2380bb3570ac38a678a7ce4f',
           'comment_count': 0,
           'verification': {'verified': False, 'reason': 'unsigned', 'signature': None, 'payload': None}
           },
'url': 'https://api.github.com/repos/break11/playrix_test/commits/6a3d7bf24713d08a2380bb3570ac38a678a7ce4f',
'html_url': 'https://github.com/break11/playrix_test/commit/6a3d7bf24713d08a2380bb3570ac38a678a7ce4f',
'comments_url': 'https://api.github.com/repos/break11/playrix_test/commits/6a3d7bf24713d08a2380bb3570ac38a678a7ce4f/comments',
'author': {'login': 'break11', 
          'id': 32346580,
          'node_id': 'MDQ6VXNlcjMyMzQ2NTgw',
          'avatar_url': 'https://avatars3.githubusercontent.com/u/32346580?v=4', 
          'gravatar_id': '', 
          'url': 'https://api.github.com/users/break11', 
          'html_url': 'https://github.com/break11', 
          'followers_url': 'https://api.github.com/users/break11/followers', 
          'following_url': 'https://api.github.com/users/break11/following{/other_user}', 
          'gists_url': 'https://api.github.com/users/break11/gists{/gist_id}', 
          'starred_url': 'https://api.github.com/users/break11/starred{/owner}{/repo}', 
          'subscriptions_url': 'https://api.github.com/users/break11/subscriptions', 
          'organizations_url': 'https://api.github.com/users/break11/orgs', 
          'repos_url': 'https://api.github.com/users/break11/repos', 
          'events_url': 'https://api.github.com/users/break11/events{/privacy}', 
          'received_events_url': 'https://api.github.com/users/break11/received_events', 
          'type': 'User', 
          'site_admin': False}, 
          'committer': {'login': 'break11', 
                        'id': 32346580,
                        'node_id': 'MDQ6VXNlcjMyMzQ2NTgw', 
                        'avatar_url': 'https://avatars3.githubusercontent.com/u/32346580?v=4', 
                        'gravatar_id': '', 
                        'url': 'https://api.github.com/users/break11', 
                        'html_url': 'https://github.com/break11', 
                        'followers_url': 'https://api.github.com/users/break11/followers', 
                        'following_url': 'https://api.github.com/users/break11/following{/other_user}', 
                        'gists_url': 'https://api.github.com/users/break11/gists{/gist_id}', 
                        'starred_url': 'https://api.github.com/users/break11/starred{/owner}{/repo}', 
                        'subscriptions_url': 'https://api.github.com/users/break11/subscriptions', 
                        'organizations_url': 'https://api.github.com/users/break11/orgs', 
                        'repos_url': 'https://api.github.com/users/break11/repos', 
                        'events_url': 'https://api.github.com/users/break11/events{/privacy}', 
                        'received_events_url': 'https://api.github.com/users/break11/received_events', 
                        'type': 'User', 
                        'site_admin': False
                        },
          'parents': [{'sha': '0992c5d5edc4a9c0e8c2702dd9def4dbd85f76cd', 
                        'url': 'https://api.github.com/repos/break11/playrix_test/commits/0992c5d5edc4a9c0e8c2702dd9def4dbd85f76cd', 
                        'html_url': 'https://github.com/break11/playrix_test/commit/0992c5d5edc4a9c0e8c2702dd9def4dbd85f76cd'
                        }]
}

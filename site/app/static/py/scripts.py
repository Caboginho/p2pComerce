# -*- coding: utf8 -*-
import requests
import re

req = requests.get('http://checkip.dyndns.org')

ip_final = re.findall('[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}', req.text)

html = """<!DOCTYPE html>
<html lang="pt-br">
    <head>
    <meta charset="UTF-8">
    </head>
    <body>
        <h1>Your ip is : {{IP}}</h1>
    </body>
</html>
"""
html = html.replace('{{IP}}', ip_final[0])
print(html)
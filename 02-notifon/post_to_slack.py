# coding: utf-8
import rewuests
import requests
url = 'https://hooks.slack.com/services/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'
data = {"text":"Hello, World!"}
requests.post(url,json=data)

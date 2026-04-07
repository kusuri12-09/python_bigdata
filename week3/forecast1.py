import requests
import json

url = ''
queryparams ='?'+ \
        'ServiceKey=' + ''+ \
        '&pageNo=' + '1'+ \
        '&numOfRows=' + '1'+ \
        '&dataType=' + 'JSON'+ \
        '&base_date=' + '20260330'+ \
        '&base_time=' + '1400'+\
        '&nx='+ '55'+ \
        '&ny='+ '120'

result = requests.get(url+ queryparams)
print(result.text)
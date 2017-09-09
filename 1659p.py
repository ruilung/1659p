# python 3
import json
from urllib.request import urlopen

url_1659a = 'http://www.taiwanbus.tw/app_api/SP_PredictionTime.ashx?routeNo=1659&branch=0&goBack=1&Lang=&Source=w'
url_1659b = 'http://www.taiwanbus.tw/app_api/SP_PredictionTime.ashx?routeNo=1659&branch=A&goBack=1&Lang=&Source=w'
url_1659c = 'http://www.taiwanbus.tw/app_api/SP_PredictionTime.ashx?routeNo=1659&branch=B&goBack=1&Lang=&Source=w'
url_9089 = 'http://www.taiwanbus.tw/app_api/SP_PredictionTime.ashx?routeNo=9089&branch=0&goBack=1&Lang=&Source=w'

url_1659a_back = 'http://www.taiwanbus.tw/app_api/SP_PredictionTime.ashx?routeNo=1659&branch=0&goBack=2&Lang=&Source=w'
url_1659b_back = 'http://www.taiwanbus.tw/app_api/SP_PredictionTime.ashx?routeNo=1659&branch=A&goBack=2&Lang=&Source=w'
url_9089_back = 'http://www.taiwanbus.tw/app_api/SP_PredictionTime.ashx?routeNo=9089&branch=0&goBack=2&Lang=&Source=w'


def find_stop(alist, astop):
    j = 0
    for i in alist:
        if i['name'] == astop:
            return j
        else:
            j += 1


def show_stop(aurl, astop, abefore):
    response = urlopen(aurl)
    html = response.read()
    jsondata = json.loads(html)
    mystop_id = find_stop(jsondata, astop)
    mystop_before = abefore
    mystop_index = 0
    for i in jsondata:

        if mystop_id - mystop_before < mystop_index <= mystop_id:
            text = '{mystop:2d} {myname:<7s} {ptime:<5s} {carno:<6s} {isfull:<2s} '.format(mystop=mystop_index,
                                                                                           myname=i["name"],
                                                                                           ptime=i["predictionTime"],
                                                                                           carno=i["carNo"],
                                                                                           isfull=i["isFull"])
            print(text)
        mystop_index += 1


bustop = '大草厝'

print('===1659a===')
show_stop(url_1659a, bustop, 5)
print('===1659b===')
show_stop(url_1659b, bustop, 5)
print('===1659c===')
show_stop(url_1659c, bustop, 5)
print('===9089===')
show_stop(url_9089, bustop, 5)

print('===1659a_back===')
show_stop(url_1659a_back, bustop, 1)
print('===1659b_back===')
show_stop(url_1659b_back, bustop, 1)
print('===9089_back===')
show_stop(url_9089_back, bustop, 1)

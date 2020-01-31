class model:
        def _init_(self,name,county,city,date):
            self.name=name
            self.county = county
            self.city = city
            self.date=date


import time ,json,requests

def getProvince():
            url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=&_=%d'%int(time.time()*1000)
            data=json.loads(requests.get(url=url).json()['data'])
            #print(data)
            for item in data['areaTree']:
                if item in data['areaTree']:
                    if (item['name'] == '中国'):
                        for item1 in item['children']:
                            if item1 in item['children']:
                                pro = item1
                                return pro






if __name__=='__main__':
    url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=&_=%d'%int(time.time()*1000)
    csdnurl = 'https://view.inews.qq.com/g2/getOnsInfo?name=wuwei_ww_area_counts&callback=&_=%d'%int(time.time()*1000)
    data=json.loads(requests.get(url=url).json()['data'])

    #print(data['areaTree'])

    for item in data['areaTree']:
        if item in data['areaTree']:
            if(item['name']=='中国'):
                    for item1 in item['children']:
                        if item1 in item['children']:
                            pro=item1
                            print(pro)






import requests
import pandas as pd
import time
import random

url = 'https://tiki.vn/api/v2/products/{}'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'vi-VN,vi;q=0.8,en-US;q=0.5,en;q=0.3',
    'Referer': 'https://tiki.vn/?src=header_tiki',
    'x-guest-token': '8jWSuIDBb2NGVzr6hsUZXpkP1FRin7lY',
    'Connection': 'keep-alive',
    'TE': 'Trailers',
}

cokie={
    'TOKENS':'{%22access_token%22:%22SUi2PlBOsuYmXopxGvefFrQc8NhAIMLa%22}',
    '_trackity':'ca067ce7-1a00-4b88-7961-b5cb0d720e1c',
    'delivery_zone':'Vk4wMzQwMjQwMTM=',
    'tiki_client_id':''
}

params = {
     'platform': 'web',
     'spid': '276158236',
     'version': 3 
}

df_id = pd.read_csv('E:/PTIT/python/rawl_tiki/product_id_device_mobile.csv')


pid_list=df_id.id.to_list()

cnt=0
list_product=[]
price=[]
sold=[]

for pid in pid_list:
    url = 'https://tiki.vn/api/v2/products/{}'.format(pid)

    reponse=requests.get(url,headers=headers,params=params,cookies=cokie)

    if reponse.status_code==200:
        try:
            data=reponse.json()         
            list_product.append({'name':data['name']})
            price.append({'price':data['price']})    
        except:
            print('no price')
    else:
        print("value error")
        
sold=[]
rating_evaluate=[]
count_evaluate=[]


for pid in pid_list:
    url = 'https://tiki.vn/api/v2/products/{}'.format(pid)

    reponse=requests.get(url,headers=headers,params=params,cookies=cokie)

    if reponse.status_code==200:
        try:
            data=reponse.json() 
            try:          
                sold.append({'sold':data['quantity_sold'].get('value')})       
            except:
                sold.append({'sold':0})
            try:
                count_evaluate.append({'count_evaluate':data['rating_average']})
            except:
                count_evaluate.append({'count_evaluate':0})
            try:
                rating_evaluate.append({'rating_evaluate':data['rating_average']})
            except:
                rating_evaluate.append({'rating_evaluate':0})
        except:
            pass       

    else:
        print("value error")

df_sold=pd.DataFrame(sold)
df_rating=pd.DataFrame(rating_evaluate)
df_count_rating=pd.DataFrame(count_evaluate)

df_name=pd.DataFrame(list_product)
df_price=pd.DataFrame(price)

df_id['name']=df_name['name']
df_id['price']=df_price['price']
df_id['sold']=df_sold['sold']
df_id['rating_evaluate']=df_rating['rating_evaluate']
df_id['count_evaluate']=df_count_rating['count_evaluate']



df2=df_id[df_id['name'].notna()]


df2.to_csv('sold.csv',index=True)


#df2.to_csv('device_mobile.csv',index=False)


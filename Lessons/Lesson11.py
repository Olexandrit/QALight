# pyramida
import requests
url = 'https://bittrex.com/Api/v2.0/pub/market/GetTicks?marketName=USDT-BTC&tickInterval=day'
r = requests.get(url)
data = r.json()
# print data

nlist = []

for i in data["result"]:
    # print(i)
    
    # h = i["H"]
    # l = i["L"]
    
    ssum = (i["H"]+i["L"])/2
    
    # print("H:{}/L:{}=S:{}".format(h,l,ssum))
    
    nlist.append(ssum) 

# print("nlist= ",nlist)

# print([(i["H"]+i["L"])/2 for i in data["result"]])
btc = 100
usd = 0

for i in range(6,len(nlist)):
    
    y2 = (nlist[i]+nlist[i-1]+nlist[i-2]+nlist[i-3]+nlist[i-4])/5
    y1 = (nlist[i-1]+nlist[i-2]+nlist[i-3]+nlist[i-4]+nlist[i-5])/5
    
    x2 = (nlist[i]*5+nlist[i-1]*4+nlist[i-2]*3+nlist[i-3]*2+nlist[i-4])/15
    x1 = (nlist[i-1]*5+nlist[i-2]*4+nlist[i-3]*3+nlist[i-4]*2+nlist[i-5])/15
    
    
    if (x1>=y1)and(y2>=x2): 
        print("sale",data["result"][i]["T"])
        usd = btc * nlist[i]        
        
    
    if (y1>=x1)and(x2>=y2): 
        print("buy",data["result"][i]["T"])
        btc = usd/nlist[i]
    
print("usd=",usd-100*420)
    

    
    
    


    


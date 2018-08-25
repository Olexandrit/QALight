# -*- coding: utf-8 -*-
from app import *

@app.route('/tasks')
def get_tasks():
    return render_template("tasks.html", tasks = Tasks.query.all())
    
@app.route('/day')
def get_day():
    return render_template("day.html", view_day = Tasks_day.query.all())
    
@app.route('/day2')
def get_day2s():
    r = requests.get("https://api.privatbank.ua/p24api/infrastructure?json&atm&city=kyiv")
    r_text =r.json()
    
    devices = r_text['devices']
    
    for i in devices:
        
        fullAddressEn,x,y = i["fullAddressEn"],i["latitude"],i["longitude"]
        
        print(fullAddressEn,x,y)
        
        data = Private(fullAddressEn=fullAddressEn,latitude=x,longitude=y)
        
    #     db.session.add(data)
    
    # db.session.commit()
    return ":)))))))"
    
@app.route('/private')
def get_map():
    return render_template("map.html", data_private = Private.query.all())        
        
    
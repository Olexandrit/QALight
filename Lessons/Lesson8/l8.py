from bottle import route, run, template, request

import redis

r_server = redis.Redis(host="127.0.0.1",port=6379)

l=[""]
l2 = [""]

# @route('/hello/<name>')
# def index(name):
#     return template('temp/index.html', name=name)
    
def create_tr_td():
    
    tr_td1_td2 = ""
    for key in r_server.scan_iter("set*"):
    
        n_key = str(key).replace("b","")
        n_key = n_key.replace("'","")
        
        tr_td1_td2 = tr_td1_td2 + find_val(n_key)
    
    return tr_td1_td2

def find_val(key):
    
    val = r_server.smembers(key)
    
    tr_td1_td2 = '<tr><td>{}</td><td>{}</td></tr>'.format(key,val)
    
    return tr_td1_td2
    
@route('/hello/')
def index2():
    
    key = str(request.query.get('key') or "")
    tr_td1_td2=find_val(key)
    
    if key == "":
        tr_td1_td2 = create_tr_td()
        
    return template('temp/index2.html', tr_td1_td2=tr_td1_td2)

        
    # num2 = int(request.query.get('num2') or 0)
    
    # print(num1,num2)
    
    # res = num1**num2
    
    # str_res = '{}<sup>{}</sup>={}'.format(num1, num2, res)

    # if l[-1] != str_res:
        
    #     l.append(str_res)
        
    #     r_server.lpush("foo",str_res)
        
    # l2 = r_server.lrange("foo",0,6)
    
    # return template('temp/index2.html', tr_td1_td2=create_tr_td()) #num1=num1, num2=num2, res=res,l=l[-6:][::-1],l2=l2)

print(create_tr_td())
run(host='0.0.0.0', port=8080)


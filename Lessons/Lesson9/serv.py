from bottle import route, run, template, request

l = []

@route('/pow')
def pow():
    num1 = int(request.query.get('num1') or 0)
    num2 = int(request.query.get('num2') or 0)
    rez = num1**num2
    l.append('{}<sup>{}</sup>={}'.format(num1, num2, rez))
    return template('pow_other_device.html', num1=num1, num2=num2, l=l[-6:][::-1])

run(host='0.0.0.0', port=8080)
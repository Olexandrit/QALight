
from math import sqrt
a = 1
b = -8
c = 12

def quadratic_equation(a,b,c):

    print('{0}x**2 {1}x {2} = 0'.format(a, b, c))

    d = b**2-4*a*c

    print('D= {0}'.format(d))

    sqrt_d = sqrt(d)
    print('sqrt(d)= {0}'.format(sqrt_d))

    if sqrt_d<0:
        print("no sqrt")
    elif sqrt_d==0:
        x = -b/2*a
        print('x= {0}'.format(x))
    elif sqrt_d > 0:
        x1 = (-b+sqrt_d)/2*a
        x2 = (-b-sqrt_d)/2*a
        print('x1= {0}; x2= {1}'.format(x1,x2))

quadratic_equation(float(a),float(b),float(c))

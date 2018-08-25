from pyramid.view import view_config
from models import *


@view_config(renderer="templates/index.pt")
def index_view(request):
    return {}
    
@view_config(renderer="templates/pc.pt", name="pc")
def pc_view(request):
    return {"pcs": PC.select()}
    
@view_config(renderer="templates/product.pt", name="product")
def product_view(request):
    return {"prd": Product.select()}
    
@view_config(renderer="templates/productapple.pt", name="productappple")
def productapple_view(request):
    list_apple = ProductApple.select()
    c = 1
    for i in list_apple:
        print("i=",i)
        i.t = "atr" + str(c)
        c += 1
    
    return {"apl": list_apple}
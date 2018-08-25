from peewee import *

db = SqliteDatabase('my.db')

class PC(Model):
    code = IntegerField(primary_key=True)
    model = CharField()
    speed = SmallIntegerField()
    ram = SmallIntegerField()
    hd = FloatField()
    cd = CharField()
    price = DecimalField()

    class Meta:
        database = db
        db_table = 'PC'
        
class Product(Model):
    model = CharField(primary_key=True)
    maker = CharField()
    type  = CharField()
   
    class Meta:
        database = db
        db_table = 'Product'

class ProductApple(Model):
    model = CharField(primary_key=True)
    maker = CharField()
    type  = CharField()
   
    def method_view(self):
        return '{}:{}-{}'.format(self.maker,self.model,self.type)
   
    def __str__(self):
        return '{}:{}-{}'.format(self.maker,self.model,self.type) 
        
    class Meta:
        database = db
        db_table = 'ProductApple'
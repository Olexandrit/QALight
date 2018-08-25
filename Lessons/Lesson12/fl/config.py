import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

#SQLALCHEMY_DATABASE_URI = 'mysql://tolearn:@' + os.getenv('IP', '0.0.0.0') + ':3306/c9'
#SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

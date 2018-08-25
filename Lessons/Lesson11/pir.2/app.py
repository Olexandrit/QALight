import os
from wsgiref.simple_server import make_server
from pyramid.config import Configurator

def main():
    # Grab the config, add a view, and make a WSGI app
    config = Configurator()
    config.include('pyramid_chameleon')
    config.scan("views")
    app = config.make_wsgi_app()
    return app


if __name__ == '__main__':
    # When run from command line, launch a WSGI server and app
    app = main()
    server = make_server(os.getenv('IP', '0.0.0.0'), int(os.getenv('PORT', 8080)), app)
    server.serve_forever()

# sudo pip install pyramid
# sudo pip install zope.interface
# sudo pip install --upgrade zope.interface
# sudo pip install pyramid_chameleon
# sudo pip install peewee
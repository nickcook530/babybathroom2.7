from bottle import default_app, route, hook
from peewee import *

db = MySQLDatabase(
    'nickcook530$babydb',  # Required by Peewee.
    user='nickcook530',  # Will be passed directly to psycopg2.
    password='dbenter530',  # Ditto.
    host='nickcook530.mysql.pythonanywhere-services.com',  # Ditto.
    #threadlocals=True,
    )

class BaseModel(Model):
    """A base model that will use our MySQL database"""
    class Meta:
        database = db

class BoyBathroom(BaseModel):
    name = CharField()
    description = CharField()
    lon = FloatField()
    lat = FloatField()



@hook('before_request')
def _connect_db():
    db.get_conn()
    print('Db is closed via before hook: {}'.format(db.is_closed()))

@hook('after_request')
def _close_db():
    db.close()
    print('Db is closed via after hook: {}'.format(db.is_closed()))

@route('/bloc')
def boy_location():
    bloc_dict = {}
    for entry in BoyBathroom.select():
        bloc_dict[entry.id] = {'name':entry.name, 'description':entry.description,'lon':entry.lon, 'lat':entry.lat}
    print(bloc_dict)
    return bloc_dict


application = default_app()

'''
def database_connection_context(function):

    def wrapper(*args, **kwargs):
        db.get_conn()
        result = function(*args, **kwargs)
        db.close()
        return result
    print('Db is closed via wrapper: {}'.format(db.is_closed()))
    return wrapper
'''

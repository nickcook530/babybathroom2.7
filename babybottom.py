from peewee import *
#(MySQLDatabase, Model, CharField, FloatField)

db = MySQLDatabase(
    'nickcook530$babydb',  # Required by Peewee.
    user='nickcook530',  # Will be passed directly to psycopg2.
    password='dbenter530',  # Ditto.
    host='nickcook530.mysql.pythonanywhere-services.com',  # Ditto.
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

'''
update = BoyBathroom.select().where(BoyBathroom.name == 'First BB').get()
update.name = 'Nick House'
update.description = 'I pee here'
update.lon = -72.729673
update.lat = 41.761924
update.save()


db.connect()
test = BoyBathroom.select().where(BoyBathroom.name == 'First BB').get()
print(test.lon)

newloc1 = BoyBathroom.create(name='First BB', description='I really hope this works',
                                lon = 55.284923, lat = 58.322329)
db.create_table(BoyBathroom)
'''

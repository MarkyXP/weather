# https://github.com/coleifer/peewee
import peewee as _db

db = _db.SqliteDatabase("database.db")


class _DB_BaseModel(_db.Model):
    class Meta:
        database = db


class Location_Metadata(_DB_BaseModel):
    id = _db.AutoField()  # Primary Key Auto Increment
    name_lower = _db.CharField(unique=True)
    name = _db.CharField(unique=True)
    wiki_data = _db.TextField()
    landmarks = _db.TextField()
    lat = _db.FloatField()
    long = _db.FloatField()


class Forecast(_DB_BaseModel):
    location = _db.ForeignKeyField(Location_Metadata, backref="forecasts")
    start_time = _db.DateTimeField()
    temp_c = _db.TextField()
    condition = _db.TextField()
    wind_kph = _db.FloatField()
    gust_kph = _db.FloatField()
    precipitation = _db.FloatField()


def setup():
    global db
    db.connect()
    db.create_tables([Location_Metadata, Forecast])


if __name__ == "__main__":
    setup()

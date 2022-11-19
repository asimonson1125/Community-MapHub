from init import db


class Vendors(db.Model):
    __tablename__ = 'vendors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    longitude = db.Column(db.String, nullable=False)
    latitude = db.Column(db.String, nullable=False)

    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return '<name {}>'.format(self.name)

    def to_json(self):
        return {"id": self.id,
                "name": self.name,
                "latitude": self.latitude,
                "longitude": self.longitude}

    def get_id(self):
        return self.id

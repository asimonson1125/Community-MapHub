from init import db


class Vendors(db.Model):
    __tablename__ = 'vendors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    longitude = db.Column(db.REAL, nullable=False)
    latitude = db.Column(db.REAL, nullable=False)
    min = db.Column(db.REAL)
    max = db.Column(db.REAL)
    percentile = db.Column(db.REAL)
    deployer = db.Column(db.String)
    notes = db.Column(db.String)

    def __init__(self, name, latitude, longitude, min, max, percentile, deployer, notes):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.min = min
        self.max = max
        self.percentile = percentile
        self.deployer = deployer
        self.notes = notes

    def __repr__(self):
        return '<name {}>'.format(self.name)

    def to_json(self):
        return {"id": self.id,
                "name": self.name,
                "latitude": self.latitude,
                "longitude": self.longitude}

    def get_id(self):
        return self.id

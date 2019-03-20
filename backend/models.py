from app import db

class Activity(db.Model):
    """
    Represents information about an activity.
    id (lowercase string)
    type (lowercase string (TODO: maybe enum?)
    url (string)
    name (string)
    description (string)
    latitude (number)
    longitude (number)
    location (string)
    is_active (boolean)
    is_free (boolean)
    image_1 (string)
    image_2 (string)
    image_3 (string)
    image_4 (string)
    ~~~~~~~~~~~(National Parks Only)~~~~~~~~~~~
    designation (string)
    weather (string)
    directions (string)
    ~~~~~~~~~~~((Meetup / Eventbrite Only)~~~~~~~~~~~
    date (string)
    """

    __tablename__ = "activity"
    id = db.Column(db.String(50), primary_key=True, nullable=False)
    type = db.Column(db.String(50), primary_key=True, nullable=False)
    url = db.Column(db.String(255))
    name = db.Column(db.String(255))
    description = db.Column(db.Text)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    location = db.Column(db.String(255))
    is_active = db.Column(db.Boolean)
    is_free = db.Column(db.Boolean)
    image_1 = db.Column(db.String(1000))
    image_2 = db.Column(db.String(1000))
    image_3 = db.Column(db.String(1000))
    image_4 = db.Column(db.String(1000))
    designation = db.Column(db.String(255))
    weather = db.Column(db.Text)
    directions = db.Column(db.Text)
    date = db.Column(db.String(1000))

    def __init__(self, id, type, url, name, description, latitude, longitude,
                location, is_active, is_free, image_1, image_2, image_3, image_4,
                designation, weather, directions, date):
        self.id = id
        self.type = type
        self.url = url
        self.name = name
        self.description = description
        self.latitude = latitude
        self.longitude = longitude
        self.location = location
        self.is_active = is_active
        self.is_free = is_free
        self.image_1 = image_1
        self.image_2 = image_2
        self.image_3 = image_3
        self.image_4 = image_4
        self.designation = designation
        self.weather = weather
        self.directions = directions
        self.date = date

    def __repr__(self):
        return '<id {} type {}>'.format(self.id, self.type)

    def serialize(self):
        return {
            "id": self.id,
            "type": self.type,
            "url": self.url,
            "name": self.name,
            "description": self.description,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "location": self.location,
            "is_active": self.is_active,
            "is_free": self.is_free,
            "image_1": self.image_1,
            "image_2": self.image_2,
            "image_3": self.image_3,
            "image_4": self.image_4,
            "designation": self.designation,
            "weather": self.weather,
            "directions": self.directions,
            "date": self.date,
        }

class Breed(db.Model):
    """
    Represents information about a breed.
    name (lowercase string)
    group (string)
    min_height (number)
    max_height (number)
    min_lifespan (number)
    max_lifespan (number)
    temperament (string)
    min_weight (number)
    max_weight (number)
    image_1 (string)
    image_2 (string)
    image_3 (string)
    image_4 (string)
    is_active (boolean)
    """

    __tablename__ = "breed"
    name = db.Column(db.String(255), primary_key=True, nullable=False)
    group = db.Column(db.String(255))
    min_height = db.Column(db.Float)
    max_height = db.Column(db.Float)
    min_lifespan = db.Column(db.Float)
    max_lifespan = db.Column(db.Float)
    temperament = db.Column(db.String(1000))
    min_weight = db.Column(db.Integer)
    max_weight = db.Column(db.Integer)
    image_1 = db.Column(db.String(1000))
    image_2 = db.Column(db.String(1000))
    image_3 = db.Column(db.String(1000))
    image_4 = db.Column(db.String(1000))
    is_active = db.Column(db.Boolean)

    def __init__(self, name, group, min_height, max_height, min_lifespan,
                max_lifespan, temperament, min_weight, max_weight,
                image_1, image_2, image_3, image_4, is_active):
        self.name = name
        self.group = group
        self.min_height = min_height
        self.max_height = max_height
        self.min_lifespan = min_lifespan
        self.max_lifespan = max_lifespan
        self.temperament = temperament
        self.min_weight = min_weight
        self.max_weight = max_weight
        self.image_1 = image_1
        self.image_2 = image_2
        self.image_3 = image_3
        self.image_4 = image_4
        self.is_active = is_active

    def __repr__(self):
        return '<name {}>'.format(self.name)

    def serialize(self):
        return {
            "name": self.name,
            "group": self.group,
            "min_height": self.min_height,
            "max_height": self.max_height,
            "min_lifespan": self.min_lifespan,
            "max_lifespan": self.max_lifespan,
            "temperament": self.temperament,
            "min_weight": self.min_weight,
            "max_weight": self.max_weight,
            "image_1": self.image_1,
            "image_2": self.image_2,
            "image_3": self.image_3,
            "image_4": self.image_4,
            "is_active": self.is_active
        }

# class Dog(db.Model):
#     """
#     Represents information about a dog.
#     id (number)
#     shelter_id (string)
#     name (string)
#     breed (lowercase string)
#     age (string)
#     size (string)
#     sex (string)
#     description (string)
#     image_1 (string)
#     image_2 (string)
#     image_3 (string)
#     image_4 (string)
#     """

class Shelter(db.Model):
    """
    Represents information about a shelter.
    id (string)
    name (string)
    latitude (number)
    longitude (number)
    city (string)
    state (string)
    zipcode (number)
    phone (string)
    address (string)
    """

    __tablename__ = "shelter"
    id = db.Column(db.String(25), primary_key=True, nullable=False)
    name = db.Column(db.String(255))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    city = db.Column(db.String(255))
    state = db.Column(db.String(50))
    zipcode = db.Column(db.Integer)
    phone = db.Column(db.String(50))
    address = db.Column(db.String(255))

    def __init__(self, id, name, latitude, longitude, city, state, zipcode, phone, address):
        self.id = id
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.phone = phone
        self.address = address

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "city": self.city,
            "state": self.state,
            "zipcode": self.zipcode,
            "phone": self.phone,
            "address": self.address
        }
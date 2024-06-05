# This file contains the mapping of class names to classes for easy access in file_storage.py and db_storage.py
from models.user import User
from models.property import Property
from models.room import Room
from models.booking import Booking
from models.review import Review
from models.university import University

classes = {
    "User": User,
    "Property": Property,
    "Room": Room,
    "Booking": Booking,
    "Review": Review,
    "University": University
}

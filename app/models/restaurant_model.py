from app.database import db
from uuid import uuid4

restaurants = []
class Restaurant(db.Model):
    """
    A class to represent a restaurant.

    Attributes:
        name (str): The name of the restaurant.
        address (str): The address of the restaurant.
        cuisine (str): The type of cuisine the restaurant offers.
        menu (list): A list of menu items with prices.
        work_hours (str): The working hours of the restaurant.
    """

    __tablename__ = 'restaurants'

    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid4()))
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    cuisine = db.Column(db.String, nullable=False)
    menu = db.Column(db.PickleType, nullable=False)  # Using PickleType to store list data
    work_hours = db.Column(db.String, nullable=True)

    def __init__(self, name, address, cuisine, menu, work_hours):
        self.name = name
        self.address = address
        self.cuisine = cuisine
        self.menu = menu
        self.work_hours = work_hours

    def update_details(self, address=None, cuisine=None, menu=None, work_hours=None):
        """Update the restaurant details."""
        if address:
            self.address = address
        if cuisine:
            self.cuisine = cuisine
        if menu:
            self.menu = menu
        if work_hours:
            self.work_hours = work_hours

class Restaurant:
    """
    A class to represent a restaurant.

    Attributes:
        name (str): The name of the restaurant.
        address (str): The address of the restaurant.
        cuisine (str): The type of cuisine the restaurant offers.
        menu (list): A list of menu items with prices.
        work_hours (str): The working hours of the restaurant.
    """

    def __init__(self, name, address, cuisine, menu, work_hours):
        """
        Constructs all the necessary attributes for the restaurant object.

        Args:
            name (str): The name of the restaurant.
            address (str): The address of the restaurant.
            cuisine (str): The type of cuisine the restaurant offers.
            menu (list): A list of menu items with prices.
            work_hours (str): The working hours of the restaurant.
        """
        self.name = name
        self.address = address
        self.cuisine = cuisine
        self.menu = menu  # List of dictionaries with item names and prices
        self.work_hours = work_hours

    def update_details(self, address=None, cuisine=None, menu=None, work_hours=None):
        """
        Update the restaurant details.

        Args:
            address (str): The new address of the restaurant.
            cuisine (str): The new cuisine of the restaurant.
            menu (list): The new menu of the restaurant.
            work_hours (str): The new working hours of the restaurant.
        """
        if address:
            self.address = address
        if cuisine:
            self.cuisine = cuisine
        if menu:
            self.menu = menu
        if work_hours:
            self.work_hours = work_hours

# In-memory storage for simplicity
restaurants = []

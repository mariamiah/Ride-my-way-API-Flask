class RideOffer:
    def __init__(self, id, driver, destination):
        self.id = id
        self.driver = driver
        self.destination = destination

    def get_dict(self):
        return{
            'id': self.id,
            'driver': self.driver,
            'destination': self.destination
        }

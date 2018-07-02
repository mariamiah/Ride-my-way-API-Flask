class RideOffer:
    def __init__(self,ride_id, driver, destination):
        self.ride_id = ride_id
        self.driver = driver
        self.destination = destination

    def get_dict(self):
        return{
            'ride_id': self.ride_id,
            'driver': self.driver,
            'destination': self.destination
        }
    def post_dict(self):
        return{
            'ride_id':self.ride_id,
            'driver':self.driver,
            'destination':self.destination
        }

from serviceable import Serviceable


class CarriganTire(Serviceable):
    def __init__(self, tire_quality):
        self.tire_quality = tire_quality

    def needs_service(self):
        return any(x >= 0.9 for x in self.tire_quality)

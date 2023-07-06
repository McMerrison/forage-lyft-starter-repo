from serviceable import Serviceable


class OctoprimeTire(Serviceable):
    def __init__(self, tire_quality):
        self.tire_quality = tire_quality

    def needs_service(self):
        return sum(self.tire_quality) > 3

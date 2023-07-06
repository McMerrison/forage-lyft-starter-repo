from datetime import datetime

from car import Car

class Calliope(Car):
    
    def __init__(self, engine, battery):
        super().__init__()

    def needs_service(self):
        return self.engine.should_be_serviced() or self.battery.should_be_serviced()


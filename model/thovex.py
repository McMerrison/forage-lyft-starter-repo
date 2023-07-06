from datetime import datetime

from car import Car

class Thovex(Car):
    
    def __init__(self) -> None:
        super().__init__()

    def needs_service(self):
        return self.engine.should_be_serviced() or self.battery.should_be_serviced()


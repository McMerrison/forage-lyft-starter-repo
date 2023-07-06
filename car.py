from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery
from tire.carrigan import CarriganTire
from tire.octoprime import OctoprimeTire

class Car():

    def __init__(self, engine, battery, tire):
        self.engine = engine
        self.battery = battery
        self.tire = tire

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service() or self.tire.needs_service()

class CarFactory:
    
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tire_quality):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tire = CarriganTire(tire_quality)
        return Car(engine, battery, tire)
    
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tire_quality):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tire = CarriganTire(tire_quality)
        return Car(engine, battery, tire)
    
    def create_palindrome(current_date, last_service_date, current_mileage, last_service_mileage, warning_light_is_on, tire_quality):
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(current_date, last_service_date)
        tire = OctoprimeTire(tire_quality)
        return Car(engine, battery, tire)
    
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tire_quality):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tire = OctoprimeTire(tire_quality)
        return Car(engine, battery, tire)
    
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tire_quality):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date) 
        tire = OctoprimeTire(tire_quality) 
        return Car(engine, battery, tire)
    
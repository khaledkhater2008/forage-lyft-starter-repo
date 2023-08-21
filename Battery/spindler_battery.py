from Battery import Battery
from datetime import datetime, timedelta


class SpindlerBattery(Battery):
    def __init__(self, current_date, last_service_date):
        super().__init__(current_date, last_service_date)
        self.BatteryExpiry = 2
    
    
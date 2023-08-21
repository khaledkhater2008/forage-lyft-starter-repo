from abc import ABC
from datetime import datetime, timedelta



class Battery(ABC):

    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self,BatteryExpiry):
        return (datetime.strptime(self.current_date, '%Y-%m-%d') - datetime.strptime(self.last_service_date, '%Y-%m-%d')) >= timedelta(days=365 * BatteryExpiry)

import unittest
from datetime import datetime, timedelta

from battery.nubbin_battery import NubbinBattery

class TestNubbinBattery(unittest.TestCase):
    def test_battery_should_be_serviced_exactly_4_years(self):
        current_date = datetime.fromisoformat("2023-05-01")
        last_service_date = datetime.fromisoformat("2019-01-01")
        battery = NubbinBattery(current_date,last_service_date)
        self.assertTrue(battery.needs_service(battery.BatteryExpiry))

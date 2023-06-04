import unittest
import datetime

from engines.capulet import CapuletEngine
from engines.sternman import SternmanEngine
from engines.willoughby import WilloughbyEngine
from batteries.nubbin import NubbinBattery
from batteries.spindler import SpindlerBattery
from tires.carrigan import CarriganTire
from tires.octoprime import OctoprimeTire

class TestSternmanEngine(unittest.TestCase):
    def test_should_be_serviced(self):
        engine = SternmanEngine(False)
        self.assertFalse(engine.needs_service())

    def test_should_not_be_serviced(self):
        engine = SternmanEngine(True)
        self.assertTrue(engine.needs_service())

class TestWilloughbyEngine(unittest.TestCase):
    def test_should_be_serviced(self):
        engine = WilloughbyEngine(61000, 127000)
        self.assertTrue(engine.needs_service())

    def test_should_not_be_serviced(self):
        engine = WilloughbyEngine(61000, 90000)
        self.assertFalse(engine.needs_service())


class TestCapuletEngine(unittest.TestCase):
    def test_should_be_serviced(self):
        engine = CapuletEngine(61000, 100000)
        self.assertTrue(engine.needs_service())

    def test_should_not_be_serviced(self):
        engine = CapuletEngine(61000, 70000)
        self.assertFalse(engine.needs_service())

'''
Old tests for spindler battery (when it needed service every 2 years)

class TestSpindlerBattery(unittest.TestCase):
    def test_should_be_serviced(self):
        today = datetime.date.today()
        three_years_ago = today.replace(year=today.year - 3)
        engine = SpindlerBattery(three_years_ago, today)
        self.assertTrue(engine.needs_service())

    def test_should_not_be_serviced(self):
        today = datetime.date.today()
        one_year_ago = today.replace(year=today.year - 1)
        engine = SpindlerBattery(one_year_ago, today)
        self.assertFalse(engine.needs_service())
'''

class TestNubbinBattery(unittest.TestCase):
    def test_should_be_serviced(self):
        today = datetime.date.today()
        five_years_ago = today.replace(year=today.year - 5)
        engine = NubbinBattery(five_years_ago, today)
        self.assertTrue(engine.needs_service())

    def test_should_not_be_serviced(self):
        today = datetime.date.today()
        two_years_ago = today.replace(year=today.year - 2)
        engine = NubbinBattery(two_years_ago, today)
        self.assertFalse(engine.needs_service())


'''
Old tests for spindler battery (when it needs service every 3 years)
'''
class TestSpindlerBattery(unittest.TestCase):
    def test_should_be_serviced(self):
        today = datetime.date.today()
        four_years_ago = today.replace(year=today.year - 4)
        engine = SpindlerBattery(four_years_ago, today)
        self.assertTrue(engine.needs_service())

    def test_should_not_be_serviced(self):
        today = datetime.date.today()
        one_year_ago = today.replace(year=today.year - 1)
        engine = SpindlerBattery(one_year_ago, today)
        self.assertFalse(engine.needs_service())

'''
Tests for the tires  
'''
class TestCarriganTire(unittest.TestCase):
    def test_should_be_serviced(self):
        tire = CarriganTire([0.95, 0.2, 0.3, 0.99])
        self.assertTrue(tire.needs_service())

    def test_should_not_be_serviced(self):
        tire = CarriganTire([0.83, 0.2, 0.7, 0.59])
        self.assertFalse(tire.needs_service())

class TestOctoprimeTire(unittest.TestCase):
    def test_should_be_serviced(self):
        tire = OctoprimeTire([0.95, 0.92, 0.93, 0.5])
        self.assertTrue(tire.needs_service())

    def test_should_not_be_serviced(self):
        tire = OctoprimeTire([0.23, 0.2, 0.7, 0.39])
        self.assertFalse(tire.needs_service())

if __name__ == '__main__':
    unittest.main()

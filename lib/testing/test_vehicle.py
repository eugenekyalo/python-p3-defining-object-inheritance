# lib/testing/test_vehicle.py
import unittest
from lib.vehicle import Vehicle
from lib.car import Car

class TestVehicle(unittest.TestCase):

    def test_vehicle_initialization(self):
        v = Vehicle('large', 4)
        self.assertEqual(v.wheel_size, 'large')
        self.assertEqual(v.wheel_number, 4)

    def test_vehicle_go(self):
        v = Vehicle('large', 4)
        self.assertEqual(v.go(), "vrrrrrrrooom!")

    def test_vehicle_fill_up_tank(self):
        v = Vehicle('large', 4)
        self.assertEqual(v.fill_up_tank(), "filling up!")

class TestCar(unittest.TestCase):

    def test_car_initialization(self):
        c = Car('medium', 4)
        self.assertEqual(c.wheel_size, 'medium')
        self.assertEqual(c.wheel_number, 4)

    def test_car_go(self):
        c = Car('medium', 4)
        self.assertEqual(c.go(), "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!")

    def test_car_fill_up_tank(self):
        c = Car('medium', 4)
        self.assertEqual(c.fill_up_tank(), "filling up!")

if __name__ == '__main__':
    unittest.main()

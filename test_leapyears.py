import unittest
from leapyears import LeapYears

class TestLeapYears(unittest.TestCase):

    def setUp(self):
        self.leap_years = LeapYears()

    def testIsLeapFrom400(self):
        self.assertTrue(self.leap_years.isLeapYear(2000))

    def testIsNotLeapFrom100AndNot400(self):
        self.assertFalse(self.leap_years.isLeapYear(1900))

    def testIsLeapFor4AndNot100(self):
        self.assertTrue(self.leap_years.isLeapYear(2008))

    def testIsNotLeapForNot4(self):
        self.assertFalse(self.leap_years.isLeapYear(2017))